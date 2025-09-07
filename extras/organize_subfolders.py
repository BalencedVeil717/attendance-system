# organize_dataset.py
import os
import shutil

dataset_path = "data"

# List all images in dataset folder
image_files = [
    f for f in os.listdir(dataset_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

for img_file in image_files:
    # Derive folder name from image name (before first hyphen)
    folder_name = img_file.split("-")[0]  # e.g., "Barack-Obama..." -> "Barack"
    folder_path = os.path.join(dataset_path, folder_name)

    # Create folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Move image into folder
    src_path = os.path.join(dataset_path, img_file)
    dst_path = os.path.join(folder_path, img_file)
    shutil.move(src_path, dst_path)
    print(f"Moved {img_file} → {folder_name}/")
