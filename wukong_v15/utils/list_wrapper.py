from PIL import Image
from wukong_v15.utils.image_processing import ImageSaver

class ImageListWrapper(list):
    """
    A custom wrapper for lists that adds image saving functionality.
    This class extends the built-in list type and adds a save method
    to handle saving of image objects contained within the list.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def save(self, path, quality=95, **kwargs):
        """
        Save the first valid image in the list to the specified path.
        
        Args:
            path (str): The file path where the image should be saved
            quality (int): The quality setting for JPEG images (1-100)
            **kwargs: Additional arguments to pass to the save method
        """
        # Use the ImageSaver utility to handle the saving logic
        try:
            ImageSaver.save_image(self, path, quality)
        except Exception as e:
            print(f"ImageListWrapper caught exception: {e}")
            # Fallback: try to save the first item if it's an image
            if len(self) > 0 and hasattr(self[0], 'save'):
                self[0].save(path, quality=quality, **kwargs)
            else:
                print(f"Warning: Could not save image at {path}. Object is not a valid image or list of images.")
                # Re-raise if we can't handle it
                raise

def wrap_image_list(image_list):
    """
    Utility function to wrap a regular list in an ImageListWrapper.
    
    Args:
        image_list (list): The list to wrap
        
    Returns:
        ImageListWrapper: A wrapped list with image saving capabilities
    """
    if isinstance(image_list, list) and not isinstance(image_list, ImageListWrapper):
        return ImageListWrapper(image_list)
    return image_list