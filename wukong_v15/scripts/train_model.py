import os
import sys
import paddlex as pdx

def main():
    # Load configuration
    model = pdx.load_model("./data/itx/output/mobilenetv3_small/best_model")
    
    # Export model for inference
    save_dir = "./data/itx/output/mobilenetv3_small/best_model/inference"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    model.export(save_dir)
    print(f"Model exported to {save_dir}")

if __name__ == "__main__":
    main()