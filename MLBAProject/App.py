from PyQt6.QtWidgets import QApplication, QMainWindow

from MLBAProject.UI.MainWindowEx import MainWindowEx
import matplotlib

matplotlib.use("QtAgg")  # backend cho PyQt6

qApp=QApplication([])
qmainWindow=QMainWindow()
window=MainWindowEx()
window.setupUi(qmainWindow)
window.show()
qApp.exec()