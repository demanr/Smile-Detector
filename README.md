# Smile-Detector
This Python program uses cv2 to detect smiles from images and webcam.

It converts face data into greyscale for improved classification, and was made with reference to a Youtube livestream by Clever Programmer, which can be found here https://www.youtube.com/watch?v=uLY5JSE5WAU.

# Dataset and Haar Cascades

The generated_haarcascade_grey_smile dataset was created using images from the [GENKI4K dataset](https://inc.ucsd.edu/mplab/398/), which were then converted to greyscale for improved performance.
This dataset was generated using Cascade Trainer GUI.

The haarcascade_frontalface_default and haarcascade_smile xml files are two of the OpenCV Haar Cascades, which can be found on the [OpenCV Github](https://github.com/opencv/opencv) under data.

# Program Use

If the generated AI is having a hard time reading the face, ensure the face is in a bright area, and no parts are blocked from view. 

To display the detected image(s) the program will open a tab. To close these tabs, press ESCAPE and alternatively for photo analysis click the X.

# Image

Example image by <a href="https://unsplash.com/@leahhetteberg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">leah hetteberg</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>.
  
