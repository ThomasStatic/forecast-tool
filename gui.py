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

        # Create a label for the number of independent variables
        indepVarLabel = QLabel(self)
        indepVarLabel.setText("Number of independent variables:")
        indepVarLabel.setStyleSheet("color: #36F1CD;")
        indepVarLabel.setFont(QFont('Arial', 20))
        indepVarLabel.adjustSize()
        indepVarLabel.move(20, 550)

        # Create a group to contain the radio buttons
        indepVarButtonGroup = QButtonGroup(self)

        # Create the radio buttons
        zeroIndepVarRB = QRadioButton("0", self)
        zeroIndepVarRB.setChecked(True) # Set the default value to 0 independent variables
        zeroIndepVarRB.numVars = 0
        oneIndepVarRB = QRadioButton("1", self)
        oneIndepVarRB.numVars = 1
        twoIndepVarRB = QRadioButton("2", self)
        twoIndepVarRB.numVars = 2
        threeIndepVarRB = QRadioButton("3", self)
        threeIndepVarRB.numVars = 3
        fourIndepVarRB = QRadioButton("4", self)
        fourIndepVarRB.numVars = 4
        fiveIndepVarRB = QRadioButton("5", self)
        fiveIndepVarRB.numVars = 5

        # Add the radio buttons to the same group
        indepVarButtonGroup.addButton(zeroIndepVarRB)
        indepVarButtonGroup.addButton(oneIndepVarRB)
        indepVarButtonGroup.addButton(twoIndepVarRB)
        indepVarButtonGroup.addButton(threeIndepVarRB)
        indepVarButtonGroup.addButton(fourIndepVarRB)
        indepVarButtonGroup.addButton(fiveIndepVarRB)

        # Move the radio buttons into place
        zeroIndepVarRB.move(450, 553)
        oneIndepVarRB.move(500, 553)
        twoIndepVarRB.move(550, 553)
        threeIndepVarRB.move(600, 553)
        fourIndepVarRB.move(650, 553)
        fiveIndepVarRB.move(700, 553)

        # Change the font colour of the buttons 
        zeroIndepVarRB.setStyleSheet("color: #36F1CD")
        oneIndepVarRB.setStyleSheet("color: #36F1CD")
        twoIndepVarRB.setStyleSheet("color: #36F1CD")
        threeIndepVarRB.setStyleSheet("color: #36F1CD")
        fourIndepVarRB.setStyleSheet("color: #36F1CD")
        fiveIndepVarRB.setStyleSheet("color: #36F1CD")

        # Connect the radiobuttons to their method
        zeroIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        oneIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        twoIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        threeIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        fourIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        fiveIndepVarRB.toggled.connect(self.radioButtonOnClicked)

        # Create the text box for indep var 1 column
        self.indepVar1Textbox = QLineEdit(self)
        self.indepVar1Textbox.setFont(QFont("Arial", 15))
        self.indepVar1Textbox.setStyleSheet("background-color: white;")
        self.indepVar1Textbox.resize(100, 35)
        self.indepVar1Textbox.move(100, 600)
        self.indepVar1Textbox.hide()
        




        # Windows are hidden by default, must run this command AT END to show!
        self.show()

    def upload_button_click(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '*.xlsx')
        print('Path file :', filename)

    def radioButtonOnClicked(self):
        """Create a function to display the appropriate number of text fields depending on what radio button is clicked"""
        
        # Identify what radiobutton was clicked
        radioButton = self.sender()
        if radioButton.isChecked():

            # Add in conditional statements to hide text fields depending on what radiobutton was selected
            print(radioButton.numVars) # Place holder code for testing buttons

            if(radioButton.numVars == 0):
                self.indepVar1Textbox.hide()

            elif(radioButton.numVars == 1):
                self.indepVar1Textbox.show()



# Allows app to utilize command line arguments
app = QApplication(sys.argv)

# Create an instance of the GUI Window 
window = GUIWindow()

# Start the app, return an actual exit code
sys.exit(app.exec())




