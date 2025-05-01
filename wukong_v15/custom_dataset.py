from ppdet.core.workspace import register
from ppdet.data.source.keypoint_coco import KeypointTopDownCocoDataset
import copy
import os # Added import
import numpy as np # Added import

@register
class CustomKeypointDataset(KeypointTopDownCocoDataset):
    # Note: The first __init__ below is overridden by the second one.
    # Consider removing the first one if it's not needed.
    # def __init__(self, **kwargs):
    #     super(CustomKeypointDataset, self).__init__(**kwargs)
    #     # Add any custom initialization here if needed

    """Custom dataset class with dynamic image setting capability"""

    def __init__(self, *args, **kwargs):
        # Remove 'type' and potentially 'name' and 'module' if they cause issues,
        # as they are often part of the configuration but not direct init parameters.
        kwargs.pop('type', None)
        kwargs.pop('name', None)
        kwargs.pop('module', None)
        super().__init__(*args, **kwargs)
        self.custom_images = []

    def set_images(self, image_paths):
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
