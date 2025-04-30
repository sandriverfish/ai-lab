import os
import json
import paddlex as pdx
import numpy as np
import cv2

def convert_numpy_types(obj):
    """
    转换 NumPy 数据类型为 Python 原生类型
    """
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {key: convert_numpy_types(value) for key, value in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convert_numpy_types(item) for item in obj]
    return obj

def draw_prediction_results(image_path, predictions, save_path):
    """
    在图片上绘制预测结果
    Args:
        image_path: 输入图片路径
        predictions: 预测结果
        save_path: 保存路径
    """
    # 读取图片
    image = cv2.imread(image_path)
    
    # 获取图片尺寸
    height, width = image.shape[:2]
    
    # 设置文本参数
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    thickness = 2
    margin = 10
    text_height = 30
    
    # 在图片顶部绘制半透明背景
    n_results = min(5, len(predictions['scores']))  # 最多显示前5个结果
    overlay_height = (text_height + margin) * n_results
    overlay = image.copy()
    cv2.rectangle(overlay, (0, 0), (width, overlay_height + margin), 
                 (0, 0, 0), -1)
    alpha = 0.7
    image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    
    # 绘制每个预测结果
    for i in range(n_results):
        score = predictions['scores'][i]
        label = predictions['label_names'][i]
        text = f"{label}: {score:.2%}"
        
        # 计算文本位置
        y_pos = margin + (i + 1) * text_height
        
        # 绘制文本
        cv2.putText(image, text, (margin, y_pos), font, font_scale, 
                   (255, 255, 255), thickness)
        
        # 如果置信度超过50%，绘制边界框
        if score > 0.5:
            # 设置边框参数
            border_margin = 20  # 边框到图像边缘的距离
            border_thickness = 3
            border_color = (0, 255, 0)  # 绿色边框
            
            # 绘制边界框
            cv2.rectangle(image, 
                        (border_margin, border_margin), 
                        (width - border_margin, height - border_margin),
                        border_color,
                        border_thickness)
            
            # 在边框右下角添加标签
            label_text = f"{label}: {score:.2%}"
            text_size = cv2.getTextSize(label_text, font, font_scale, thickness)[0]
            text_x = width - border_margin - text_size[0] - 5
            text_y = height - border_margin - 5
            
            # 绘制文本背景
            cv2.rectangle(image,
                        (text_x - 5, text_y - text_size[1] - 5),
                        (text_x + text_size[0] + 5, text_y + 5),
                        border_color,
                        -1)
            
            # 绘制文本
            cv2.putText(image, label_text,
                       (text_x, text_y),
                       font, font_scale,
                       (0, 0, 0),  # 黑色文字
                       thickness)
    
    # 保存结果图片
    cv2.imwrite(save_path, image)

def format_prediction_result(raw_result):
    """
    格式化预测结果，严格按照官方示例格式
    """
    # 先将生成器转换为列表
    if hasattr(raw_result, '__iter__') and not isinstance(raw_result, (dict, list)):
        raw_result = list(raw_result)
    
    # 获取第一个结果
    result = raw_result[0] if isinstance(raw_result, (list, tuple)) else raw_result
    
    # 转换 NumPy 类型
    result = convert_numpy_types(result)

    # 严格按照官方示例格式构建输出
    formatted_result = {
        "input_path": result.get('input_path', ''),
        "page_index": None,
        "class_ids": result.get('class_ids', [])[:5],  # 只取前5个
        "scores": result.get('scores', [])[:5],        # 只取前5个
        "label_names": result.get('label_names', [])[:5]  # 只取前5个
    }
    
    return formatted_result

def predict_single_image(model_dir, image_path, save_dir):
    """
    对单张图片进行预测
    """
    try:
        os.makedirs(save_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        
        # 加载模型
        model = pdx.create_model(
            model_name="MobileNetV3_small_x1_0",
            model_dir=model_dir
        )
        
        # 执行预测并将生成器转换为列表
        result = model.predict(image_path)
        if hasattr(result, '__iter__') and not isinstance(result, (dict, list)):
            result = list(result)
        
        # 格式化结果
        formatted_result = format_prediction_result(result)
        
        # 保存 JSON 结果
        result_file = os.path.join(save_dir, f"{base_name}_result.json")
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(formatted_result, f, indent=2, ensure_ascii=False)
        
        # 生成并保存可视化结果
        vis_file = os.path.join(save_dir, f"{base_name}_result.jpg")
        draw_prediction_results(image_path, formatted_result, vis_file)
            
        print(f"预测完成！")
        print(f"结果文件已保存到: {result_file}")
        print(f"可视化结果已保存到: {vis_file}")
        print("\n预测结果:")
        print(json.dumps(formatted_result, indent=2, ensure_ascii=False))
        
        return formatted_result
        
    except Exception as e:
        print(f"预测过程中出现错误: {e}")
        raise e

if __name__ == "__main__":
    # 设置路径
    model_dir = "/home/nvidia/ai-lab/wukong_v15/data/itx/output/mobilenetv3_small/best_model/inference"
    test_image_dir = "/home/nvidia/ai-lab/test/test_images"
    output_dir = "/home/nvidia/ai-lab/test/output"
    
    # 获取所有图片文件
    image_files = [f for f in os.listdir(test_image_dir) 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    
    # 处理每张图片
    for image_file in image_files:
        print(f"\n处理图片: {image_file}")
        image_path = os.path.join(test_image_dir, image_file)
        predict_single_image(model_dir, image_path, output_dir)