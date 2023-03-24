from PyQt5 import QtWidgets
import cv2 as cv


cap = cv.VideoCapture(0)


class CameraWidget(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout(self)

        self.camera_label = QtWidgets.QLabel("Camera")
        layout.addWidget(self.camera_label)

        self.camera_button = QtWidgets.QPushButton("Take Picture")
        self.camera_button.clicked.connect(self.take_picture)
        layout.addWidget(self.camera_button)

    def take_picture(self):
        print("Picture!")
        while True:
            ret, frame = cap.read()
            cv.imshow('Frame', frame)
            print("Video!")
            
            w = cv.waitKey(1)
            if w%256 == 27:
                print("Escape Hit, closing...") 
            break
            
        
        

        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = CameraWidget()
    window.show()
    app.exec_()
