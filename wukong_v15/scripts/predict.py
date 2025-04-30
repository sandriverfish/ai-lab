import os
import json
import paddlex as pdx
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

def format_prediction_result(raw_result):
    """
    格式化预测结果，只保留必要信息
    """
    if isinstance(raw_result, list):
        raw_result = raw_result[0]  # 获取第一个结果
    
    # 提取关键信息
    formatted_result = {
        'class_ids': raw_result.get('class_ids', []),
        'scores': raw_result.get('scores', []),
        'label_names': raw_result.get('label_names', []),
        'input_path': raw_result.get('input_path', '')
    }
    
    # 只保留前5个最高置信度的结果
    if len(formatted_result['class_ids']) > 5:
        formatted_result['class_ids'] = formatted_result['class_ids'][:5]
        formatted_result['scores'] = formatted_result['scores'][:5]
        formatted_result['label_names'] = formatted_result['label_names'][:5]
    
    return formatted_result

def predict_single_image(model_dir, image_path, save_dir):
    try:
        os.makedirs(save_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        
        # 加载模型
        model = pdx.create_model(
            model_name="MobileNetV3_small_x1_0",
            model_dir=model_dir
        )
        
        # 执行预测
        results = model.predict(image_path)
        
        # 格式化结果
        formatted_results = format_prediction_result(results)
        
        # 保存结果
        result_file = os.path.join(save_dir, f"{base_name}_result.json")
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(formatted_results, f, cls=NumpyEncoder, ensure_ascii=False, indent=2)
            
        print(f"预测完成！结果已保存到: {result_file}")
        print("\n预测结果:")
        print(json.dumps(formatted_results, cls=NumpyEncoder, ensure_ascii=False, indent=2))
        
        return formatted_results
        
    except Exception as e:
        print(f"预测过程中出现错误: {e}")
        raise e

def predict_directory(model_dir, image_dir, save_dir):
    image_files = [f for f in os.listdir(image_dir) 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    
    results = {}
    for image_file in image_files:
        print(f"\n处理图片: {image_file}")
        image_path = os.path.join(image_dir, image_file)
        result = predict_single_image(model_dir, image_path, save_dir)
        results[image_file] = result
    
    # 保存汇总结果
    summary_file = os.path.join(save_dir, "prediction_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, cls=NumpyEncoder, ensure_ascii=False, indent=2)
    
    print(f"\n所有预测完成！汇总结果保存在: {summary_file}")

if __name__ == "__main__":
    model_dir = "/home/nvidia/ai-lab/wukong_v15/data/itx/output/mobilenetv3_small/best_model/inference"
    test_image_dir = "/home/nvidia/ai-lab/test/test_images"
    output_dir = "/home/nvidia/ai-lab/test/output"
    
    predict_directory(model_dir, test_image_dir, output_dir)