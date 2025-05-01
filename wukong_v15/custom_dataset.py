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

        # The logic for creating dummy annotations and populating self.db
        # is now handled within the set_images method and its nested
        # custom_parse_dataset function.
        # get_imid2path should primarily focus on returning the mapping
        # if it's already generated or based on standard dataset loading.

        # Example: If using standard COCO loading, the parent's logic might be sufficient
        # or needs adaptation here based on how self.roidbs or similar is populated.
        if hasattr(self, 'roidbs') and self.roidbs:
             for record in self.roidbs:
                 if 'id' in record and 'im_file' in record:
                     imid2path[record['id']] = record['im_file']
        elif hasattr(self, 'db') and self.db: # If db populated by custom_parse_dataset
            for i, ann in enumerate(self.db):
                # Assuming 'image_file' holds the path and we use index as ID for custom images
                imid2path[i] = ann.get('image_file', ann.get('image'))

        if not imid2path and hasattr(self, 'custom_images') and self.custom_images:
             print("Warning: get_imid2path() called but custom_images are set. "
                   "Ensure set_images() was called and populated the dataset correctly.")
        elif not imid2path:
             print("Warning: get_imid2path() is returning an empty dictionary. "
                   "Ensure dataset loading or set_images() populates necessary structures.")

        return imid2path

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
