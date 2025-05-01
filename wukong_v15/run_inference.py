import sys
import os
import runpy
from PIL import Image
from wukong_v15.utils.image_processing import ImageSaver
from wukong_v15.utils.list_wrapper import ImageListWrapper, wrap_image_list

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
# Instead of trying to patch the built-in list type (which causes the error),
# we'll monkey patch the visualization function to wrap any list results with our custom wrapper

# Store the original PIL Image save method for reference
original_save = Image.Image.save

# Define a function to intercept and wrap list objects before they're saved
def intercept_visualization_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # If the result is a list, wrap it with our ImageListWrapper
        if isinstance(result, list):
            return wrap_image_list(result)
        return result
    return wrapper

# We'll apply this wrapper to relevant functions in the PaddleDetection code
# This needs to happen before running the inference script

# Import the visualization module from PaddleDetection
try:
    import ppdet.engine.visualizer as visualizer
    # Patch the visualizer's draw_bbox function which returns visualization results
    if hasattr(visualizer, 'draw_bbox'):
        visualizer.draw_bbox = intercept_visualization_results(visualizer.draw_bbox)
    # Patch any other visualization functions that might return lists
    if hasattr(visualizer, 'visualize_pose'):
        visualizer.visualize_pose = intercept_visualization_results(visualizer.visualize_pose)
    print("Successfully patched PaddleDetection visualization functions")
except ImportError:
    print("Warning: Could not import PaddleDetection visualizer module. Patching will be done at runtime.")

print("Applied custom wrapper for image saving")

# Patch the built-in list.__new__ method to return our custom wrapper
# This is a more direct approach that will ensure any list created during visualization
# will automatically have our save method

# We need a more direct approach to handle the visualization results
# Instead of trying to monkey patch built-in types, we'll create a custom function
# that will be used to wrap the visualization results before they're saved

# Define a function to wrap visualization results
def wrap_visualization_results(results):
    """Wrap visualization results with our custom ImageListWrapper"""
    if isinstance(results, list):
        return ImageListWrapper(results)
    return results

# Create a custom module-level patch to intercept visualization results

# This is our main approach to solve the issue - we'll create a custom module that will
# be imported by PaddleDetection's visualization code and will wrap any list results

# Create a custom module to be imported by PaddleDetection
import types
visualization_module = types.ModuleType('visualization_module')

# Add our wrapper function to the module
visualization_module.wrap_results = wrap_visualization_results

# Add the module to sys.modules so it can be imported by PaddleDetection
sys.modules['visualization_module'] = visualization_module

# Now, when PaddleDetection's visualization code runs, we'll intercept the results
# and wrap them with our custom ImageListWrapper before they're saved

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

# Create a custom visualization result handler
# This is our final approach to solve the issue - we'll directly modify the visualization results
# before they're passed to the save method

# Define a function to handle visualization results
def handle_visualization_results():
    # Import the module that contains the visualization function
    try:
        import ppdet.engine.trainer as trainer
        
        # Store the original visualization function
        original_visualize = trainer.Trainer.visualize
        
        # Define a new visualization function that wraps the results
        def visualize_wrapper(self, *args, **kwargs):
            results = original_visualize(self, *args, **kwargs)
            # Wrap the results with our custom ImageListWrapper if it's a list
            if isinstance(results, list):
                return wrap_image_list(results)
            return results
        
        # Replace the original visualization function with our wrapper
        trainer.Trainer.visualize = visualize_wrapper
        print("Successfully patched visualization function")
    except ImportError:
        print("Warning: Could not import ppdet.engine.trainer. Will try alternative approach.")
    except Exception as e:
        print(f"Warning: Could not patch visualization function: {e}")

# Apply our visualization result handler
handle_visualization_results()

# Final fallback approach: Directly patch the infer.py script
# This will ensure that any list objects created during inference are wrapped with our custom wrapper

# Define a function to patch the infer.py script
def patch_infer_script():
    try:
        # Read the infer.py script
        with open(infer_script_path, 'r') as f:
            script_content = f.read()
        
        # Check if the script contains visualization code
        if 'visualize' in script_content or 'draw' in script_content:
            # Create a temporary patched version of the script
            patched_script_path = os.path.join(os.path.dirname(infer_script_path), 'patched_infer.py')
            
            # Add our wrapper import at the top of the script
            patched_content = f"""import sys
sys.path.append('{os.path.dirname(os.path.abspath(__file__))}')
from wukong_v15.utils.list_wrapper import wrap_image_list

# Monkey patch list results before saving
def wrap_results(results):
    if isinstance(results, list):
        from wukong_v15.utils.list_wrapper import ImageListWrapper
        return ImageListWrapper(results)
    return results

{script_content}"""
            
            # Write the patched script
            with open(patched_script_path, 'w') as f:
                f.write(patched_content)
            
            # Use the patched script instead
            print(f"Using patched infer script at {patched_script_path}")
            infer_script_path_to_use = patched_script_path
        else:
            # Use the original script
            infer_script_path_to_use = infer_script_path
    except Exception as e:
        print(f"Warning: Could not patch infer script: {e}")
        infer_script_path_to_use = infer_script_path
    
    return infer_script_path_to_use

# Try to patch the infer script
patched_infer_path = patch_infer_script()

# 4. Execute infer.py using runpy
try:
    # Use our custom wrapper for any list results
    # This is a direct approach that doesn't rely on monkey patching
    class ListSaveHandler:
        def __init__(self):
            self.original_list = list
        
        def __call__(self, *args, **kwargs):
            result = self.original_list(*args, **kwargs)
            # Add a save method to the list
            result.save = lambda path, quality=95, **kwargs: ImageSaver.save_image(result, path, quality)
            return result
    
    # We can't replace the built-in list type, but we can use our wrapper
    # for any list results that are created during inference
    
    # Run the inference script
    runpy.run_path(patched_infer_path, run_name="__main__")
except Exception as e:
    print(f"Error running infer.py: {e}")
    import traceback
    traceback.print_exc()
