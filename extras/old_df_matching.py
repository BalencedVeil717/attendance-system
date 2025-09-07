from deepface import DeepFace
import os

# Path to the query image
query_image_path = "student.png"

# Path to the dataset folder
dataset_path = "data"

# List image files in dataset
image_files = [
    f for f in os.listdir(dataset_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

print("Comparing query image with each image in dataset...")

found_match = False

for img in image_files:
    img_path = os.path.join(dataset_path, img)
    try:
        result = DeepFace.verify(
            img1_path=query_image_path, img2_path=img_path, enforce_detection=False
        )


        if result["verified"]:
            print(f"✅ Match found with {img}!")
            found_match = True


    except Exception as e:
        print(f"⚠ Could not process {img}: {e}")

# Final output
if not found_match:
    print("\nNo confident match found in the dataset.")
else:
    print("\nMatching process completed.")
