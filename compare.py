import cv2
import pickle

# Load trained model + labels
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

with open("labels.pkl", "rb") as f:
    label_map = pickle.load(f)

# Haar cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def recognize_face(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in faces:
        face = img[y : y + h, x : x + w]
        label_id, confidence = recognizer.predict(face)

        # Lower confidence = better match
        if confidence < 70:  # tweak threshold
            student_name = label_map[label_id]
            return f"✅ Recognized as {student_name} (confidence={confidence:.2f})"
        else:
            return "❌ Face not recognized"

    return "⚠️ No face detected"


# Example
print(recognize_face("image.png"))
