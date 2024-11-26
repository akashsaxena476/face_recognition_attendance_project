import os
import numpy as np

def train_model():
    data_dir = 'dataset'
    known_face_encodings = []
    known_face_ids = []
    known_face_names = []

    for label in os.listdir(data_dir):
        person_id, name = label.split('_', 1)
        for file in os.listdir(f'{data_dir}/{label}'):
            face_encoding = np.load(f'{data_dir}/{label}/{file}')
            known_face_encodings.append(face_encoding)
            known_face_ids.append(person_id)
            known_face_names.append(name)

    np.save('face_encodings.npy', known_face_encodings)
    np.save('face_ids.npy', known_face_ids)
    np.save('face_names.npy', known_face_names)

train_model()
