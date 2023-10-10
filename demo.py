
#%%
import numpy as np
from skimage import io;
import matplotlib.pyplot as plt;
import picfunc as pf

photo = io.imread('Lion.jpg')
done = False

plt.imshow(photo)
plt.show()
print("Select an option: ")
print("     1. Skip Pixels")
print("     2. Crop Picture")
print("     0. Quit")
while(not done):
    option = int(input())
    if(option == 0):
        done = True
        break
    elif(option == 1):
        print("Input amount of pixels to skip")
        num = int(input())
        print(num)
        pf.skipPixels(photo,num)
    elif(option == 2):
        print("Give input in form 'r1,r2,c1,c2")
        val = str(input())
        x = val.split(',')
        pf.cropPictureInRange(photo, int(x[0]), int(x[1]),int(x[2]),int(x[3]))
    plt.show()
    print("Select an option: ")
    print("     1. Skip Pixels")
    print("     2. Crop Picture")
    print("     0. Quit")

# %%

