# Import required modules
import sys, requests

# Import PyQt5 stuff
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer


# Initialize the splash screen
class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Remove the window title bar etc.
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)         

        # Setup the logo and pixmap
        self.setFixedSize(650, 400)
        self.setWindowFlags(flags)
        self.setStyleSheet('background-color: #FFFFFF;')
         
        # Get image from server (not yet stored in cache)
        urlImage = 'https://file.fled.dev/apps/crypx/versions/2022.8.5.png'
        Image = QImage()
        Image.loadFromData(requests.get(urlImage).content)
        
        # Image label (cover full window)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(Image))
        self.label.move(0, 23)
        self.label.resize(650, 354)


# Define and display the splash screen
splashScreen = QApplication(sys.argv)
window = SplashScreen()
window.show()

# Quit app and exit (after 2000 milliseconds)
QTimer.singleShot(2000, window.close)
splashScreen.exec()
