[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# Exploration Activity 1: Colton Coughlin

## Which package/library does the sample program demonstrate?

This program demonstrates the use of NumPy, a math module in Python.

## How does somebody run your program?

To run my program, a few steps must be completed. First off, the program must be ran in visual studio code because we need the help of some extensions.

1) When using visual studio code, you will need the Python (Microsoft) extension and the Python Extension Pack (Don Kayamanne). After downloading the extension pack, you will be asked if you want to install Jupyter. Make sure to agree to install Jupyter, it is what allows you to see the pictures of the progam.

2) You may need to download the required packages to run this program. Here is a list of commands to install them through pip:

    1. pip install numpy

    2. python -m pip install -U scikit-image
    
    3. python -m pip install -U matplotlib

3) Usually when running a program in Visual Studio Code, you can use the play button or terminal commands to run a program. In this program, you will notice there are '#%%' lines in the code. These turn the program into cells where you can run different areas of code seperately.

     Although I don't do that in my program, you MUST press 'run cell' above the code to be able to see the picture you are working with in the program. A window should pop up on the right called 'Interactive'.

     Warning: When running the code, the input box may come up before the prompt. If that happens and you don't know what you are inputting for. Ensure that the interactive window is scrolled to the bottom and re-run code with 'run cell'.

## What purpose does your program serve?

The purpose of this program is to import a jpg photo, modify it, and export it as a new jpg photo. The program allows you to modify the photo in multiple ways and you can also print statistics of your photo at any time.

## What would be some sample input output?

The program consists of three parts:

1. Choose what picture you would like to work with.
2. Modify the picture through a text loop.
3. Name and save new picture.

Here is a quick demo of the app using pictures:

Step 1: User is prompted to choose an image from the local directory. After the selection is made, the program prints the image.

![image](READMEIMAGES/Step1.JPG)

Step 2: User is promted to choose a way to modify the picture with an additional option to print the statistics of the image's pixel data. The user decided to crop the image with the input (0,1250,500,1250) which takes rows 0-1250 of the image and columns 500-1250 of the image to create a new image.

![image](READMEIMAGES/Step2.JPG)

Step 3: User is finished modifying the picture and presses 0 to finish up the photo editing process. The user is prompted for a file name so that the image may be stored. When finished, the image will be stored in the local directory.

![image](READMEIMAGES/Step3.JPG)
