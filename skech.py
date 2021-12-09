import numpy as np
import imageio
import scipy.ndimage
import cv2

# commit
img = "sk.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989, 0.5870, 0.1140])
def dodge(front, back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back == 255]=255

    return final_sketch.astype("uint8")


ss = imageio.imread(img)   # to read as a given image
gray = rgb2gray(ss)         # 1st we will image convet black and white that means gray scale

i = 255-gray             #0,0,0 is for darkest colour and 255,255,255 is brightest color witch is white color
blur =  scipy.ndimage.filters.gaussian_filter(i,sigma=15)  #convet into blur and sigma is the intensiy of blurness imf\g
r = dodge(blur,gray)

cv2.imwrite('sk-sketch.png',r)

 
