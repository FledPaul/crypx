# Import required modules
import sys, datetime, json, urllib.request

# Import PyQt5 stuff
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel


# Initialize the MainMenu
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Sets the title for the main window
        self.setWindowTitle('Crypx 2022.8.5')
        self.setFixedSize(650, 490)
        self.setStyleSheet('background-color: #FFFFFF;')

        # Transaction hash input field
        self.input = QLineEdit(self)
        self.input.resize(420, 65)
        self.input.move(35, 35)
        self.input.setPlaceholderText('Enter Transaction ...')
        self.input.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border: none; border-radius: 25px; color: rgba(68, 68, 68, 0.5); font-size: 20px; padding: 10px 20px;')

        # Transaction hash error label
        self.error = QLabel(self)
        self.error.resize(420, 20)
        self.error.move(55, 105)
        self.error.setStyleSheet('font-size: 15px; color: #FC6464; font-family: Poppins; background: transparent;')
        
        # Transferred amount label
        self.amount = QLabel(self)
        self.amount.resize(285, 65)
        self.amount.move(35, 135)
        self.amount.setText('Amount')
        self.amount.setStyleSheet('background-color: #EEEEEE; font-family: Poppins-SemiBold; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')
        
        # Fee label
        self.fee = QLabel(self)
        self.fee.resize(285, 65)
        self.fee.move(330, 135)
        self.fee.setText('Fee')
        self.fee.setStyleSheet('background-color: #EEEEEE; font-family: Poppins-SemiBold; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')
        
        # Transaction date label
        self.date = QLabel(self)
        self.date.resize(285, 65)
        self.date.move(35, 210)
        self.date.setText('Date')
        self.date.setStyleSheet('background-color: #EEEEEE; font-family: Poppins-SemiBold; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')
        
        # Transaction time label
        self.time = QLabel(self)
        self.time.resize(285, 65)
        self.time.move(330, 210)
        self.time.setText('Time')
        self.time.setStyleSheet('background-color: #EEEEEE; font-family: Poppins-SemiBold; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')
        
        # Transaction input address label
        self.txInput = QPushButton(self)
        self.txInput.resize(580, 65)
        self.txInput.move(35, 285)
        self.txInput.setText('Input Address')
        self.txInput.setStyleSheet('background-color: #EEEEEE; font-family: Poppins-SemiBold; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.5); text-align: left;')
        txInputTxt = self.txInput.text()

        # Transaction output address label
        self.txOutput = QPushButton(self)
        self.txOutput.resize(580, 65)
        self.txOutput.move(35, 360)
        self.txOutput.setText('Output Address')
        self.txOutput.setStyleSheet('background-color: #EEEEEE; font-family: Poppins-SemiBold; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5); text-align: left;')
        txOutputTxt = self.txOutput.text()

        # Add some fonts to the database
        QtGui.QFontDatabase.addApplicationFont('font/Poppins-SemiBold.ttf')
        QtGui.QFontDatabase.addApplicationFont('font/Poppins-Medium.ttf')


        def getInput():
            # Collect transaction hash
            global hashInput
            hashInput = self.input.text()
            
            try:
                # Request raw api json data & decode it
                apiDataRaw = urllib.request.urlopen('https://blockchain.info/rawtx/' + hashInput)
                apiResponse = json.loads(apiDataRaw.read().decode())    
            # Except web request errors (404, 501, etc.)
            except urllib.error.HTTPError as weberror:
                if format(weberror.code) == '404':
                    self.error.setText('Error 404 : Not Found')
                elif format(weberror.code) == '501':
                    self.error.setText('Error 501 : Not Implemented')
                else:
                    self.error.setText('Unknown Error')
            except urllib.error.URLError:
                self.error.setText('Non HTTP-Specific Error')
            except:
                self.error.setText('Unknown Error')

            # Define the api data variables
            txSatoshi = apiResponse['inputs'][0]['prev_out']['value']
            txBtc = txSatoshi / 100000000
            txFee = apiResponse['fee']
            txEpochDate = apiResponse['time']
            txDate = datetime.datetime.fromtimestamp(txEpochDate).strftime('%Y-%m-%d')
            txTime = datetime.datetime.fromtimestamp(txEpochDate).strftime('%H:%M:%S')
            txInputAddr = apiResponse['inputs'][0]['prev_out']['addr']
            txOutputAddr = apiResponse['out'][0]['addr']
            
            # Change style after submit button is clicked
            self.amount.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.fee.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.date.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.time.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.txInput.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.8); text-align: left;')
            self.txOutput.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.8); text-align: left;')
            
            # Sets requested api data to the labels
            self.amount.setText(str(str(txBtc) + ' BTC'))
            self.fee.setText(str(txFee) + ' SAT')
            self.date.setText(str(txDate))
            self.time.setText(str(txTime))
            self.txInput.setText(str(txInputAddr))
            self.txOutput.setText(str(txOutputAddr))
        
        # Submit button with color gradient
        self.submit = QPushButton(self)
        self.submit.resize(150, 65)
        self.submit.move(465, 35)
        self.submit.setText('Search')
        self.submit.setStyleSheet('background: QLinearGradient(spread:pad, x1:0, y1:0, x2:1, y5:0, stop:0 rgb(252, 252, 100), stop:1 rgb(255, 158, 20)); border: none; border-radius: 25px; font-size: 20px; color: #FFFFFF; font-family: Poppins;')
        self.submit.clicked.connect(getInput)


# Define and display the main window
mainMenu = QApplication(sys.argv)
window = MainMenu()
window.show()
mainMenu.exec()