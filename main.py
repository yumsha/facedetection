import cv2
import face_recognition
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Face Recognition", font="doom")
print(ascii_banner)

prsnimage = face_recognition.load_image_file("images/YOUR_IMAGE.jpg")
prsnencoding = face_recognition.face_encodings(prsnimage)[0]

prsnnames = ["YOUR_NAME"]
prsnencodings = [prsnencoding]

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)



    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(prsnencodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = prsnnames[first_match_index]
            coordinate = (left, top, right, bottom)
            face_location = f"{coordinate[0]}, {coordinate[1]}, {coordinate[2]}, {coordinate[3]}"
            print(f"Wajah dikenali! {name} pada {face_location}")
        else:
            name = "Unknown"
            coordinate = (left, top, right, bottom)
            face_location = f"{coordinate[0]}, {coordinate[1]}, {coordinate[2]}, {coordinate[3]}"
            print(f"Wajah tidak dikenal! pada {face_location}")


        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("recognition wannabe", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
