
---

### 🔧 Prototype Stack with Python

1. **QR Code Scanning**

   * `opencv` + `pyzbar` → detect & decode QR codes using camera.
   * Alternative: `qrcode` (for generating test codes).

2. **Face Capture & Matching**
   * `opencv` → open webcam & capture photo.
   * `face_recognition` → compare captured face with stored encodings (from your “college DB” mock).
   * `dlib` (dependency for face\_recognition).

3. **Database (Mocking College DB)**

   * Use **MongoDB** (with `pymongo`).
   * Store:

     * Student ID (linked to QR code),
     * Face embedding (from `face_recognition.face_encodings`),
     * Profile details (name, roll no, etc.).

4. **Attendance Marking**

   * On successful face match:

     * Insert a document in `attendance` collection.
     * Store `student_id`, `timestamp`, and `status`.

5. **Session Management**

   * Simple **timer** with `time.time()` to auto-expire after 30s.
   * Could also maintain a session dictionary with expiry timestamps.

---

### ⏳ Flow in 30 Seconds

1. User scans QR → decode student ID.
2. Prompt photo capture → run face recognition.
3. If match found → fetch details from MongoDB.
4. Insert attendance record with current timeslot.
5. Expire session after 30s (force restart if exceeded).

---

### ✅ Why This Works for a Hackathon

* You don’t need to integrate college’s **real** database yet → mock it with a MongoDB collection.
* Everything is **self-contained in Python**.
* Can run locally without cloud infra (unless you want extra polish).

---
