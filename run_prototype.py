import os
import threading

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings("ignore")

from qr_scan import scan_qr
from face_check import check_face
from attendance import mark_attendance
from capture_face import take_picture, set_session_expired
from capture_qr import take_qr

SESSION_TIMEOUT = 30  # seconds

# ---- Start main workflow ----

# Take QR
take_qr()

# Scan QR
qr_data = scan_qr("qr.jpg")
print("QR Data:", qr_data)

# Start session timer after QR is scanned successfully
timer = threading.Timer(SESSION_TIMEOUT, set_session_expired)
timer.start()
print(f"⏳ You have {SESSION_TIMEOUT} seconds to capture your face...")

# Take picture (will automatically exit if session expired)
take_picture()

# Stop timer in case picture was taken
timer.cancel()

# Check if session expired
from capture_face import session_expired_flag
if session_expired_flag:
    print("⏰ Session expired! Retry again.")
    exit(0)

# Scan face
student_name = check_face("captured.jpg")
if student_name:
    mark_attendance(student_name, qr_data)
else:
    print("❌ No matching face found")
