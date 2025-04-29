#!/usr/bin/env python3
import paddlex as pdx

def run_prediction():
    pipeline = pdx.create_pipeline(
        pipeline="ImageClassification",
        model_dir="/home/nvidia/ai-lab/wukong_v15/data/itx/output/mobilenetv3_small/best_model/inference",
        device="gpu:0"
    )
    result = pipeline.predict("/home/nvidia/ai-lab/test/test_images/itx1.jpg")
    print(f"预测类别：{result['class_name']}, 置信度：{result['score']}")

if __name__ == "__main__":
    run_prediction()
