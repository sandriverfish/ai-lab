from ppdet.core.workspace import register
from ppdet.data.source.keypoint_coco import KeypointTopDownCocoDataset
import copy
import os # Added import
import numpy as np # Added import

@register
class CustomKeypointDataset(KeypointTopDownCocoDataset):
    """Custom dataset class with dynamic image setting capability"""

    def __init__(self, *args, **kwargs):
        # Remove 'type' and potentially 'name' and 'module' if they cause issues,
        # as they are often part of the configuration but not direct init parameters.
        # These are handled by the factory/registry mechanism.
        kwargs.pop('type', None)
        kwargs.pop('name', None)
        kwargs.pop('module', None)
        # Initialize the parent class with the remaining relevant arguments
        super().__init__(*args, **kwargs)
        self.custom_images = [] # Initialize list for custom images if needed later

    def get_imid2path(self):
        """
        Returns a dictionary mapping image IDs to their file paths.
        This implementation needs to be robust for inference scenarios
        where annotations might not be fully loaded or available.
        """
        imid2path = {}

        # If --infer_img is used, self.custom_images should be populated
        if hasattr(self, 'custom_images') and self.custom_images:
            # For inference on specific images, create mapping based on these
            for i, img_path in enumerate(self.custom_images): # Add index 'i'
                # Create dummy annotation data for single image inference
                # The structure should match what the transforms expect
                dummy_ann = {
                    'im_id': i, # Add image ID using the index
                    'image': img_path, # Use 'image' key as often expected by transforms
                    'image_file': img_path, # Keep original key too if needed
                    'bbox': np.array([0, 0, 10, 10], dtype=np.float32), # Dummy bbox, might be refined later
                    'center': np.array([5, 5]),  # Dummy center
                    'scale': np.array([1.0, 1.0]), # Dummy scale
                    'joints_3d': np.zeros((num_joints, 3), dtype=np.float32), # Use num_joints
                    'joints_3d_visible': np.zeros((num_joints, 3), dtype=np.float32), # Use num_joints
                    # Add other fields expected by transforms if necessary
                }
                self.db.append(dummy_ann)
            print(f"Custom parse dataset created db with {len(self.db)} entries.")

        # Replace parse_dataset with our custom version for this instance
        self.parse_dataset = lambda: custom_parse_dataset(self)
        # Call the overridden parse_dataset immediately to populate self.db
        self.parse_dataset()

    # Ensure other necessary methods from KeypointTopDownCocoDataset are inherited
    # or defined if they need custom behavior. For example, __len__ and __getitem__.

    # You might need to override __len__ if parse_dataset is dynamically changed
    def __len__(self):
        if hasattr(self, 'db'):
            return len(self.db)
        # Fallback to parent's __len__ if db isn't populated by custom logic yet
        # return super().__len__()
        # Or return 0 if db is the sole source of length info in this custom class
        return 0

# --- The second, incorrect class definition below should be REMOVED ---
# class CustomKeypointDataset: # <--- REMOVE THIS BLOCK
#     def __init__(self, **kwargs):
#         super(CustomKeypointDataset, self).__init__(**kwargs)
#         # Add any custom initialization here if needed
#     def get_imid2path(self):
#         """
#         Returns a dictionary mapping image IDs to their file paths.
#         Adjust the implementation based on how your dataset handles image IDs and paths.
#         """
#         imid2path = {}
#         # Example: Assuming self.roidbs holds image information
#         # You might need to adapt this based on your actual class structure
#         if hasattr(self, 'roidbs') and self.roidbs:
#              for record in self.roidbs:
#                  # Assuming 'id' and 'im_file' keys exist in your records
#                  if 'id' in record and 'im_file' in record:
#                      imid2path[record['id']] = record['im_file']
#                  # If your dataset doesn't use 'id', you might need to generate
#                  # sequential IDs or use filenames as keys if appropriate.
#                  # Example using index as ID if 'id' is missing:
#                  # elif 'im_file' in record:
#                  #    image_index = self.roidbs.index(record) # Or some other unique index
#                  #    imid2path[image_index] = record['im_file']
# 
#         # If your dataset doesn't load annotations during inference (e.g., only image files),
#         # you might need to build this mapping differently, perhaps by listing files
#         # in the image directory.
#         # Example:
#         # image_dir = os.path.join(self.dataset_dir, self.image_dir)
#         # image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
#         # for i, fname in enumerate(image_files):
#         #     imid2path[i] = os.path.join(image_dir, fname)
# 
# 
#         if not imid2path:
#              print("Warning: get_imid2path() is returning an empty dictionary. "
#                    "Ensure your CustomKeypointDataset correctly loads or generates image paths and IDs.")
# 
#         return imid2path

    def set_images(self, image_paths, **kwargs): # Accept extra keyword arguments
        """Set custom image paths for inference"""
        self.custom_images = image_paths
        # Override the parse_dataset method to use our custom images
        def custom_parse_dataset(self):
            self.db = []
            for img_path in self.custom_images:
                # Create dummy annotation data for single image inference
                img_name = os.path.basename(img_path)
                # Use absolute path to avoid directory issues
                dummy_ann = {
                    'image_file': os.path.abspath(img_path),
                    'center': np.array([0, 0]),  # Will be calculated later
                    'scale': np.array([0, 0]),    # Will be calculated later
                    'gt_joints': np.zeros((self.ann_info['num_joints'], 3), dtype=np.float32),
                    'joints_vis': np.zeros((self.ann_info['num_joints'], 3), dtype=np.float32)
                }
                self.db.append(dummy_ann)
        # Replace parse_dataset with our custom version
        self.parse_dataset = lambda: custom_parse_dataset(self)
