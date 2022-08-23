import os, sys
import cv2


faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# used for number inputs
def enterNumber(text, range):
    while True:
        numEntered = input("{}".format(text))
        try:
            numEntered = int(numEntered)
            if 0 < numEntered <= range:
              #changes back to int as menu deals with choices only
                return numEntered
            else:
                print("That number is out of range, try again")
        except ValueError:
            print("That isn't a valid option, try again")
# prints the options

def optionsText(txt):
    #cyan coloured text
    print("\u001b[36m{}\u001b[0m\n".format(txt))
        
# changes the AI in use
def aiChanger():
    print("\nWould you like to use my generated AI (lower quality) or a prebuilt Haar Cascade AI?")
    optionsText("\n1 - Generated AI \n2 - Prebuilt AI\n3 - Quit Program")
    choice = enterNumber("\nEnter your choice here: ", 3)
    if choice == 1:
        return True
    elif choice == 2:
        return False
    elif choice == 3:
        return 3

# chooses the method to obtain img data
def imgFormatOptions():
    print("\nWould you like to detect a smile from a photo, or webcam?")
    optionsText("\n1 - Upload a photo \n2 - Use webcam")
    choice = enterNumber("Enter your choice here: ", 2)
    if choice == 1:
        #os.system("cls")
        return True
    elif choice == 2:
        #os.system("cls")
        return False

#ends the prog ram
def endProgram():
    print("This program will now close.\nThank you for using my smile recognition system.")
    cv2.destroyAllWindows()
    quit()
    
# main loop
while True:
    #os.system("cls")
    print("\nWelcome to my AI smile recognition program. You will be presented with several options throughout the use of this program.\nUse numbers to make your choices.")
    print("Use bright lighting for best results.")
    AIChoice = aiChanger()
    #ends the program
    if AIChoice == 3:
        endProgram()
    if AIChoice == True:
        
        print("If error occurs, change to exact file path. If using windows, use double backslashes.")
        #must use full filepath
        smileDetect = cv2.CascadeClassifier(cv2.data.haarcascades +  "generated_haarcascade_grey_smile.xml")
        print("For best results use in a bright environment with face(s) pointed directly forwards, and chin tilted slightly downwards.")
    else:
        smileDetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
    imgChoice = imgFormatOptions()
    if imgChoice == True:
        print("A blue sqaure will appear around any smiling faces.")
        print("Click ESCAPE to close the image")
        try:
            path = input("Enter the COMPLETE image path here (ex. C:/User/docs/images/myImgage.jpg): ")
            img = cv2.imread(path)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except:
            print("\nThat is not a valid path, \ntry again\n")
            continue
        if AIChoice == True:
            smiles = smileDetect.detectMultiScale(imgGray,1.02,4)
        else:
            smiles = smileDetect.detectMultiScale(imgGray,1.7,20)

        for (x,y,w,h) in smiles:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(200,50,0),2)

        cv2.imshow('img',img)
        
        while True:
            key=cv2.waitKey(1)
            if key%256 == 27 or cv2.getWindowProperty('img',cv2.WND_PROP_VISIBLE) == 0:
                print("Returning to main menu...\n")
                cv2.destroyAllWindows()  
                break
    # webcam use
    elif imgChoice == False:
        print("To exit the webcam capture mode click ESC")
        webcam = cv2.VideoCapture(0)
        # while webcam open
        while True:
            #updates the display
            key=cv2.waitKey(1)
            # 27 stands for escape key https://stackoverflow.com/questions/62072021/opencv-video-capture-using-keyboard-to-start-stop
            if key%256 == 27:
                print("\nReturning to main menu...")
                webcam.release()
                cv2.destroyAllWindows()  
                break
            # reads current frame (success is a bool to see if the webcam finds anything)
            successFrameRead, frame = webcam.read()
            # breaks if theres an error reading
            if not successFrameRead:
                break
            #grayscales the image
            frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detect face (returns array of points) multiscale means detecting all despite size (rectangular array)
            faces = faceDetect.detectMultiScale(frameGray)
            # runs smile detection within the faces and places rectangle 
            for (x,y,w,h) in faces:
                # draws rectangle around face
                cv2.rectangle(frame, (x,y),(x+w,y+h),(100,200,50),4)

                # sets the smile detector to only detect within faces
                theFace= frame[y:y+h, x:x+w]
                imgGray = cv2.cvtColor(theFace, cv2.COLOR_BGR2GRAY)

                # detects smiles, 
                if AIChoice == True:
                    #settings to make criteria for a smile more specified (1.02 works well, but )
                    smiles = smileDetect.detectMultiScale(imgGray,1.02,4)
                else:
                    smiles = smileDetect.detectMultiScale(imgGray,1.7,20)
                # prints smile txt
                if len(smiles) > 0:
                    cv2.putText(frame, "Smile", (x, y+h+50), fontScale = 3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(50,50,200))
            # shows frame
            cv2.imshow('webcamWindow', frame)


#if program ends prematurely, this ensures everything is closed
cv2.destroyAllWindows()