import sys, urllib.request, json, ssl

# Import PyQt5 stuff
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# Import other stuff
from build.mainMenu import address

# Initialize the WalletAnalyzer
class WalletAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Sets the title for the wallet analyzer
        self.setWindowTitle(address)
        self.setFixedSize(650, 490)
        self.setStyleSheet('background-color: #FFFFFF;')

        with urllib.request.urlopen('https://blockchain.info/rawaddr/' + address, context=ssl.create_default_context()) as url:
            apiData = json.loads(url.read().decode())
            print(apiData)


        # Sets the address label
        self.address = QLabel(self)
        self.address.resize(580, 65)
        self.address.move(35, 35)
        self.address.setText(address)
        self.address.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.8); text-align: left;')


# Define and display the MainMenu
walletAnalyzer = QApplication(sys.argv)
window = WalletAnalyzer()
window.show()
walletAnalyzer.exec()