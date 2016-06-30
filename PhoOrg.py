from PIL import Image, ExifTags

class SngIm(object):
    """ A class that provides basic image functionality with PIL library.

    A basic class that takes an image file path and sets up basic
    functionality for a single image. Class uses PIL for image
    processing. Subclasses can use the method open to prepare an image
    for data manipulation and method get_exif for working with EXIF data.

    Attributes:
        image_path - the file path of a single image represented by a string

    Important Methods:
        open - readies an image for data manipulation
        get_exif - returns basic EXIF data from image
    """
 
    def __init__(self, image_path):
        self.image_path = image_path

    def open(self):
        """ open identifies image and readies image data for processing. """
        im = Image.open(self.image_path)
        return im
 

    def get_exif(self):
        """  Gets basic EXIF data from image, returns data in dictionary
            e.g. 'shutter speed': 1/200. """
        exif = {
            ExifTags.TAGS[k]: v
            for k, v in self.open()._getexif().items()
            if k in ExifTags.TAGS
                }
 
        return exif

