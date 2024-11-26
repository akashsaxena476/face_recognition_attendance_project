import cv2
import dlib
import os
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

def capture_faces(person_id, name):
    directory = f'dataset/{person_id}_{name}'
    if not os.path.exists(directory):
        os.makedirs(directory)

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            shape = predictor(gray, face)
            face_descriptor = face_rec_model.compute_face_descriptor(frame, shape)
            np.save(f'{directory}/{person_id}_{name}_{count}.npy', face_descriptor)
            count += 1

            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)

        cv2.imshow('Capturing Faces', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 4:  # Capture only 4 photos
            break

    cap.release()
    cv2.destroyAllWindows()

# Example call
capture_faces(24, 'Akash')  # Replace '24' and 'Akash' with the actual ID and name
