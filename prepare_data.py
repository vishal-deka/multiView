import cv2
import os
import numpy as np

DEGREE_OF_ROTATION = 20
NUM_IMAGES = 16
path =  "png4/"

l = os.listdir(path)
os.system('mkdir train')
os.system('mkdir test')

c=0
name=0
for j in l:
  image=0
  for i in range(1, NUM_IMAGES+1):
    image = image + DEGREE_OF_ROTATION
    folder = str(j)
    im_path = path + j +'/'+str(folder)+'_r'+str(image)+'.png'
	
	
    if i%2==0:
      img = cv2.imread(im_path)
      output = np.hstack((temp_im, img))
      if c>6000:
        cv2.imwrite('test/'+str(name)+'.png', output)
      else:
        cv2.imwrite('train/'+str(name)+'.png', output)
      name+=1
    else:
      temp_im = cv2.imread(im_path)
      c+=1