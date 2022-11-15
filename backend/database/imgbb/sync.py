import imgbbpy
import wget
import cv2

import os
import time

from all_env import IMGBB_API_KEY
client = imgbbpy.SyncClient(IMGBB_API_KEY)

def save_image(url):
	image = wget.download(url)
	return image

def delete_image(image):
	time.sleep(2)
	os.remove(image)
	
def upload_imgbb_image(image):
	img = client.upload(file=image)
	return img.url

def imgbb_image(url:str):
	image = save_image(url)
	link = upload_imgbb_image(image)
	delete_image(image)

	return link

def crop_image(url):
	image = save_image(url)
	img = cv2.imread(image)

	# resize image
	resized_img = cv2.resize(img,(382, 200), interpolation = cv2.INTER_AREA)
	# Cropping an image
	cropped_image = resized_img[0:200,91:291]

	# Save the cropped image
	cv2.imwrite("cropped-"+str(image), cropped_image)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

	delete_image(image)

	return "cropped-"+str(image)