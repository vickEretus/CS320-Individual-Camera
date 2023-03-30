from PyQt5.QtWidgets import  QWidget, QLabel, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2 as cv
import sys



class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    
    def run(self):
        cap = cv.VideoCapture(0)
        print("Picture!")
        
        while(1):
            ret, frame = cap.read()
            
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

class CameraWidget(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.title = 'Video'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        
        layout.addWidget(self.label)

        self.camera_button = QPushButton("Take Picture", self)
    
        self.camera_button.clicked.connect(self.initUI)
        


        self.initUI()
        
       
        
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        if  self.camera_button.clicked.connect(self.initUI):
            self.camera_button.setEnabled(False) 
            self.camera_button.setStyleSheet('QPushButton:disabled { color: red }')
            
            
        self.setWindowTitle( self.title)
        self.setGeometry( self.left, self.top, self.width,  self.height)
        

        self.label = QLabel(self)
        self.label.resize(640, 480)
        
        th =Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show();   
        
           
          
        
            
            
        
    
    
               
    #Grab the next frame? loop~ this frame -> next frame -> loop~ 
    #FInd face
    #highlight?
    #ardino     
        
    # print("Video!")
    #        w = cv.waitKey(0)
     #       if w%256 == 27:
      #          print("Escape Hit, closing...") 
       #         cap.release()
        #        cv.destroyWindow('Frame')
         #   break
    
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CameraWidget()
    #window.show()
    sys.exit(app.exec_())
