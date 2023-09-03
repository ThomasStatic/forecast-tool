from PyQt5.QtWidgets import QApplication, QWidget

# Needed for access to command line arguments
import sys

# Allows app to utilize command line arguments
app = QApplication(sys.argv)

# Create a QWidget which is the window
window = QWidget()
window.show() # Windows are hidden by default

#Change the title of the window
window.setWindowTitle("Forecast Tool")

#Start the event loop
app.exec()