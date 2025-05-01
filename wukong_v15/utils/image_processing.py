from PIL import Image

class ImageSaver:
    @staticmethod
    def save_image(image, path, quality=95):
        if isinstance(image, Image.Image):
            image.save(path, quality=quality)
        else:
            raise TypeError("Provided object is not an image")