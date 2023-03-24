import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QComboBox, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.uic import loadUi
import random
import pickle

import cv2 as cv

import threading
import time
from queue import Queue


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Start Video")

        # Set the central widget of the Window.
        self.setCentralWidget(button)
    

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window =  MainWindow()

window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()