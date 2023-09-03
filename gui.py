from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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
        logoPixmap = QPixmap("Forecast Tool Logo.png")
        logoLabel.setPixmap(logoPixmap)
        logoLabel.move(30, 30)
        logoLabel.setScaledContents(True)
        logoLabel.resize(200,100)


        # Windows are hidden by default, must run this command AT END to show!
        self.show()


# Allows app to utilize command line arguments
app = QApplication(sys.argv)

# Create an instance of the GUI Window 
window = GUIWindow()

# Start the app, return an actual exit code
sys.exit(app.exec())


