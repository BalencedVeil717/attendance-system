# take_picture.py
import cv2

def take_qr(save_path="qr.jpg"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("❌ Cannot access webcam")

    print("📸 Press SPACE to capture qr, ESC to exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.imshow("Take QR", frame)
        key = cv2.waitKey(1)

        if key == 27:  # ESC key → exit
            break
        elif key == 32:  # SPACE key → capture and save
            cv2.imwrite(save_path, frame)
            print(f"✅ QR captured successfully")
            break

    cap.release()
    cv2.destroyAllWindows()

# if __name__ == "__main__":
#     take_qr()
