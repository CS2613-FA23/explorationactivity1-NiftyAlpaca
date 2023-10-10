import numpy as np
from skimage import io;
import matplotlib.pyplot as plt;

##Using this method excludes data from the picture and prints picture with what is left
##Example: skipPixels(photo,1) takes the data of photo and only displays every second pixel (skipping 1 pixel)
def skipPixels(photo, numToSkip):
    num = numToSkip + 1
    plt.imshow(photo[::num, ::num])
    
##Crops pictures based on given row or column ranges
def cropPictureInRange(photo, startRow, endRow, startCol, endCol):
    plt.imshow(photo[startRow:endRow,startCol:endCol])
    