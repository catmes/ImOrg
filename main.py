import os
from sys import argv
import imghdr
import ExifRead
 
 
# Takes folder and returns clean_images, a list of only photos.
def mk_clean_images(images):
 
    clean_images = []
    # Changes cwd to images dir to loop.
    os.chdir(images)
 
    for image in os.listdir(os.getcwd()):
		try:
			# If image does not have a .image extension, don't add it to the list.
			if imghdr.what(image) == 'jpeg':
				clean_images.append(image)
		except IOError:
			pass

		return clean_images
 
# User input directory.
script, images = argv

 
# Making an unclean_images test dir.
images_dir = os.path.join(images)
clean_images = mk_clean_images(images_dir)
# Cleaning up unclean_images.
clean_images.sort() 
images_with_data = {}
 
# First k,v in dictionary has no key. Needs fixing.
for image in clean_images:
        images_with_data[image] = ExifRead.ExifRead(image).get_stats()
 	
text_file = open("images_with_data.txt", 'w')

for image in images_with_data:
	
    text_file.write(image)
    text_file.write("--->")
    text_file.write(str(images_with_data[image]))
    text_file.write("\n \n")
   

text_file.close()

	