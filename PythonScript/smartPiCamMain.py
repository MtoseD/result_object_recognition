#!/usr/bin/python3
############################################################
# File smartPiCamMain.py
# This is the main application file for the smart Pi camera.
# It implements object detection with the Coral USB
# Accelarotor (Edge TPU Coprozessor) using a model
# trained on the COCO dataset.
#
# File: smartPiCamMain.py
# Author: Detlef Heinze 
# Version: 1.1     Date: 22.04.2019       
###########################################################

from tkinter import *
import time 
from PIL import Image, ImageTk
import smartPiCamContr as SPCC_Contr

#Settings
#Size of picture displayed on the screen
imageDisplaySize= (300, 300)

#IDs of objects of interest to be detected
#for this application. 43 = bottle, 52 = apple, 83 = book in COCO-Dataset
objectIdsOfInterest = { 43, 52, 83} 

arrDetectedObjects = []

#Terminate program
def terminate():
    print("Program terminates")
    camera.close()
    appWin.destroy()

#Add a rectangle on canvas with object label
def addRectangles(canvas, label, box):
    canvas.create_rectangle(box[0], box[1],
                            box[2], box[3],
                            width=2, outline='yellow')
    canvas.create_text((box[0],box[1]), text= label,
             fill='yellow', anchor=SW)
    
#Handle window close event   
def on_closing():
    print("\nWindow closed by user")
    terminate()

#Create controller and warm up cam
print('SmartPiCam Application 1.0\n')
spcc= SPCC_Contr.SmartPiCamContr()  #Step 1
camera= spcc.configurePiCam()       #Step 3
count=0 #Count processed images

#Create main application window:    #Step 5
appWin = Tk()
appWin.wm_title("Smart PiCam 1.0")
lblPicTaken= Label(appWin, text="Last picture taken")
canPict = Canvas(appWin, height=imageDisplaySize[1],
                         width= imageDisplaySize[0])
lblPicTaken.pack(anchor=W, pady=5)
canPict.pack(fill=X)
appWin.protocol("WM_DELETE_WINDOW", on_closing)

#Start main loop of application
timeout = time.time() + spcc.appDuration

print('\nApplication starts...\n')
while time.time() < timeout:
    picData= spcc.takePhoto()    #Step 6
    #Display image on screen     #Step 8
    img= Image.frombytes('RGB', (picData.shape[1],picData.shape[0]),
                                 picData.astype('b').tostring())
    actPhoto= ImageTk.PhotoImage(image=img)
    canPict.create_image(0,0,image=actPhoto, anchor=NW)
        
    #Run neural network on Edge TPU Accelarotor
    result= spcc.predict(picData)       #Step 9
    detectedObjects= spcc.analyseResult(result, objectIdsOfInterest) #Step 11
    for obj in detectedObjects:         #Step 13
        addRectangles(canPict, obj[0], obj[1])
    appWin.update()
    spcc.processResult(detectedObjects) #Step 14
    count += 1
    for res in result:
        arrDetectedObjects.append(res.id)
print("\nDuration of running application has been reached.")
print("Number of processed images: ", count)
print("Duration: ", spcc.appDuration, "seconds.")
print(arrDetectedObjects)
terminate()


if 43 in arrDetectedObjects:
	object = "bottle"
	print("it's a bottle")
	bottlePics = (arrDetectedObjects.count(43))
	print(bottlePics, " pictures of the bottle were taken.")
	amountOfPictures = bottlePics
elif 52 in arrDetectedObjects:
	object = "apple"
	print("it's an apple")
	applePics = (arrDetectedObjects.count(52))
	print(applePics, " pictures of the apple were taken.")
	amountOfPictures = applePics
elif 83 in arrDetectedObjects:
	object = "book"
	print("it's a book")
	bookPics = (arrDetectedObjects.count(83))
	print(bookPics, " pictures of the book were taken.")
	amountOfPictures = bookPics
else:
	object = "-Nothing detected-"
	amountOfPictures = 0
	print("Nothing detected")

#noDuplicates = set(arrDetectedObjects)
#print(len(set)" objects were detected.")


import mysql
import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "USER",
        password =  "PASSWORD",
        database = "dbObjectRecognition"
)

mycursor = mydb.cursor()

sql = "INSERT INTO tbObjects_Amount (object, amount, processedImages) VALUES (%s, %s, %s)"
val = (object, amountOfPictures, count)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
