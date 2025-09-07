import csv
from datetime import datetime


def mark_attendance(student_name, qr_data, csv_file="attendance.csv"):
    """
    Appends student attendance to CSV.
    """
    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                student_name,
                qr_data["class_id"],
                qr_data["time_slot"],
                qr_data["date"],
                datetime.now().strftime("%H:%M:%S"),
            ]
        )
    print(f"✅ Attendance logged for {student_name}")
