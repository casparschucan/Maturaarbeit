import tensorflow as tf 
import numpy as np 
from scipy import misc
import cv2
import matplotlib.pyplot as plt 

i = misc.ascent()
plt.grid(False)
plt.gray()
plt.axis('off')
plt.imshow(i)
plt.show()
i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]

filter = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
weight = 1

for x in range(1,size_x-1):
  for y in range(1,size_y-1):
      output_pixel = 0.0
      output_pixel = output_pixel + (i[x - 1, y-1] * filter[0][0])
      output_pixel = output_pixel + (i[x, y-1] * filter[0][1])
      output_pixel = output_pixel + (i[x + 1, y-1] * filter[0][2])
      output_pixel = output_pixel + (i[x-1, y] * filter[1][0])
      output_pixel = output_pixel + (i[x, y] * filter[1][1])
      output_pixel = output_pixel + (i[x+1, y] * filter[1][2])
      output_pixel = output_pixel + (i[x-1, y+1] * filter[2][0])
      output_pixel = output_pixel + (i[x, y+1] * filter[2][1])
      output_pixel = output_pixel + (i[x+1, y+1] * filter[2][2])
      output_pixel = output_pixel * weight
      if(output_pixel<0):
        output_pixel=0
      if(output_pixel>255):
        output_pixel=255
      i_transformed[x, y] = output_pixel

plt.imshow(i_transformed)
plt.show()

new_x = int(size_x/2)
new_y = int(size_y/2)
newImage = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
  for y in range(0, size_y, 2):
    pixels = []
    pixels.append(i_transformed[x, y])
    pixels.append(i_transformed[x + 1, y])
    pixels.append(i_transformed[x, y + 1])
    pixels.append(i_transformed[x + 1, y + 1])
    pixels.sort(reverse=True)
    newImage[int(x / 2), int(y / 2)] = pixels[0]

plt.imshow(newImage)
plt.show()

new_new_x = int(new_x/2)
new_new_y = int(new_y/2)
newnewImage = np.zeros((new_new_x, new_new_y))
for x in range(0, size_x, 4):
  for y in range(0, size_y, 4):
    pixels = []
    pixels.append(i_transformed[x, y])
    pixels.append(i_transformed[x + 1, y])
    pixels.append(i_transformed[x, y + 1])
    pixels.append(i_transformed[x + 1, y + 1])
    pixels.sort(reverse=True)
    newnewImage[int(x / 4), int(y / 4)] = pixels[0]

plt.imshow(newnewImage)
plt.show()




