# Import sys, dateimtime, json, urllib.request
import sys, datetime, json, urllib.request, ssl

# Import PyQt5 stuff
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel

# Initialize the MainMenu
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Sets the title for the main window
        self.setWindowTitle('Crypx 2022.8.1-A')
        self.setFixedSize(650, 490)
        self.setStyleSheet('background-color: #FFFFFF;')

        # Creates a QLineEdit and sets the input
        self.input = QLineEdit(self)
        self.input.resize(420, 65)
        self.input.move(35, 35)
        self.input.setPlaceholderText('Enter Transaction ...')
        self.input.setStyleSheet('background-color: #EEEEEE; border: none; border-radius: 25px; color: rgba(68, 68, 68, 0.5); font-size: 20px; padding: 10px 20px;')

        # Sets the error label
        self.error = QLabel(self)
        self.error.resize(420, 20)
        self.error.move(55, 105)
        self.error.setStyleSheet('font-size: 15px; color: #FC6464; font-family: Poppins; background: transparent;')
        
        # Sets the amount label
        self.amount = QLabel(self)
        self.amount.resize(282, 65)
        self.amount.move(35, 135)
        self.amount.setText('Amount')
        self.amount.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')
        
        # Sets the fee label
        self.fee = QLabel(self)
        self.fee.resize(282, 65)
        self.fee.move(333, 135)
        self.fee.setText('Fee')
        self.fee.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')
        
        # Sets the date label
        self.date = QLabel(self)
        self.date.resize(282, 65)
        self.date.move(35, 220)
        self.date.setText('Date')
        self.date.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')
        
        # Sets the time label
        self.time = QLabel(self)
        self.time.resize(282, 65)
        self.time.move(333, 220)
        self.time.setText('Time')
        self.time.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')
        
        # Sets the sendFrom label
        self.sendFrom = QLabel(self)
        self.sendFrom.resize(580, 65)
        self.sendFrom.move(35, 305)
        self.sendFrom.setText('Input Address')
        self.sendFrom.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')

        # Sets the sendTo label
        self.sendTo = QLabel(self)
        self.sendTo.resize(580, 65)
        self.sendTo.move(35, 390)
        self.sendTo.setText('Output Address')
        self.sendTo.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.5);')

        # Adds the application font to the database
        QtGui.QFontDatabase.addApplicationFont('font/Poppins-SemiBold.ttf')
        QtGui.QFontDatabase.addApplicationFont('font/Poppins-Medium.ttf')
        

        def getInput():
            # Returns the hashInput
            hashInput = self.input.text()
            
            try:
                # Returns the API data as a dict
                with urllib.request.urlopen('https://blockchain.info/rawtx/' + hashInput, context=ssl.create_default_context()) as url:
                    apiData = json.loads(url.read().decode())    
            # Set the error text
            except urllib.error.HTTPError as e:
                if format(e.code) == '404':
                    self.error.setText('Error 404 : Not Found')
                elif format(e.code) == '501':
                    self.error.setText('Error 501 : Not Implemented')
                else:
                    self.error.setText('Unknown Error')
            except urllib.error.URLError:
                self.error.setText('Non HTTP-Specific Error')

            # Generate the API data
            apiSatoshi = apiData['inputs'][0]['prev_out']['value']
            apiValue = apiSatoshi / 100000000
            apiFee = apiData['fee']
            apiEpochDate = apiData['time']
            apiDate = datetime.datetime.fromtimestamp(apiEpochDate).strftime('%Y-%m-%d')
            apiTime = datetime.datetime.fromtimestamp(apiEpochDate).strftime('%H:%M:%S')
            apiInput = apiData['inputs'][0]['prev_out']['addr']
            apiOutput = apiData['out'][0]['addr']
            
            # Get API currency (bitcoin, etc)
            if apiData['inputs'][0]['prev_out']['addr'].startswith('bc'):
                apiCurrency = ' BTC'
            else:
                apiCurrency = ''
            
            # Sets the label time attributes (opacity 0.5 to opacity 0.8).
            self.amount.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.fee.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.date.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.time.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.sendFrom.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            self.sendTo.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 20px; color: rgba(68, 68, 68, 0.8);')
            
            # Sets the return data (api data)
            self.amount.setText(str(apiValue) + apiCurrency)
            self.fee.setText(str(apiFee) + ' SAT')
            self.date.setText(str(apiDate))
            self.time.setText(str(apiTime))
            self.sendFrom.setText(str(apiInput))
            self.sendTo.setText(str(apiOutput))
        
        # Creates a QPushButton and renders a linear gradient.
        self.submit = QPushButton(self)
        self.submit.resize(145, 65)
        self.submit.move(470, 35)
        self.submit.setText('Search')
        self.submit.setStyleSheet('background: QLinearGradient(spread:pad, x1:0, y1:0, x2:1, y5:0, stop:0 rgb(252, 252, 100), stop:1 rgb(255, 158, 20)); border: none; border-radius: 25px; font-size: 20px; color: #FFFFFF; font-family: Poppins;')
        self.submit.clicked.connect(getInput)


# Define and display the MainMenu
mainMenu = QApplication(sys.argv)
window = MainMenu()
window.show()
mainMenu.exec()