import cv2

def take_picture(self):
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error opening camera")
        return

    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error capturing frame")
        return

    # Save the captured frame to a file
    cv2.imwrite("picture.png", frame)

    # Release the camera
    cap.release()

    print("Picture taken!")







#class App(QWidget):