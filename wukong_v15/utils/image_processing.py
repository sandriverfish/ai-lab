from PIL import Image

class ImageSaver:
    @staticmethod
    def save_image(image, path, quality=95):
        if isinstance(image, list):
            if len(image) > 0 and isinstance(image[0], Image.Image):
                image[0].save(path, quality=quality)
            else:
                raise TypeError("List contains no valid images")
        elif isinstance(image, Image.Image):
            image.save(path, quality=quality)
        else:
            raise TypeError("Provided object is not an image or list of images")