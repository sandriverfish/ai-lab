from PIL import Image

class ImageSaver:
    @staticmethod
    def save_image(image, path, quality=95):
        if isinstance(image, list):
            # Try to find the first valid PIL Image in the list
            for item in image:
                if isinstance(item, Image.Image):
                    item.save(path, quality=quality)
                    return
                # Handle case where the item might have a 'save' method but isn't a PIL Image
                elif hasattr(item, 'save') and callable(item.save):
                    try:
                        item.save(path, quality=quality)
                        return
                    except Exception:
                        # Continue to next item if this fails
                        pass
            
            # If we get here, we couldn't find a valid image in the list
            raise TypeError("List contains no valid images or objects with a working save method")
        elif isinstance(image, Image.Image):
            image.save(path, quality=quality)
        # Handle case where the object has a 'save' method but isn't a PIL Image
        elif hasattr(image, 'save') and callable(image.save):
            try:
                image.save(path, quality=quality)
            except Exception as e:
                raise TypeError(f"Object has a save method but failed to save: {e}")
        else:
            raise TypeError("Provided object is not an image or list of images")