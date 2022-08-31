############################################################################################################
## AABOUGHAZALA
## USER INTERFACE FOR COMPUTER MONITOR
############################################################################################################


## IMPORTS
import sys
import os
from PySide6 import *
from qt_material import apply_stylesheet
from PySide6 import QtCore, QtGui, QtWidgets


## Import GUI FILE
from ui_mainWindow import *

## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_stylesheet(app, theme='dark_cyan.xml')
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # remove window title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # main background to transparent

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self) # shadow effect style
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow) # apply shadow

        self.setWindowIcon(QtGui.QIcon(":\\icons\\white\\airplay.svg"))


        self.show()

## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())




# pyside6-uic MainWindow.ui -o ui_mainwindow.py
# pyside6-rcc icons.qrc -o icons_rc.py