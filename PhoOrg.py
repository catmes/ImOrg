from PIL import Image, ExifTags
 
# A basic class that takes an image file path and sets up basic
# functionality for a single image. Class uses PIL for image
# processing.
class SngIm(object):
 
    def __init__(self, image_path):
        self.image_path = image_path
 
    # open() identifies image and readies image data for processing.
    def open(self):
        im = Image.open(self.image_path)
        return im
 
    # Gets basic exif data from image, returns data in dictionary
    # e.g. 'shutter speed': 1/200
    def get_exif(self):
 
        exif = {
            ExifTags.TAGS[k]: v
            for k, v in self.open()._getexif().items()
            if k in ExifTags.TAGS
                }
 
        return exif

# SortImages takes provided, unsorted image directory and creates a series of directories containing
# images. New images are sorted into directories based upon a chosen attribute e.g. date, size, ISO.
class SortImages(object):

    def __init__(self):

    def sort_date(self):
