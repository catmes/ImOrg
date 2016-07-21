ImOrg stands for Image Organizer and is intended to intelligently organize images.

I have come across several times when I have a directory of images that have no rhyme or reason to the way that
they are organized. ImOrg is intended to solve the laborious and messy problem of organization by providing an
intelligent method of sorting a particular directory of unorganized images into a system of user-selected organization.
Criteria for user-selected organization would include items such as image name, date, model of camera, and
shutter speed.

Key Classes:
    SngIm - sets ups basic image functionality for use with PIL library
    ExifRead - subclass of SngIm that retrieves basic EXIF data from image

Key Functions:
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

HOWTO:
    1. Locate the folder of images that you wish to use.
    2. Place selected folder in main.py dir, this is where the EXIF Data is read.
    3. Open command line and enter the following command "python main.py myfolder".
    4. After you have entered in the command, you should recieve text output of the EXIF Data for your images via the command line.

Dependencies:
    Python 2.7.2
    Pillow 3.2.0



