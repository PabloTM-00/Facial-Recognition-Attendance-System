import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])  # Remove file extension to get the person's name
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image from BGR (OpenCV) to RGB (face_recognition)
        encode = face_recognition.face_encodings(img)[0]  # Get the facial encoding (assumes one face per image)
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')  # Split each line into name and time
            nameList.append(entry[0])
        if name not in nameList:  # Register attendance only once per person
            now = datetime.now()
            dateString = now.strftime("%H:%M:%S")
            f.writelines(f'\n{name},{dateString}')

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Resize to 1/4 for faster processing
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(imgSmall)  # Detect face locations in the frame
    encodeCurrentFrame = face_recognition.face_encodings(imgSmall, facesCurrentFrame)  # Get encodings for all detected faces

    for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)  # Compare with known encodings
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)  # Calculate distance to each known face
        matchIndex = np.argmin(faceDis)  # Get the closest match (smallest distance)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4  # Scale back up to original size
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw rectangle around the face
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)  # Draw filled label background
            cv2.putText(img, name, (x1 + 6 , y2 - 6), cv2.FONT_ITALIC, 1 ,(255,255,255), 2)  # Write name on label
            markAttendance(name)  # Log attendance

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
