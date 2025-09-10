from qr_scan import scan_qr
from face_check import check_face
from attendance import mark_attendance

# Scanning QR
qr_data = scan_qr("qr_codes/class1_qr.png")
print("QR Data:", qr_data)

# Scanning face
student_name = check_face("student_faces/student4.png")
if student_name:
    mark_attendance(student_name, qr_data)
else:
    print("❌ No matching face found")
