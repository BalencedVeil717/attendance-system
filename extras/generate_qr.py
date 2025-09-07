# generate_qr.py
import qrcode

# QR data for prototype
qr_data = "CSE101,09:00-09:30,2025-09-07"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(qr_data)
qr.make(fit=True)

# Make an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_codes/class1_qr.png")
print("QR code saved as qr_codes/class1_qr.png")
