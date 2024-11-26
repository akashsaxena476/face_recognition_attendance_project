import cv2
import dlib
import numpy as np
from datetime import datetime
import pandas as pd
import os
from mark_attendance import mark_attendance

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

known_face_encodings = np.load('face_encodings.npy')
known_face_ids = np.load('face_ids.npy')
known_face_names = np.load('face_names.npy')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)
        face_descriptor = face_rec_model.compute_face_descriptor(frame, shape)
        face_descriptor = np.array(face_descriptor)

        matches = np.linalg.norm(known_face_encodings - face_descriptor, axis=-1)
        min_distance = np.min(matches)
        name = "Unknown"

        if min_distance < 0.6:  # Threshold for recognition
            index = np.argmin(matches)
            person_id = known_face_ids[index]
            name = known_face_names[index]
            mark_attendance(person_id, name)

            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
            cv2.putText(frame, f'{name} (ID: {person_id})', (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.imshow('Face Recognition', frame)
            cv2.waitKey(2000)  # Wait for 2 seconds

            cap.release()
            cv2.destroyAllWindows()
            break
        else:
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 0, 255), 2)
            cv2.putText(frame, 'Unknown', (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            cv2.imshow('Face Recognition', frame)
            cv2.waitKey(2000)  # Wait for 2 seconds

            cap.release()
            cv2.destroyAllWindows()
            break

    if not cap.isOpened():
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
