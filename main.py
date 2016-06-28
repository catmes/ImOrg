# main.py

"""ImOrg stands for Image Organizer and is intended to intelligently organize images.

I have come across several times when I have a directory of images that have no rhyme or reason to the way that
they are organized. ImOrg is intended to solve the laborious and messy problem of organization by providing an
intelligent method of sorting a particular directory of unorganized images into a system of user-selected organization.
Criteria for user-selected organization would include items such as image name, date, model of camera, and
shutter speed.

Classes:
    SngIm - sets ups basic image functionality for use with PIL library
    ExifRead - subclass of SngIm that retrieves basic exif data from image

Functions:
    mk_clean_images - a function that assures that only usable images will be picked out a chosen directory

Known problems:
    PIL library only is able to analyze jpeg images and thus ImOrg
    ImOrg only able to organize a single folder of images at a time

Current features:
    ImOrg can write EXIF data from selected folder of images to .txt file

Planned features:
    intelligent image organizational system based on criteria of user
    functional GUI

 """

from sys import argv
import os
import imghdr
import ExifRead


image_values = ['rgb', 'gif', 'pbm', 'ppm', 'tiff', 'rast', 'xbm'
                'jpeg', 'bmp', 'png']


def mk_clean_images(user_images):
    """ A function that sorts non images and non jpegs.

    Predicting that the given directory won't always be consisting of photos and only jpegs, mk_clean_images filters
    out everything that is not a jpeg. After the filtering, a list of clean_images is left - images that won't make the
    program crash.

    Args:
        user_images - chosen user image dir

    Returns:
        Filters through user_images
    """
    clean_images = []
    # Changes cwd to images dir to loop.
    os.chdir(user_images)
 
    for lone_image in os.listdir(os.getcwd()):
        try:
            # If image does not have a .image extension, don't add it to the list.
            if imghdr.what(lone_image) == 'jpeg':
                clean_images.append(lone_image)

            elif imghdr.what(lone_image) is not "jpeg":
                if imghdr.what(lone_image) in image_values:
                    print "%s: not a jpeg." % lone_image

        except IOError:
            print "%s: not an image." % lone_image
            continue





 
    return clean_images
 
 
# User input directory.
script, images = argv
 
# Making a unclean_images test dir.
images_dir = os.path.join(images)
clean_images = mk_clean_images(images_dir)
# Cleaning up unclean_images.
clean_images.sort() 
images_with_data = {}

for image in clean_images:
        images_with_data[image] = ExifRead.ExifRead(image).get_stats()

text_file = open("images_with_data.txt", 'w')

for image in images_with_data:

    text_file.write(image)
    text_file.write("--->")
    text_file.write(str(images_with_data[image]))
    text_file.write("\n \n")
   

text_file.close()

