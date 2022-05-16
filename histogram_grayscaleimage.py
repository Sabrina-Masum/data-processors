# -*- coding: utf-8 -*-
"""histogram_grayscaleimage.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P1w5LubxjGtv9C2I2zBH7uE1OJ9PXJ0M
"""

# Commented out IPython magic to ensure Python compatibility.
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

import cv2
from google.colab.patches import cv2_imshow

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %clear
A= cv2.imread('/content/drive/My Drive/content/col.jpg')
cv2_imshow(A)
gray = cv2.cvtColor(A,cv2.COLOR_BGR2GRAY)
(n,m) = (gray.shape)

cv2_imshow(gray)

print (gray)

k=0 
H= np.zeros((256), dtype=int)  #zero mat 
print(H) 
while k < 256:
  H[k] =np.count_nonzero(gray==k)
  k=k+1 

Intensity=np.arange(0, 256, 1)
print (Intensity)
print(H) #eta count
plt.bar(Intensity, H , color='blue' , width = 0.8)
plt.xlabel('Intensity')
plt.ylabel('freq')
plt.title('Histo')
plt.show()