import cv2 #For Image processing 
import numpy as np #convert Images to Numerical array 
import os #To handle directories and provides functions for interacting with the operating system
from PIL import Image #Pillow lib for handling images 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Cascade classifier class for object detection / XML pre-trained classifiers for face
recognizer = cv2.createLBPHFaceRecognizer()

Face_ID = -1 
pev_person_name = ""
y_ID = []
x_train = []

Face_Images = os.path.join(os.getcwd(), "Face Images") #path of your "Face Image" Directory
print (Face Images)

for root, dirs, files in os.walk(Face_Images): #go to the face image directory 
	for file in files: #check every directory in it 
		if file.endswith("jpeg") or file.endswith("jpg") or file.endswith("png"): #for image files ending with jpeg,jpg or png 
			path = os.path.join(root, file)
			person_name = os.path.basename(root)
			print(path, person_name)

			
			if pev_person_name!=person_name: #Check if the name of person has changed 
				Face_ID=Face_ID+1 #If yes increment the ID count 
				pev_person_name = person_name

			
			Gery_Image = Image.open(path).convert("L") # convert the image to greysclae using Pillow
			Crop_Image = Gery_Image.resize( (550,550) , Image.ANTIALIAS) #resize the Grey Image to 550*550 (Make sure your face is in the center in all image)
			Final_Image = np.array(Crop_Image, "uint8")
			#print(Numpy_Image)
			faces = face_cascade.detectMultiScale(Final_Image, scaleFactor=1.5, minNeighbors=5) #used to find the faces ; 
			#the scaleFactor parameter used to specify how much the image size is redused at each image scale
			#minNeighbors parameter used to specify how many neighbors each candidate rectangle should have to retain it.
			print (Face_ID,faces)

			for (x,y,w,h) in faces:
				roi = Final_Image[y:y+h, x:x+w] #crop the Region of Interest (ROI), it allows you to select a rectangle from the upper left corner to the lower right point.		
				x_train.append(roi)
				y_ID.append(Face_ID)

recognizer.train(x_train, np.array(y_ID)) #Create a Matrix of Training data 
recognizer.save("face-trainner.yml") #Save the matrix as YML file 
