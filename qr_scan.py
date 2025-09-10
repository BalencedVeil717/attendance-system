from pyzbar.pyzbar import decode
from PIL import Image


def scan_qr(qr_image_path):
    """
    Simulate QR scan. Returns a dict with session data.
    """
    img = Image.open(qr_image_path)
    decoded = decode(img)
    if decoded:
        data = decoded[0].data.decode("utf-8")

        class_id, time_slot, date = data.split(",")
        return {"class_id": class_id, "time_slot": time_slot, "date": date}
    else:
        raise ValueError("No QR code detected!")


# if __name__ == "__main__":
#     qr_data = scan_qr("qr_codes/class1_qr.png")
#     print("QR Data:", qr_data)
