import os
import sys
import paddle
import paddlex as pdx

def main():
    try:
        # Try loading with PaddleX
        print("Attempting to load with PaddleX...")
        model_dir = '/home/nvidia/ai-lab/wukong_v15/data/itx/output/mobilenetv3_small/best_model'
        model = pdx.load_model(model_dir)
        print("Model loaded successfully with PaddleX")
        print(f"Model type: {type(model)}")
        
        # Try loading parameters directly
        print("\nAttempting to load parameters directly...")
        params_path = os.path.join(model_dir, 'best_model.pdparams')
        state_dict = paddle.load(params_path)
        print("Parameters loaded successfully")
        print(f"Parameter keys: {state_dict.keys()}")
        
    except Exception as e:
        import traceback
        print(f"Error occurred: {str(e)}", file=sys.stderr)
        print("Traceback:", file=sys.stderr)
        traceback.print_exc()

if __name__ == '__main__':
    main()