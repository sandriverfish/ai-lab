from ppdet.core.workspace import register
from ppdet.data.source.keypoint_coco import KeypointTopDownCocoDataset
import copy
import os # Added import
import numpy as np # Added import
import logging

logger = logging.getLogger(__name__)

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
                # Use the im_id we added in set_images method if available
                if 'im_id' in ann and ('image_file' in ann or 'image' in ann):
                    imid2path[ann['im_id']] = ann.get('image_file', ann.get('image'))
                # Fallback to using index as ID if im_id is not present
                elif 'image_file' in ann or 'image' in ann:
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
            for i, img_path in enumerate(self.custom_images):
                # Create dummy annotation data for single image inference
                img_name = os.path.basename(img_path)
                # Use absolute path to avoid directory issues
                dummy_ann = {
                    'image_file': os.path.abspath(img_path),
                    'im_id': i,  # Add image ID for inference pipeline
                    'center': np.array([0, 0]),  # Will be calculated later
                    'scale': np.array([0, 0]),    # Will be calculated later
                    'gt_joints': np.zeros((self.ann_info['num_joints'], 3), dtype=np.float32),
                    'joints_vis': np.zeros((self.ann_info['num_joints'], 3), dtype=np.float32)
                }
                self.db.append(dummy_ann)
        # Replace parse_dataset with our custom version
        self.parse_dataset = lambda: custom_parse_dataset(self)
        
        # Set custom skeleton for visualization
        # This is needed to avoid index out of bounds errors in visualization
        # The default skeleton might expect more keypoints than we have
        try:
            from ppdet.utils import visualizer
            # Check if the visualizer module has the draw_pose function
            if hasattr(visualizer, 'draw_pose'):
                # Save the original draw_pose function
                original_draw_pose = visualizer.draw_pose
                
                # Define a wrapper function that handles our custom keypoint structure
                def custom_draw_pose(image, results, visual_thread=0.6):
                    try:
                        # Create a custom skeleton that only uses our available keypoints
                        # Our model has 6 keypoints (indexed 0-5)
                        num_keypoints = self.ann_info['num_joints']
                        logger.info(f"Using custom visualization with {num_keypoints} keypoints")
                        
                        # Debug the incoming results structure
                        logger.info(f"Visualization received {len(results)} results")
                        
                        # Modify the results to avoid index errors
                        for i, result in enumerate(results):
                            logger.info(f"Processing result {i}")
                            
                            # Log keypoints info if available
                            if 'keypoints' in result:
                                kp_len = len(result['keypoints'])
                                logger.info(f"Result {i} has {kp_len} keypoint values (expected {num_keypoints*3})")
                                
                                # Ensure keypoints array doesn't exceed our model's capacity
                                if kp_len > num_keypoints * 3:
                                    # Truncate keypoints to match our model's capacity
                                    result['keypoints'] = result['keypoints'][:num_keypoints * 3]
                                    logger.info(f"Truncated keypoints to {num_keypoints*3} values")
                                elif kp_len < num_keypoints * 3:
                                    # If we have fewer keypoints than expected, pad with zeros
                                    logger.warning(f"Result {i} has fewer keypoints than expected, padding with zeros")
                                    padding = [0.0] * (num_keypoints * 3 - kp_len)
                                    result['keypoints'] = list(result['keypoints']) + padding
                            else:
                                logger.warning(f"Result {i} has no 'keypoints' field, creating empty keypoints array")
                                # Create empty keypoints array with the right size
                                result['keypoints'] = [0.0] * (num_keypoints * 3)
                            
                            # Log skeleton info if available
                            if 'skeleton' in result:
                                logger.info(f"Original skeleton: {result['skeleton']}")
                            
                            # Create a safe skeleton that only uses available keypoints
                            safe_skeleton = []
                            # Only create connections between consecutive points up to our available keypoints
                            for j in range(num_keypoints - 1):
                                safe_skeleton.append([j, j+1])
                            
                            # Replace the skeleton in the result or add it if missing
                            if 'skeleton' in result:
                                result['skeleton'] = safe_skeleton
                                logger.info(f"Set custom skeleton with {len(safe_skeleton)} connections")
                            else:
                                logger.info(f"Adding missing skeleton field with {len(safe_skeleton)} connections")
                                result['skeleton'] = safe_skeleton
                            
                            # Ensure num_joints matches our model
                            if 'num_joints' in result and result['num_joints'] != num_keypoints:
                                logger.info(f"Adjusting num_joints from {result['num_joints']} to {num_keypoints}")
                                result['num_joints'] = num_keypoints
                        
                        # Add additional safety checks before calling original function
                        # Ensure all results have valid score values
                        for i, result in enumerate(results):
                            if 'score' not in result or result['score'] is None:
                                logger.warning(f"Result {i} missing score, adding default value")
                                result['score'] = 0.9  # Default confidence score
                            
                            # Ensure category_id is set properly
                            if 'category_id' not in result:
                                logger.warning(f"Result {i} missing category_id, adding default value")
                                result['category_id'] = 1  # Default category ID
                            
                            # Ensure keypoint_scores are valid if present
                            if 'keypoint_scores' in result:
                                # Check if keypoint_scores length matches our model
                                if len(result['keypoint_scores']) > num_keypoints:
                                    logger.warning(f"Truncating keypoint_scores from {len(result['keypoint_scores'])} to {num_keypoints}")
                                    result['keypoint_scores'] = result['keypoint_scores'][:num_keypoints]
                                elif len(result['keypoint_scores']) < num_keypoints:
                                    # If we have fewer scores than expected, pad with default values
                                    logger.warning(f"Result {i} has fewer keypoint_scores than expected, padding with defaults")
                                    padding = [0.9] * (num_keypoints - len(result['keypoint_scores']))
                                    result['keypoint_scores'] = list(result['keypoint_scores']) + padding
                            else:
                                # Create default keypoint_scores if missing
                                logger.warning(f"Result {i} missing keypoint_scores, adding defaults")
                                result['keypoint_scores'] = [0.9] * num_keypoints
                        
                        logger.info("Calling original draw_pose with modified results")
                        # Call the original function with our modified results
                        return original_draw_pose(image, results, visual_thread)
                    except Exception as e:
                        logger.error(f"Error in custom_draw_pose: {e}")
                        # Provide more detailed error information
                        import traceback
                        logger.error(traceback.format_exc())
                        # Fallback to a simple visualization if the custom one fails
                        return image
                
                # Replace the original function with our custom one
                visualizer.draw_pose = custom_draw_pose
                logger.info("Custom visualization function installed successfully")
            else:
                logger.warning("Could not find draw_pose in visualizer module")
        except ImportError as e:
            logger.warning(f"Could not import visualizer module: {e}")
        except Exception as e:
            logger.error(f"Error setting up custom visualization: {e}")
