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
        self.setWindowTitle('Crypx Wallet 2022.8.4')
        self.setFixedSize(650, 490)
        self.setStyleSheet('background-color: #FFFFFF;')

        # Returns a JSON - serializable representation of the API data.
        with urllib.request.urlopen('https://blockchain.info/rawaddr/' + address, context=ssl.create_default_context()) as url:
            apiData = json.loads(url.read().decode())
            
            # This method calculates the balance of the wallet, total received, total sent, and the number of transactions.
            balanceSat = apiData['final_balance']
            totalReceivedSat = apiData['total_received']
            totalSentSat = apiData['total_sent']
            totalReceived = totalReceivedSat / 100000000
            totalSent = totalSentSat / 100000000
            balance = balanceSat / 100000000
            allTransactions = apiData['n_tx']

        # Sets the address label
        self.address = QLabel(self)
        self.address.resize(580, 65)
        self.address.move(35, 35)
        self.address.setText(address)
        self.address.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.8); text-align: left;')

        # Sets the balance label
        self.balance = QLabel(self)
        self.balance.resize(285, 65)
        self.balance.move(35, 110)
        self.balance.setText(str(balance) + ' BTC')
        self.balance.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.8); text-align: left;')

        # Sets the all transactions label
        self.allTransactions = QLabel(self)
        self.allTransactions.resize(285, 65)
        self.allTransactions.move(330, 110)
        self.allTransactions.setText(str(allTransactions) + ' Transactions')
        self.allTransactions.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.8); text-align: left;')

        # Sets the total received label
        self.totalReceived = QLabel(self)
        self.totalReceived.resize(285, 65)
        self.totalReceived.move(35, 185)
        self.totalReceived.setText(str(totalReceived) + ' BTC')
        self.totalReceived.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.8); text-align: left;')

        # Sets the total sent label
        self.totalSent = QLabel(self)
        self.totalSent.resize(285, 65)
        self.totalSent.move(330, 185)
        self.totalSent.setText(str(totalSent) + ' BTC')
        self.totalSent.setStyleSheet('background-color: #EEEEEE; font-family: Poppins; border-radius: 25px; font-size: 20px; padding: 0px 25px; color: rgba(68, 68, 68, 0.8); text-align: left;')

        # Adds the application font to the database
        QtGui.QFontDatabase.addApplicationFont('font/Poppins-SemiBold.ttf')
        QtGui.QFontDatabase.addApplicationFont('font/Poppins-Medium.ttf')


# Define and display the MainMenu
walletAnalyzer = QApplication(sys.argv)
window = WalletAnalyzer()
window.show()
walletAnalyzer.exec()