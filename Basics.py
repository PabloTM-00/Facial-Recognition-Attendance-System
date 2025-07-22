import cv2
import numpy as np
import face_recognition

# Load and convert the known image (Elon Test) to RGB
imgElon = face_recognition.load_image_file('ImagesBasic/Elon Test.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

# Load and convert the image to be tested against (Elon Musk) to RGB
imgTest = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# Detect the face and generate the encoding for the known image
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0), 2)  # Draw rectangle on face

# Detect the face and generate the encoding for the test image
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 255, 0), 2)

# Compare the two encodings to see if they match
results = face_recognition.compare_faces([encodeElon], encodeTest)  # Returns [True] or [False]
faceDis = face_recognition.face_distance([encodeElon], encodeTest)  # Returns a distance value (lower = better match)

print(results, faceDis)

# Display the result and confidence on the test image
cv2.putText(imgTest, f'{results}{round(faceDis[0], 2)}', (50, 50), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

# Show both images
cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)
