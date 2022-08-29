

# Import PyQt5 stuff
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# Initialize the WalletAnalyzer
class WalletAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Sets the title for the wallet analyzer
        self.setWindowTitle('Wallet Analyzer')
        self.setFixedSize(650, 490)
        self.setStyleSheet('background-color: #FFFFFF;')