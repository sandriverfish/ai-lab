import sys
import os
import runpy

# 1. Ensure custom module is found (already handled by PYTHONPATH)

# 2. Explicitly import custom dataset module
try:
    from wukong_v15.custom_dataset import CustomKeypointDataset
    print("Successfully imported custom dataset class.")
except ImportError as e:
    print(f"Error importing custom dataset class: {e}")
    print("Please ensure 'wukong_v15' is in PYTHONPATH and custom_dataset.py exists.")
    sys.exit(1)

# --- Workaround Start ---
# Import the target module and add the custom class to its namespace
try:
    import ppdet.data.source
    setattr(ppdet.data.source, 'CustomKeypointDataset', CustomKeypointDataset)
    print("Successfully added CustomKeypointDataset to ppdet.data.source namespace.")
except ImportError:
    print("Warning: Could not import ppdet.data.source. The workaround might not be effective.")
except Exception as e:
    print(f"Warning: Error applying workaround: {e}")
# --- Workaround End ---


# 3. Prepare arguments for infer.py
infer_script_path = '/home/nvidia/ai-lab/PaddleX/paddlex/repo_manager/repos/PaddleDetection/tools/infer.py'
config_file = 'config/tinypose_keypoint.yaml'
weights_path = 'output/pp_tinypose_itx/model_final.pdparams'
infer_image = 'data/itx/images/itx_board_007.jpg'
output_dir = 'output/inference_results'

# Build sys.argv for infer.py
sys.argv = [
    infer_script_path,
    '-c', config_file,
    '-o', f'weights={weights_path}',
    '--infer_img', infer_image,
    '--output_dir', output_dir
]

print(f"Running {infer_script_path} with args: {sys.argv}")

# 4. Execute infer.py using runpy
try:
    runpy.run_path(infer_script_path, run_name="__main__")
except Exception as e:
    print(f"Error running infer.py: {e}")
    import traceback
    traceback.print_exc()
