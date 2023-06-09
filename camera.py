from PyQt5.QtWidgets import  QWidget, QLabel, QApplication, QVBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2 as cv
import sys, serial, time 
from array import array



face_cas = cv.CascadeClassifier('C:/Users/victo/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
serialPort = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


def face(frame):
        diffx = 0
        diffy = 0
       
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        #-- Detect faces
        faces = face_cas.detectMultiScale(frame_gray, 1.2, 5)
        for (x,y,w,h) in faces:

            center = array('i', [468, 384, 640, 480])  
            #1024, 768
            #x: 185 x+w: 421 y:151 y+h: 387 center area of the screen 
            #pt1 = (x, y) #bottom left point 
            #pt2 = (x+w, y+h) # top left point 
            #pt3 = (x+w, y) # bottom right point 
            #pt4 = (x, y+h) # top left point
            squareW = x+w
            squareH = y+h
            
            frame = cv.rectangle(frame, (x, y) , (squareW, squareH),  (0, 255, 0), 2)          
            # print("x: " + str(x), "x+w: " + str(squareW), "y:" + str(y), "y+h: " + str(squareH))
            
            diffx = (center[0] - squareW) # 320 - x+w 
            diffy = (center[1] - squareH)   #240 - y+h 
           
            # creates the intial offset of the camera
            offsetAngleX = 90
            offsetAngleY = 90
            
            offsetX = ((diffx/center[2] )) * 45 # finds how much the camera needs to move 
            offsetY = ((diffy/center[3] )) * 45
            
            diffx = abs(offsetX) + offsetAngleX # ratio -> true horizontal movement value for servo     
            diffy = abs(offsetY) + offsetAngleY # ratio -> true vertical movement value for servo  

            diffx = int(diffx)
            diffy = int(diffy)
            
            
            print("x: " + str(diffx), "y: " + str(diffy))
            if(diffx >=30 and diffx <= 150):
            
                serialPort.write(f'X{diffx}\n'.encode())
                # time.sleep(0.05)
            if( diffy >=30 and diffy <= 150):
                serialPort.write(f'Y{diffy}\n'.encode())
                # time.sleep(0.05)
            
            offsetAngleX += offsetX  
            offsetAngleY += offsetY             
       
                               
            
            
            
            

             
            
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    
    
    def run(self):
        cap = cv.VideoCapture(0)
        print("Picture!")
        
        while(1):
            ret, frame = cap.read()
            
            if ret:
                face(frame)
                rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(1024, 768, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

class CameraWidget(QWidget):
 
    
    def __init__(self):
        
        super().__init__()
       
        self.title = 'Tracking-Camera'
        self.left = 100
        self.top = 100
        self.width = 1024  
        self.height = 768
        
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        
        layout.addWidget(self.label)

        self.camera_button = QPushButton("Turn on camera", self)
        self.initUI()
        
        #self.bar = QProgressBar('Loading Camera', self)
        #self.camera_button.clicked.connect(self.change_button)       
        self.camera_button.clicked.connect(self.initUI)
        
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
        
    def change_button(self):
       # if   self.camera_button.isChecked:
        self.camera_button.setEnabled(False) 
        self.camera_button.setStyleSheet('QPushButton:disabled { color: red }')
    
   

    def initUI(self):

            
            
        self.setWindowTitle( self.title)
        self.setGeometry( self.left, self.top, self.width,  self.height)
        

        self.label = QLabel(self)
        self.label.resize(1024, 768)
        self.camera_button.resize(1024, 768)
        
        
        th =Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show();   
 
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CameraWidget()
    #window.show()
    sys.exit(app.exec_())





#"C:/Users/victo/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#"C:/Users/victo/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml")
