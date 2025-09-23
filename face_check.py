import warnings
warnings.filterwarnings("ignore")
from deepface import DeepFace
import os


def check_face(query_image_path, dataset_path="data", enforce_detection=False):
    """
    Returns the name of the matching student if found, else None
    """
    image_files = [
        os.path.join(dataset_path, student, f)
        for student in os.listdir(dataset_path)
        if os.path.isdir(os.path.join(dataset_path, student))
        for f in os.listdir(os.path.join(dataset_path, student))
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    for img_path in image_files:
        try:
            result = DeepFace.verify(
                img1_path=query_image_path,
                img2_path=img_path,
                enforce_detection=enforce_detection,
            )
            if result["verified"]:
                return os.path.basename(os.path.dirname(img_path))
        except Exception as e:
            print(f"⚠ Could not process {img_path}: {e}")
    return None



# if __name__ == "__main__":
#     match = check_face("student_faces/student1.png")
#     if match:
#         print("✅ Match found:", match)
#     else:
#         print("❌ No match found")
