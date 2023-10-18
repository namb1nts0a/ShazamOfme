import face_recognition
import os
import cv2
import numpy as np

path = "assets/faces"
images = []
classNames = []
myList = os.listdir(path)

for i in myList:
    curImg = cv2.imread(f"{path}/{i}")
    images.append(curImg)
    classNames.append(os.path.splitext(i)[0])


def findEncodings(images):
    encodList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodList.append(encode)

    return encodList

encodeListKnown = findEncodings(images)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        print(faceDis)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255),2)

    cv2.imshow("frame", img)
    cv2.waitKey(1)

    
###############################

# import face_recognition
# import os, sys
# import cv2
# import numpy as np
# import math
# import threading
# import time


# def face_confidence(face_distance, face_match_threshold=0.6):
#     range = (1.0 - face_match_threshold)
#     linear_val = (1.0 - face_distance) / (range * 2.0)

#     if face_distance > face_match_threshold:
#         return str(round(linear_val * 100, 2)) + "%"
#     else:
#         value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
#         return str(round(value, 2)) + "%"

# def create_thread(target):
#     thread = threading.Thread(target=target)
#     thread.start()
#     thread.join()


# class FaceRecognition:

#     face_locations = []
#     face_encodings = []
#     face_names = []
#     known_face_encodings = []
#     known_face_names = []
#     process_current_frame = True

#     def __init__(self):
#         self.encode_faces()

#     def encode_faces(self):
#         for image in os.listdir('assets/faces'):
#             face_images = face_recognition.load_image_file(f"assets/faces/{image}")
#             face_encoding = face_recognition.face_encodings(face_images)[0]

#             self.known_face_encodings.append(face_encoding)
#             self.known_face_names.append(image)

#         print(self.known_face_names)

#     def run_recognition(self):
#         video_capture = cv2.VideoCapture(0)

#         if not video_capture.isOpened():
#             sys.exit("video source not found...")

#         def face_recognition_thread():    

#             while True:
#                 ret, frame = video_capture.read()
#                 time.sleep(0.001)
#                 if self.process_current_frame:
#                     small_frame = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
#                     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#                     self.face_locations = face_recognition.face_locations(rgb_small_frame)
#                     self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

#                     self.face_names = []
#                     for face_encoding in self.face_encodings:
#                         matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#                         name = "Unknown"
#                         confidence = "Unknown"

#                         face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
#                         best_math_index = np.argmin(face_distances)

#                         if matches[best_math_index]:
#                             name = self.known_face_names[best_math_index]
#                             confidence = face_confidence(face_distances[best_math_index])

#                         self.face_names.append(f"{name} ({confidence})")

#                 self.process_current_frame = not self.process_current_frame

#                 for encodeFace, faceLoc in zip(self.face_encodings, self.face_locations):
#                     y1, x2, y2, x1 = faceLoc
#                     y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    

#                     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
#                     cv2.rectangle(frame, (x1, y2 - 30), (x2, y2), (0, 0, 255), -1)
#                     cv2.putText(frame, name, (x1 + 6, y2 -6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

#                 cv2.imshow("face recognition", frame)

#                 if cv2.waitKey(1) == ord("q"):
#                     break

#             video_capture.release()
#             cv2.destroyAllWindows()
        
#         # recognition_thread = threading.Thread(target=face_recognition_thread)
#         # recognition_thread.start()
#         create_thread(face_recognition_thread)


# if __name__ == "__main__":
#     fr = FaceRecognition()
#     fr.run_recognition()