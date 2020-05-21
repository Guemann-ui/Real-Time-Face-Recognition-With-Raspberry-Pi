# Real-Time-Face-Recognition-With-Raspberry-Pi
In this project, we will learn how we can build our face Recognition using the open CV library on RaspberryPi. The tutorial involved two parts; first part is a Trainer program, which analyzed a set of photos of a particular person and create dataset, the second part is the Recognizer program, which detects a face and recognize the face and mention the person name.
Firstable, we need to install some libraries:
Installing the Required Packages
1.	Install PIP:
PIP for Python2 – sudo apt-get install python-pip
PIP for Python3 – sudo apt-get install python3-pip
2.	Update Packages:
sudo apt-get update
sudo apt-get upgrade
3.	Install python3 in RaspberryPi
apt-get install python3
4.	Install OpenCV in RPI for python3
sudo apt-get install libqtgui
sudo apt-get install libqt4-test
sudo pip3 install opencv-python
5.	Use Camera in RPI:
Sudo apt-get install fswebcam
6.	Install dlib (Dlib is a toolkit for real world Machine Learning and data analysis applications)
Pip install dlib
7.	Install pillow ( is a imaging library used to open, manipulate and save images in different format)
pip install pillow
8.	Install  face_recognition Library ( using to train and recognize faces)
pip install face_recognition –no –cache-dir




