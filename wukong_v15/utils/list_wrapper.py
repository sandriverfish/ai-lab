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
        No-op save method that skips actual file saving.
        
        Args:
            path (str): The file path where the image would have been saved (ignored)
            quality (int): The quality setting for JPEG images (ignored)
            **kwargs: Additional arguments (ignored)
        """
        print(f"[DEBUG] Image saving disabled - would have saved to: {path}")
        return

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