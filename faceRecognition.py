import face_recognition
import cv2
import numpy as np
import os

class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    tolerance = 0.55
    process_current_frame = True

    def __init__(self):
        # self.frame = frame
        self.encode_faces()

    def encode_faces(self):
        for image in os.listdir('assets/faces'):
            face_images = face_recognition.load_image_file(f"assets/faces/{image}")
            face_encoding = face_recognition.face_encodings(face_image=face_images)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(os.path.splitext(image)[0])
        print(self.known_face_names)

    def run_recognation(self, frame):
        
        if self.process_current_frame:
            small_frame = cv2.resize(frame, (0, 0), None, fx=0.25, fy=0.25)
                
            self.face_locations = face_recognition.face_locations(small_frame)
            self.face_encodings = face_recognition.face_encodings(small_frame, self.face_locations)

            self.face_names = []
            for face_encoding in self.face_encodings:
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=self.tolerance)
                self.name = "Unknown"

                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    self.name = self.known_face_names[best_match_index]
                    print(self.name)

                self.face_names.append(f"{self.name}")

        self.process_current_frame = not self.process_current_frame

        for encodeFace, faceLoc in zip(self.face_encodings, self.face_locations):
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4 

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 30), (x2, y2), (0, 255, 0), -1)
            cv2.putText(frame, self.name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255),1)
