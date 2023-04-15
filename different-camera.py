from PyQt5.QtWidgets import  QWidget, QLabel, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2 as cv
import sys, serial, time, math 
import dlib

face_cas = cv.CascadeClassifier('C:/Users/victo/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
serialPort = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


global diffx
diffx = 45
global diffy
diffy = 90
            

def face(frame):
      
       
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        #-- Detect faces
        faces = face_cas.detectMultiScale(frame_gray, 1.2, 5)
        for (x,y,w,h) in faces:
            # center = array('i', [468, 384, 640, 480]) 
            
            center = (x + w//2, y + h//2)
            frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4) 
           
            #pt1 = (x, y) #bottom left point 
            #pt2 = (x+w, y+h) # top left point 
            #pt3 = (x+w, y) # bottom right point 
            #pt4 = (x, y+h) # top left point
            
            
            
            #print("x: " + str(x), "x+w: " + str(squareW), "y:" + str(y), "y+h: " + str(squareH))
            
         
         
            changeServoPosition (x + w//2, y + h//2)    
    
            
            
           

    
# position servos to the center of the object's frame
def changeServoPosition (x, y):
    # x: 180 x+w: 424 y:120 y+h: 364
    # x: 241, x+w: 363, y:181, y+h: 303 smaller area same center
    global diffx
    global diffy
    if (x < 241):
        diffx += 2.5
        if diffx > 180:
            diffx = 180
            
        string = (f'X{diffx}\n'.encode())
        positionServo (diffx, string)
        
    if (x > 363):
        diffx -= 2.5
        if diffx < 0:
            diffx = 0
            
        string = (f'X{diffx}\n'.encode())
        positionServo (diffx, string)
        
    if (y < 181):
        diffy -= 2.5
        if diffy > 140:
            diffy = 140
            
        string = (f'Y{diffy}\n'.encode())
        positionServo ( diffy, string)
        
    if (y > 303):
        diffy += 2.5
        if diffy < 40:
            diffy = 40
            
        string = (f'Y{diffy}\n'.encode())
        positionServo ( diffy, string)          
        
        
    
                               
def positionServo (angle, string):       
    serialPort.write(string)
    time.sleep(0.01)

    print("x: " + str(diffx), "y: " + str(diffy)) 
            
              
       
         
            
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
        self.height = 800
        
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        
        layout.addWidget(self.label)

        self.camera_button = QPushButton("Turn on camera", self)
        self.initUI()
        self.camera_button.clicked.connect(self.initUI)       
     
        
      
        
        
    def Reset(self):
        global diffx
        global diffy
        diffx = 90
        diffy = 90
        serialPort.write(f'X{diffx}\n'.encode())
        serialPort.write(f'Y{diffx}\n'.encode())
    
        
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
   

    def initUI(self):

     
            
        self.setWindowTitle( self.title)
        self.setGeometry( self.left, self.top, self.width,  self.height)
        

        self.label = QLabel(self)
        self.label.resize(1024, 768)
        self.camera_button.resize(1024, 768)
        
        
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.move(0, 768)
        self.reset_button.clicked.connect(self.Reset)
        
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
