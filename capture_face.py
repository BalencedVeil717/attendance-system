# take_picture.py
import cv2
import threading

# Global flag for session timeout
session_expired_flag = False

def set_session_expired():
    global session_expired_flag
    session_expired_flag = True

def take_picture(save_path="captured.jpg"):
    global session_expired_flag
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("❌ Cannot access webcam")

    print("📸 Press SPACE to capture image, ESC to exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.imshow("Take Picture", frame)
        key = cv2.waitKey(1)

        # Check if session expired
        if session_expired_flag:
            print("\n⏰ Session expired! Closing camera...")
            break

        if key == 27:  # ESC key → exit
            break
        elif key == 32:  # SPACE key → capture and save
            cv2.imwrite(save_path, frame)
            print(f"✅ Picture captured successfully")
            break

    cap.release()
    cv2.destroyAllWindows()
