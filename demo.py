
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
print("     3. Flip Picture")
print("     4. Get Stats")
print("     0. Quit")
while(not done):
    try:
        option = int(input())
    except:
        print("Invalid value")
        break
    if(option == 0):
        done = True
        print("QUIT")
        break
    elif(option == 1):
        print("Input amount of pixels to skip")
        try:
            num = int(input())
        except:
            print("Invalid value")
            break
        print(num)
        photo = pf.skipPixels(photo,num)
        plt.imshow(photo)
    elif(option == 2):
        print("Give input in form 'r1,r2,c1,c2' ")
        val = str(input())
        x = val.split(',')
        print(type(photo))
        photo = pf.cropPictureInRange(photo, int(x[0]), int(x[1]),int(x[2]),int(x[3]))
        print(type(photo))
        plt.imshow(photo)
    elif(option == 3):
        photo = photo[::-1]
        plt.imshow(photo)
    elif(option == 4):
        print(" ")
        print("Sum: " + str(np.sum(photo)))
        print("Average: " + str(np.average(photo)))
        print("Max: " + str(np.max(photo)))
        print("Min: " + str(np.min(photo)))
        print(" ")
    plt.show()
    print("Select an option: ")
    print("     1. Skip Pixels")
    print("     2. Crop Picture")
    print("     3. Flip Picture")
    print("     4. Get Stats")
    print("     0. Quit")

# %%

