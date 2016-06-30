# main.py

"""ImOrg stands for Image Organizer and is intended to intelligently organize images.

I have come across several times when I have a directory of images that have no rhyme or reason to the way that
they are organized. ImOrg is intended to solve the laborious and messy problem of organization by providing an
intelligent method of sorting a particular directory of unorganized images into a system of user-selected organization.
Criteria for user-selected organization would include items such as image name, date, model of camera, and
shutter speed.

Classes:
    SngIm - sets ups basic image functionality for use with PIL library
    ExifRead - subclass of SngIm that retrieves basic EXIF data from image

Functions:
    mk_clean_images - a function that assures that only usable images will be picked out a chosen directory
    mk_data - returns a dictionary of useful EXIF information for each image from user_images
    split_data - to be used with mk_data, improves readability

Known problems:
    PIL library only is able to analyze jpeg images and thus ImOrg
    ImOrg only able to organize a single folder of images at a time
    ImOrg cumbersome to use

Current features:
    ImOrg can write EXIF data from selected folder of images to console

Planned features:
    intelligent image organizational system based on criteria of user
    functional GUI

 """

from sys import argv
import os
import imghdr
import ExifRead


# For use in function mk_clean_images.
image_values = ['rgb', 'gif', 'pbm', 'ppm', 'tiff', 'rast', 'xbm'
                'jpeg', 'bmp', 'png']


# Is a bit big for a function, may need some refactoring.
def mk_clean_images(user_images):
    """ A function that sorts non images and non jpegs.

    Predicting that the given directory won't always be consisting of photos and only jpegs,
    mk_clean_images filters out everything that is not a jpeg. After the filtering,
    a list of clean_images is left - images that won't make the program crash.

    Args:
        user_images - chosen user image dir

    Returns:
        clean_images - list of only jpegs
    """
    clean_images = []
    # Changes cwd to images dir to loop.
    os.chdir(user_images)
    # For all images in user_images directory.
    for lone_image in os.listdir(os.getcwd()):
        try:
            # If image has a jpeg extension, add it to clean_images.
            if imghdr.what(lone_image) == 'jpeg':
                clean_images.append(lone_image)

            # If image does not have jpeg extension, do not add to clean_images.
            elif imghdr.what(lone_image) is not "jpeg":
                # Will pass True if the file is actually an image.
                if imghdr.what(lone_image) in image_values:
                    print "%s: not a jpeg. \n" % lone_image

        # To handle those pesky non images.
        except IOError:
            print "%s: not an image. \n" % lone_image
            continue

    return clean_images


def mk_data(cleaned_images):
    """ A function that takes clean_images and returns useful
        EXIF data for each image via dictionary.

    mk_data takes images that have gone through mk_clean_images and provides
    certain EXIF data for each photo in clean_images list via the method get_stats
    from the ExifRead class. The image is paired with its EXIF in the form
    of key-value value pair (image : EXIF data).

    Args:
        cleaned_images - user_images that have gone through function mk_clean_images

    Returns:
        images_with_data: dictionary with image to EXIF data, key-value pairs

    """

    images_with_data = {}
    # Looping through cleaned images, appending lone_image : lone_image.get_stats().
    for lone_image in cleaned_images:
        images_with_data[lone_image] = ExifRead.ExifRead(lone_image).get_stats()

    return images_with_data


def split_data(images_with_data):
    """A simple function that makes mk_data more readable.

    mk_data returns a very large dictionary with yet even more dictionaries
    on the inside of the very large dictionary! So in order to make the return of mk_data
    more readable, split_data simply uses some string formatting to make the return of
    mk_data easier on the eyes as well as being alphabetically ordered.

    Args:
        images_with_data - cleaned_images that have gone through mk_data

    Prints:
        pretty key-value pairs ordered
    """

    for image in sorted(images_with_data.keys(), key=str.lower):
        print "%s %s %s \n" % (image, "--->", images_with_data[image])


# User input directory.
script, user_images = argv
 
# Setting up path.
user_images = os.path.join(user_images)

# Cleaning up and organizing user_images
clean_images = mk_clean_images(user_images)
organized_data = mk_data(clean_images)

# Printing results to console
split_data(organized_data)