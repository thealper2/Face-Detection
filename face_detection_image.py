import cv2

image = cv2.imread("face.png")
face_cascade = cv2.CascadeClassifier("frontalface.xml")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 7)

for face in faces:
    (x, y, w, h) = face
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
