from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from forecast import ForecastTool as ft
import pandas as pd

# Needed for access to command line arguments
import sys

class GUIWindow(QMainWindow):
    """This is a class to create a GUI for the forecasting tool and to allow the user to tailor how the forecast will work on their data"""
    def __init__(self):
        """Initiate all elements of the GUI window"""

        super().__init__()

        # Change the title of the window
        self.setWindowTitle("Forecast Tool")

        # Change the window icon to the forecast logo
        self.setWindowIcon(QIcon('Forecast Tool Icon.png'))

        # Resize the window
        self.resize(1000,750)

        # Change the background colour
        self.setStyleSheet("background-color: #133C55;")

        # Place the forecast logo onto the window
        self.logoLabel = QLabel(self)
        self.logoPixmap = QPixmap("Forecast Tool Icon.png")
        self.logoLabel.setPixmap(self.logoPixmap)
        self.logoLabel.move(20, 20)
        self.logoLabel.setScaledContents(True) # Set the label to not stretch the image file
        self.logoLabel.resize(200,200)

        # Insert version label
        self.versionLabel = QLabel(self)
        self.versionLabel.setText("Version: 1.0")
        self.versionLabel.setStyleSheet("color: white;")
        self.versionLabel.move(930, 0)

        # Create label for data file upload
        self.dataUploadLabel = QLabel(self)
        self.dataUploadLabel.setText("Data File:")
        self.dataUploadLabel.setStyleSheet("color: #36F1CD;")
        self.dataUploadLabel.setFont(QFont('Arial', 20))
        self.dataUploadLabel.adjustSize()
        self.dataUploadLabel.move(80, 250)

        # Create the button to upload a data file
        self.uploadButton = QPushButton(self)
        self.uploadButton.setText("Upload")
        self.uploadButton.setFont(QFont('Arial', 10))
        self.uploadButton.setStyleSheet("background-color: #80475E; color: #5FBFF9;")
        self.uploadButton.setGeometry(750,250, 200, 40)
        self.uploadButton.clicked.connect(self.upload_button_click)

        # Variable to store the user's data filepath
        self.filepath = "Default value"

        # Create the label for date column text input
        self.dateColLabel = QLabel(self)
        self.dateColLabel.setText("Date Column Name:")
        self.dateColLabel.setStyleSheet("color: #36F1CD;")
        self.dateColLabel.setFont(QFont('Arial', 20))
        self.dateColLabel.adjustSize()
        self.dateColLabel.move(20, 350)

        # Create the text box for date column
        self.dateColTextbox = QLineEdit(self)
        self.dateColTextbox.setFont(QFont("Arial", 15))
        self.dateColTextbox.setStyleSheet("background-color: white;")
        self.dateColTextbox.resize(300, 35)
        self.dateColTextbox.move(680, 350)

        # Create the label for the data column text input
        self.dataColLabel = QLabel(self)
        self.dataColLabel.setText("Data Column Name:")
        self.dataColLabel.setStyleSheet("color: #36F1CD;")
        self.dataColLabel.setFont(QFont('Arial', 20))
        self.dataColLabel.adjustSize()
        self.dataColLabel.move(20, 450)

        # Create the text box for data column
        self.dataColTextbox = QLineEdit(self)
        self.dataColTextbox.setFont(QFont("Arial", 15))
        self.dataColTextbox.setStyleSheet("background-color: white;")
        self.dataColTextbox.resize(300, 35)
        self.dataColTextbox.move(680, 450)

        # Create a label for the number of independent variables
        self.indepVarLabel = QLabel(self)
        self.indepVarLabel.setText("Number of independent variables:")
        self.indepVarLabel.setStyleSheet("color: #36F1CD;")
        self.indepVarLabel.setFont(QFont('Arial', 20))
        self.indepVarLabel.adjustSize()
        self.indepVarLabel.move(20, 550)

        # Create a group to contain the radio buttons
        self.indepVarButtonGroup = QButtonGroup(self)

        # Create the radio buttons
        self.zeroIndepVarRB = QRadioButton("0", self)
        self.zeroIndepVarRB.setChecked(True) # Set the default value to 0 independent variables
        self.zeroIndepVarRB.numVars = 0

        self.oneIndepVarRB = QRadioButton("1", self)
        self.oneIndepVarRB.numVars = 1

        self.twoIndepVarRB = QRadioButton("2", self)
        self.twoIndepVarRB.numVars = 2

        self.threeIndepVarRB = QRadioButton("3", self)
        self.threeIndepVarRB.numVars = 3

        self.fourIndepVarRB = QRadioButton("4", self)
        self.fourIndepVarRB.numVars = 4

        self.fiveIndepVarRB = QRadioButton("5", self)
        self.fiveIndepVarRB.numVars = 5

        # Add the radiobuttons to the same radiobutton group
        self.indepVarButtonGroup.addButton(self.zeroIndepVarRB)
        self.indepVarButtonGroup.addButton(self.oneIndepVarRB)
        self.indepVarButtonGroup.addButton(self.twoIndepVarRB)
        self.indepVarButtonGroup.addButton(self.threeIndepVarRB)
        self.indepVarButtonGroup.addButton(self.fourIndepVarRB)
        self.indepVarButtonGroup.addButton(self.fiveIndepVarRB)

        # Move the radio buttons into place
        self.zeroIndepVarRB.move(450, 553)
        self.oneIndepVarRB.move(500, 553)
        self.twoIndepVarRB.move(550, 553)
        self.threeIndepVarRB.move(600, 553)
        self.fourIndepVarRB.move(650, 553)
        self.fiveIndepVarRB.move(700, 553)

        # Change the font colour of the buttons 
        self.zeroIndepVarRB.setStyleSheet("color: #36F1CD")
        self.oneIndepVarRB.setStyleSheet("color: #36F1CD")
        self.twoIndepVarRB.setStyleSheet("color: #36F1CD")
        self.threeIndepVarRB.setStyleSheet("color: #36F1CD")
        self.fourIndepVarRB.setStyleSheet("color: #36F1CD")
        self.fiveIndepVarRB.setStyleSheet("color: #36F1CD")

        # Connect the radiobuttons to their method
        self.zeroIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        self.oneIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        self.twoIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        self.threeIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        self.fourIndepVarRB.toggled.connect(self.radioButtonOnClicked)
        self.fiveIndepVarRB.toggled.connect(self.radioButtonOnClicked)

        # Create the text box for indep var 1 column
        self.indepVar1Textbox = QLineEdit(self)
        self.indepVar1Textbox.setFont(QFont("Arial", 15))
        self.indepVar1Textbox.setStyleSheet("background-color: white;")
        self.indepVar1Textbox.resize(100, 35)
        self.indepVar1Textbox.move(100, 600)
        self.indepVar1Textbox.hide()
        
        # Create the text box for indep var 2 column
        self.indepVar2Textbox = QLineEdit(self)
        self.indepVar2Textbox.setFont(QFont("Arial", 15))
        self.indepVar2Textbox.setStyleSheet("background-color: white;")
        self.indepVar2Textbox.resize(100, 35)
        self.indepVar2Textbox.move(250, 600)
        self.indepVar2Textbox.hide()

        # Create the text box for indep var 3 column
        self.indepVar3Textbox = QLineEdit(self)
        self.indepVar3Textbox.setFont(QFont("Arial", 15))
        self.indepVar3Textbox.setStyleSheet("background-color: white;")
        self.indepVar3Textbox.resize(100, 35)
        self.indepVar3Textbox.move(400, 600)
        self.indepVar3Textbox.hide()

        # Create the text box for indep var 4 column
        self.indepVar4Textbox = QLineEdit(self)
        self.indepVar4Textbox.setFont(QFont("Arial", 15))
        self.indepVar4Textbox.setStyleSheet("background-color: white;")
        self.indepVar4Textbox.resize(100, 35)
        self.indepVar4Textbox.move(550, 600)
        self.indepVar4Textbox.hide()

        # Create the text box for indep var 5 column
        self.indepVar5Textbox = QLineEdit(self)
        self.indepVar5Textbox.setFont(QFont("Arial", 15))
        self.indepVar5Textbox.setStyleSheet("background-color: white;")
        self.indepVar5Textbox.resize(100, 35)
        self.indepVar5Textbox.move(700, 600)
        self.indepVar5Textbox.hide()

        # Create the button to run the forecast in conservative mode
        self.uploadButton = QPushButton(self)
        self.uploadButton.setText("Conservative")
        self.uploadButton.setFont(QFont('Arial', 15))
        self.uploadButton.setStyleSheet("background-color: #FF312E; color: 5FBFF9;")
        self.uploadButton.setGeometry(80, 650, 200, 40)
        #self.uploadButton.clicked.connect(self.upload_button_click)

        # Create the button to run the forecast in accuracy mode
        self.uploadButton = QPushButton(self)
        self.uploadButton.setText("Unbiased")
        self.uploadButton.setFont(QFont('Arial', 15))
        self.uploadButton.setStyleSheet("background-color: #FF312E; color: 5FBFF9;")
        self.uploadButton.setGeometry(415, 650, 200, 40)
        self.uploadButton.clicked.connect(self.unBiasedButtonClick)

        # Create the button to run the forecast in aggresive mode
        self.uploadButton = QPushButton(self)
        self.uploadButton.setText("Aggressive")
        self.uploadButton.setFont(QFont('Arial', 15))
        self.uploadButton.setStyleSheet("background-color: #FF312E; color: 5FBFF9;")
        self.uploadButton.setGeometry(750, 650, 200, 40)
        #self.uploadButton.clicked.connect(self.upload_button_click)




        # Windows are hidden by default, must run this command AT END to show!
        self.show()

    def upload_button_click(self):
        """Prompt the user to upload an Excel file when they click the upload button"""
        file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "Excel Files (*.xlsx)")

        if check:
            print(file)
            self.filepath = file
        

    def radioButtonOnClicked(self):
        """Display the appropriate number of text fields depending on what radio button is clicked"""
        
        # Identify what radiobutton was clicked
        radioButton = self.sender()
        if radioButton.isChecked():

            # Debugging code
            print(f"radio button clicked: {radioButton.numVars}") 

            # Conditional statement to only show the appropriate amount of text boxes so user doesn't get confused by extra text entries
            if(radioButton.numVars == 0): 
                self.indepVar1Textbox.hide() 
                self.indepVar1Textbox.clear()

                self.indepVar2Textbox.hide()
                self.indepVar2Textbox.clear()

                self.indepVar3Textbox.hide()
                self.indepVar3Textbox.clear()

                self.indepVar4Textbox.hide()
                self.indepVar4Textbox.clear()

                self.indepVar5Textbox.hide()
                self.indepVar5Textbox.clear()

            elif(radioButton.numVars == 1):
                self.indepVar1Textbox.show()

                self.indepVar2Textbox.hide()
                self.indepVar2Textbox.clear()

                self.indepVar3Textbox.hide()
                self.indepVar3Textbox.clear()

                self.indepVar4Textbox.hide()
                self.indepVar4Textbox.clear()

                self.indepVar5Textbox.hide()
                self.indepVar5Textbox.clear()

            elif(radioButton.numVars == 2):
                self.indepVar1Textbox.show()

                self.indepVar2Textbox.show()

                self.indepVar3Textbox.hide()
                self.indepVar3Textbox.clear()

                self.indepVar4Textbox.hide()
                self.indepVar4Textbox.clear()

                self.indepVar5Textbox.hide()
                self.indepVar5Textbox.clear()

            elif(radioButton.numVars == 3):
                self.indepVar1Textbox.show()

                self.indepVar2Textbox.show()

                self.indepVar3Textbox.show()

                self.indepVar4Textbox.hide()
                self.indepVar4Textbox.clear()

                self.indepVar5Textbox.hide()
                self.indepVar5Textbox.clear()

            elif(radioButton.numVars == 4):
                self.indepVar1Textbox.show()

                self.indepVar2Textbox.show()

                self.indepVar3Textbox.show()

                self.indepVar4Textbox.show()

                self.indepVar5Textbox.hide()
                self.indepVar5Textbox.clear()

            elif(radioButton.numVars == 5):
                self.indepVar1Textbox.show()

                self.indepVar2Textbox.show()

                self.indepVar3Textbox.show()

                self.indepVar4Textbox.show()

                self.indepVar5Textbox.show()

    def unBiasedButtonClick(self):
        """Run the forecast without any bias"""

        forecast = ft(filepath=self.filepath, dateCol=self.dateColTextbox.text())

        forecastResults = forecast.run_forecast_unbiased()

        print(forecastResults)

    def conservativeButtonClick(self):
        """Run the forecast conservatively"""

        forecast = ft(filepath=self.filepath, dateCol=self.dateColTextbox.text())

        forecastResults = forecast.run_forecast_conservative()

        print(forecastResults)

    def aggressiveButtonClick(self):
        """Run the forecast aggressively"""

        forecast = ft(filepath=self.filepath, dateCol=self.dateColTextbox.text())

        forecastResults = forecast.run_forecast_aggresive()

        print(forecastResults)

        


            



# Allows app to utilize command line arguments
app = QApplication(sys.argv)

# Create an instance of the GUI Window 
window = GUIWindow()

# Start the app, return an actual exit code
sys.exit(app.exec())




