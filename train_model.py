import cv2
import os
import numpy as np

dataset_path = "dataset"
model_path = "face_model.yml"

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = []
labels = []
label_map = {}
id_counter = 0

for student_name in os.listdir(dataset_path):
    student_folder = os.path.join(dataset_path, student_name)
    if not os.path.isdir(student_folder):
        continue

    label_map[id_counter] = student_name

    for img_name in os.listdir(student_folder):
        img_path = os.path.join(student_folder, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        faces_detected = face_cascade.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=5
        )
        for x, y, w, h in faces_detected:
            face = img[y : y + h, x : x + w]
            faces.append(face)
            labels.append(id_counter)

    id_counter += 1

# LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save(model_path)

# Saving label map
import pickle

with open("labels.pkl", "wb") as f:
    pickle.dump(label_map, f)

print("✅ Model trained and saved.")
