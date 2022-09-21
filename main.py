############################################################################################################
## AABOUGHAZALA
## USER INTERFACE FOR COMPUTER MONITOR
############################################################################################################
import datetime
import platform
## IMPORTS
import sys
import os
from PySide2 import *
from qt_material import apply_stylesheet
from PySide2 import QtCore, QtGui, QtWidgets
import psutil
import PySide2extn
from multiprocessing import cpu_count

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

        self.setWindowIcon(QtGui.QIcon(u"icons\\white\\airplay.svg"))
        self.setWindowTitle("UTIL Manager")
        QtWidgets.QSizeGrip(self.ui.sizeGrip_frame)

        # main buttons configuraiton
        self.ui.minimizeWindow_btn.clicked.connect(lambda:self.showMinimized())
        self.ui.closeWindow_btn.clicked.connect(lambda:self.close())
        self.ui.maximizeWindow_btn.clicked.connect(lambda:self.restore_or_maximize_window())
        self.ui.cpu_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.cpuMemory_page))
        self.ui.battery_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.battery_page))
        self.ui.sysInfo_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.sysInfo_page))
        self.ui.activities_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.activities_page))
        self.ui.sensors_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.sensors_page))
        self.ui.storage_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.storage_page))
        self.ui.networks_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.networks_page))

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                # if e.buttons() == Qt.LeftButton:
                #     p = e.globalPosition()
                #     globalPos = p.toPoint()
                #     delta = QPoint(globalPos - self.oldPosition)
                #     self.move(self.x() + delta.x(), self.y() + delta.y())
                #     self.oldPosition = globalPos
                #     e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.ui.menu_btn.clicked.connect(lambda: self.slideLeftMenu())

        # Style clicked menu button
        for w in self.ui.menu_frame.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)

        self.show()
        self.battery()
        self.cpu_ram()
        self.system_info()
        self.processes()

    def processes(self):
        for x in psutil.pids():
            rowPosition = self.ui.activities_table.rowCount()
            self.ui.activities_table.insertRow(rowPosition)

            try:
                process = psutil.Process(x)
                self.create_table_widget(rowPosition, 0, str(process.pid), "activities_table")
                self.create_table_widget(rowPosition, 1, str(process.name()), "activities_table")
                self.create_table_widget(rowPosition, 2, str(process.status()), "activities_table")
                self.create_table_widget(rowPosition, 3, str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')),"activities_table")

                self.ui.activitiesSuspend_btn.setText("Suspend")
                self.ui.activitiesSuspend_btn.setStyleSheet("color: brown")
                self.ui.activities_table.setCellWidget(rowPosition, 4, self.ui.activitiesSuspend_btn)

                self.ui.activitiesResume_btn.setText("Resume")
                self.ui.activitiesResume_btn.setStyleSheet("color: green")
                self.ui.activities_table.setCellWidget(rowPosition, 5, self.ui.activitiesResume_btn)

                self.ui.activitiesTerminate_btn.setText("Terminate")
                self.ui.activitiesTerminate_btn.setStyleSheet("color: orange")
                self.ui.activities_table.setCellWidget(rowPosition, 6, self.ui.activitiesTerminate_btn)

                self.ui.activitiesKill_btn.setText("Kill")
                self.ui.activitiesKill_btn.setStyleSheet("color: red")
                self.ui.activities_table.setCellWidget(rowPosition, 7, self.ui.activitiesKill_btn)

            except Exception as e:
                print(e)

        self.ui.activties_lineEdit.textChanged.connect(self.findName)

    def findName(self):
        name = self.ui.activties_lineEdit.text().lower()
        for row in range(self.ui.activities_table.rowCount()):
            item = self.ui.activities_table.item(row,1)
            self.ui.activities_table.setRowHidden(row, name not in item.text().lower())

    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtableWidgetitem = QTableWidgetItem()
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtableWidgetitem)
        qtableWidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

        qtableWidgetitem.setText(text)

    def system_info(self):
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.ui.systemTimeVal_lbl.setText((time))
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.systemDateVal_lbl.setText(date)

        self.ui.machineVal_lbl.setText(platform.machine())
        self.ui.versionVal_lbl.setText(platform.version())
        self.ui.platformVal_lbl.setText(platform.platform())
        self.ui.osVal_lbl.setText(platform.system())
        self.ui.processorVal_lbl.setText(platform.processor())

    def cpu_ram(self):
        totalRam = 1.0
        totalRam = psutil.virtual_memory()[0] * totalRam
        totalRam = totalRam / (1024 * 1024 * 1024)
        self.ui.totalRamVal_lbl.setText(str(f"{totalRam:.4f} GB"))

        availRam = 1.0
        availRam = psutil.virtual_memory()[1] * availRam
        availRam = availRam / (1024 * 1024 * 1024)
        self.ui.availableMemVal_lbl.setText(str(f"{availRam:.4f} GB"))

        ramUsed = 1.0
        ramUsed = psutil.virtual_memory()[3] * ramUsed
        ramUsed = ramUsed / (1024 * 1024 * 1024)
        self.ui.usedRamVal_lbl.setText(str(f"{ramUsed:.4f} GB"))

        ramFree = 1.0
        ramFree = psutil.virtual_memory()[4] * ramFree
        ramFree = ramFree / (1024 * 1024 * 1024)
        self.ui.freeRamVal_lbl.setText(str(f"{ramFree:.4f} GB"))

        ramUsages = str(f"{psutil.virtual_memory()[2]}%")
        self.ui.ramUsageVal_lbl.setText(str(f"{totalRam:.4f} GB"))

        core = cpu_count()
        self.ui.cpuCountVal_lbl.setText(str(core))

        cpuPer = psutil.cpu_percent()
        self.ui.cpuPerVal_lbl.setText(str(f"{cpuPer} %"))

        cpuMainCore = psutil.cpu_count(logical=False)
        self.ui.cpuMainCoreVal_lbl.setText(str(f"{cpuMainCore}"))

        self.ui.cpuMonitor_widget.rpb_setMaximum(100) # value
        self.ui.cpuMonitor_widget.rpb_setValue(cpuPer) # values
        self.ui.cpuMonitor_widget.rpb_setBarStyle('Hybrid2') # style
        self.ui.cpuMonitor_widget.rpb_setLineStyle((255,30,99)) # line color
        self.ui.cpuMonitor_widget.rpb_setCircleColor((45,74,83)) # line color
        self.ui.cpuMonitor_widget.rpb_setPieColor((45,74,83)) # line color
        self.ui.cpuMonitor_widget.rpb_setPathColor((255,255,255)) # text color
        self.ui.cpuMonitor_widget.rpb_setInitialPos('West') # Starting position: North, East, West South
        self.ui.cpuMonitor_widget.rpb_setTextFormat('Percentage') # Value, Percentage
        self.ui.cpuMonitor_widget.rpb_setTextFont('Arial') # bar font
        self.ui.cpuMonitor_widget.rpb_setLineWidth(15) # line width
        self.ui.cpuMonitor_widget.rpb_setPathWidth(15) # width
        self.ui.cpuMonitor_widget.rpb_setLineCap('RoundCap') # RoundCap, SquareCap
        self.ui.cpuMonitor_widget.rpb_setLineStyle('Dotline') # DotLine, DashLine

        self.ui.ramMonitor_widget.spb_setMinimum((0,0,0)) # minimum value
        self.ui.ramMonitor_widget.spb_setMaximum((totalRam, totalRam, totalRam)) # maximum value
        self.ui.ramMonitor_widget.spb_setValue((availRam, ramUsed, ramFree)) # progress value
        self.ui.ramMonitor_widget.spb_lineColor(((6,233,38), (6,201,233),(233,6,201))) # (R,G,B) for the 3 lines
        self.ui.ramMonitor_widget.spb_setInitialPos((('West'),('West'),('West'))) # from outer -> inwards
        self.ui.ramMonitor_widget.spb_setDirection((('Clockwise'),('AntiClockwise'),('Clockwise'))) # outer -> inwards
        self.ui.ramMonitor_widget.spb_lineWidth(15) # 15 px
        self.ui.ramMonitor_widget.spb_lineStyle((('SolidLine'),('SolidLine'),('SolidLine'))) # line style
        self.ui.ramMonitor_widget.spb_lineCap((('RoundCap'),('RoundCap'),('RoundCap'))) # line cap
        self.ui.ramMonitor_widget.spb_setPathHidden(True)

    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return f"{hh:%d}:{mm:%02d}:{ss:02d} (H:M:S)"

    def battery(self):
        batt = psutil.sensors_battery()
        if not hasattr(psutil, "sensors_battery"):
            self.ui.statusVal_lbl.setText("Platform not supported")

        if batt is None:
            self.ui.statusVal_lbl.setText("No  battery installed")

        if batt.power_plugged:
            self.ui.chargeVal_lbl.setText(str(round(batt.percent,2))+"%")
            self.ui.timeLeftVal_lbl.setText("N/A")
            if batt.percent < 100:
                self.ui.statusVal_lbl.setText("Charging")
            else:
                self.ui.statusVal_lbl.setText("Fully Charged")
            self.ui.pluggedInVal_lbl.setText("Yes")
        else:
            self.ui.chargeVal_lbl.setText(str(round(batt.percent,2))+"%")
            self.ui.timeLeftVal_lbl.setText(self.secs2hours(batt.secsleft))
            if batt.percent < 100:
                self.ui.statusVal_lbl.setText("Discharging")
            else:
                self.ui.statusVal_lbl.setText("Fully Charged")

            self.ui.pluggedInVal_lbl.setText("No")

        # set progress bar
        self.ui.batteryMonitor_widget.rpb_setMaximum(100) # value
        self.ui.batteryMonitor_widget.rpb_setValue(batt.percent)  # values
        self.ui.batteryMonitor_widget.rpb_setBarStyle('Hybrid2') # style
        self.ui.batteryMonitor_widget.rpb_setLineColor((225, 30, 99)) # line color
        # self.ui.batteryMonitor_widget.rpb_setCircleColor((45,74,83)) # line color
        self.ui.batteryMonitor_widget.rpb_setPieColor((45,74,83)) # line color
        # self.ui.batteryMonitor_widget.rpb_setPathColor((45,74,83)) # changing path color
        self.ui.batteryMonitor_widget.rpb_setInitialPos('West') # starting position (north, east, west, south)
        self.ui.batteryMonitor_widget.rpb_setTextFormat('Percentage') # text type : value or percentage
        self.ui.batteryMonitor_widget.rpb_setLineWidth(15) # line width
        self.ui.batteryMonitor_widget.rpb_setPathWidth(15) # path width
        self.ui.batteryMonitor_widget.rpb_setLineCap('RoundCap') # RoundCap, SquareCap
        # self.ui.batteryMonitor_widget.rpb_setLineStyle('Dotline') # line style: dotline, dashline

    def applyButtonStyle(self):
        for w in self.ui.menu_frame.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():
                w.setStyleSheet("border-bottom: none;")

        self.sender().setStyleSheet("border-bottom: 2px solid")

        return
    def slideLeftMenu(self):
        width = self.ui.leftMenuCont_frame.width()
        if width == 60:
            newWidth = 200
        else:
            newWidth = 60

        self.animation = QtCore.QPropertyAnimation(self.ui.leftMenuCont_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        # p = event.globalPosition()
        # globalPos = p.toPoint()
        # self.oldPosition = globalPos

    def restore_or_maximize_window(self):
        direct = os.getcwd()
        if self.isMaximized():
            self.showNormal()
            self.ui.maximizeWindow_btn.setIcon(QtGui.QIcon("icons\\white\\maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.maximizeWindow_btn.setIcon(QtGui.QIcon("icons\\white\\minimize-2.svg"))





## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())




# pyside6-uic MainWindow.ui -o ui_mainwindow.py
# pyside6-rcc icons.qrc -o icons_rc.py