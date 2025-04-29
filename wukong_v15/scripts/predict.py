import os
import sys
import json
import paddlex as pdx

def predict_images(model_dir, image_dir, output_dir):
    """
    对指定目录下的图片进行推理预测并保存结果
    Args:
        model_dir (str): 模型目录路径
        image_dir (str): 图片目录路径
        output_dir (str): 结果保存目录
    """
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 加载模型
    model = pdx.create_model(
        model_name="MobileNetV3_small_x1_0",
        model_dir=model_dir
    )
    
    # 获取所有图片文件
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # 处理每张图片
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        base_name = os.path.splitext(image_file)[0]
        
        # 执行推理
        result = model.predict(image_path)
        
        # 保存结果图片
        result_img_path = os.path.join(output_dir, f"{base_name}_res.jpg")
        result_json_path = os.path.join(output_dir, f"{base_name}_res.json")
        
        # 保存结果到JSON文件
        with open(result_json_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            
        print(f"处理完成: {image_file}")
        print(f"结果已保存: {result_json_path}")

def main():
    # 设置路径
    model_dir = "/home/nvidia/ai-lab/wukong_v15/data/itx/output/mobilenetv3_small/best_model/inference"
    image_dir = "/home/nvidia/ai-lab/test/test_images"
    output_dir = "/home/nvidia/ai-lab/test/output"
    
    try:
        predict_images(model_dir, image_dir, output_dir)
        print("所有图片处理完成!")
        
    except Exception as e:
        print(f"发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()