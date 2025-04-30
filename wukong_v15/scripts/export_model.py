import os
import paddlex as pdx

def main():
    try:
        # Define model paths
        base_dir = "/home/nvidia/ai-lab/output/mobilenetv3_small"
        model_dir = os.path.join(base_dir, "best_model")
        
        if not os.path.exists(model_dir):
            raise ValueError(f"Model directory not found: {model_dir}")
        
        # Create model with parameters loaded from best_model
        model = pdx.create_model(
            model_name="MobileNetV3_small_x1_0",
            model_dir=model_dir
        )
        
        # Export model for inference
        save_dir = os.path.join(model_dir, "inference")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            
        model.export(save_dir, 
                     input_shape=[3, 224, 224]
                     )
        print(f"Model exported successfully to {save_dir}")

    except Exception as e:
        print(f"Error occurred: {e}")
        raise e

if __name__ == "__main__":
    main()