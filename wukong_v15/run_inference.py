import sys
import os
import runpy
from PIL import Image
from wukong_v15.utils.image_processing import ImageSaver

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

# --- Monkey Patch for Image Saving ---
# This patch intercepts the image.save() call in PaddleDetection's trainer.py
# to handle the case where 'image' is a list instead of a PIL Image

# Store the original PIL Image save method
original_save = Image.Image.save

# Define a new save method for lists
def list_save_patch(self, path, quality=95, **kwargs):
    # Use our ImageSaver utility to handle both Image objects and lists of Images
    try:
        ImageSaver.save_image(self, path, quality)
    except Exception as e:
        print(f"Monkey patch caught exception: {e}")
        # Fallback: try to save the first item if it's an image
        if len(self) > 0 and hasattr(self[0], 'save'):
            self[0].save(path, quality=quality, **kwargs)
        else:
            print(f"Warning: Could not save image at {path}. Object is not a valid image or list of images.")
            # Re-raise if we can't handle it
            raise

# Apply the monkey patch to both PIL.Image and list objects
Image.Image.save = original_save  # Ensure the original method is preserved
list.save = list_save_patch  # Add save method to list class

print("Applied monkey patch for image saving")

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
