"""
Stack images to use as input obs
"""
import os
import cv2
import numpy as np
import re

n_stack = 4

from_record_dir = "record_dncf/"
to_record_dir = "record_dncf_stacked/"

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

image_names = [im for im in os.listdir(from_record_dir) if im.endswith(".jpg")]
image_names.sort(key=natural_keys)
print("{} images".format(len(image_names)))

image_path = from_record_dir + image_names[0]
image = cv2.imread(image_path)
slide_window = np.array(image)
for i in range(1, n_stack):
    image_path = from_record_dir + image_names[i]
    print(image_path)
    image = cv2.imread(image_path)
    slide_window = np.concatenate((slide_window, image))
print(slide_window.shape)
cv2.imwrite(to_record_dir+'0.jpg', slide_window)

for i in range(n_stack, len(image_names) - n_stack + 1):
    image_path = from_record_dir + image_names[i]
    image = cv2.imread(image_path)
    slide_window = np.concatenate((slide_window[image.shape[0]:], image))
    cv2.imwrite(to_record_dir+str(i-n_stack+1)+'.jpg', slide_window)
