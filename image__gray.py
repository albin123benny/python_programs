# -*- coding: utf-8 -*-
"""image _gray

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18kDIz8tUhG_8Eaota1ExGJYlaLPlswjW
"""

from google.colab import files
from IPython.display import Image
from google.colab.patches import cv2_imshow
import cv2 
import numpy as np 
import matplotlib.pyplot as plt

image = cv2.imread("/content/beker.jpg", 1)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
Titles =["Original",  "gray"] 
images =[image,gray_image] 
count = 2
  
for i in range(count): 
    plt.subplot(2, 2, i + 1) 
    plt.title(Titles[i]) 
    plt.imshow(images[i]) 
  
plt.show()