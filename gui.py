from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

# Needed for access to command line arguments
import sys

class GUIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Change the title of the window
        self.setWindowTitle("Forecast Tool")

        # Change the window icon
        self.setWindowIcon(QIcon('Forecast Tool Icon.png'))

        # Resize the window
        self.resize(1000,750)

        # Change the background colour
        self.setStyleSheet("background-color: #133C55;")

        # Insert the logo image
        logoLabel = QLabel(self)
        logoPixmap = QPixmap("Forecast Tool Icon.png")
        logoLabel.setPixmap(logoPixmap)
        logoLabel.move(20, 20)
        logoLabel.setScaledContents(True)
        logoLabel.resize(200,200)

        # Insert version label
        versionLabel = QLabel(self)
        versionLabel.setText("Version: 1.0")
        versionLabel.setStyleSheet("color: white;")
        versionLabel.move(930, 0)

        # Create label for data file upload
        dataUploadLabel = QLabel(self)
        dataUploadLabel.setText("Data File:")
        dataUploadLabel.setStyleSheet("color: #36F1CD;")
        dataUploadLabel.setFont(QFont('Arial', 20))
        dataUploadLabel.adjustSize()
        dataUploadLabel.move(80, 250)

        # Create the button to upload a data file
        uploadButton = QPushButton(self)
        uploadButton.setText("Upload")
        uploadButton.setFont(QFont('Arial', 10))
        uploadButton.setStyleSheet("background-color: #80475E; color: #5FBFF9;")
        uploadButton.setGeometry(750,250, 200, 40)
        uploadButton.clicked.connect(self.upload_button_click)

        # Create the label for date column text input
        dateColLabel = QLabel(self)
        dateColLabel.setText("Date Column Name:")
        dateColLabel.setStyleSheet("color: #36F1CD;")
        dateColLabel.setFont(QFont('Arial', 20))
        dateColLabel.adjustSize()
        dateColLabel.move(20, 350)

        # Create the text box for date column
        dateColTextbox = QLineEdit(self)
        dateColTextbox.setFont(QFont("Arial", 15))
        dateColTextbox.setStyleSheet("background-color: white;")
        dateColTextbox.resize(300, 35)
        dateColTextbox.move(680, 350)

        # Create the label for the data column text input
        dataColLabel = QLabel(self)
        dataColLabel.setText("Data Column Name:")
        dataColLabel.setStyleSheet("color: #36F1CD;")
        dataColLabel.setFont(QFont('Arial', 20))
        dataColLabel.adjustSize()
        dataColLabel.move(20, 450)

        # Create the text box for data column
        dataColTextbox = QLineEdit(self)
        dataColTextbox.setFont(QFont("Arial", 15))
        dataColTextbox.setStyleSheet("background-color: white;")
        dataColTextbox.resize(300, 35)
        dataColTextbox.move(680, 450)





        # Windows are hidden by default, must run this command AT END to show!
        self.show()

    def upload_button_click(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '*.xlsx')
        print('Path file :', filename)


# Allows app to utilize command line arguments
app = QApplication(sys.argv)

# Create an instance of the GUI Window 
window = GUIWindow()

# Start the app, return an actual exit code
sys.exit(app.exec())




