# Import sys
import sys

# Import PyQt5 stuff
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


# Initialize the SplashScreen
class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
            
        # Sets the window flags for frameless and top hints.
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # Setup the logo and pixmap
        self.setFixedSize(650, 400)
        self.setWindowFlags(flags)
        self.setStyleSheet('background-color: #FFFFFF;')
        self.pixmap = QPixmap('img/logo.png')
            
        # Create QLabel and set pixmap.
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.move(0, 23)
        self.label.resize(650, 354)


# Define and display the SplashScreen
app = QApplication(sys.argv)
splashScreen = SplashScreen()
splashScreen.show()


# Quit app and exit (after 2000 milliseconds)
QTimer.singleShot(2000, splashScreen.close)
app.exec()