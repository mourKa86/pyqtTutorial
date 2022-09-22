############################################################################################################
## AABOUGHAZALA
## USER INTERFACE FOR COMPUTER MONITOR
############################################################################################################
## SYSTEM IMPORTS
import datetime
import platform
import shutil
import traceback
from multiprocessing import cpu_count
import sys
import os

# UI IMPORTS
from PySide2 import *
from qt_material import apply_stylesheet
from PySide2 import QtCore, QtGui, QtWidgets
import psutil
import PySide2extn
from time import sleep



# GLOBAL
platforms = {
    'linux':'Linux',
    'linux1':'Linux',
    'linux2':'OS X',
    'win32':'Windows'
}

## Import GUI FILE
from ui_mainWindow import *


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    Supported signals are:
    finished
        No data

    error
        tuple(exctype, value, traceback.format_exc())

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up

    :param callback: The function callback to run on this worker thread.
    Supplied args and
                    kwargs will be passed through to the runner
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result) # Return the result of the processing
        finally:
            self.signals.finished.emit() # Done


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
        QSizeGrip(self.ui.sizeGrip_frame)

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

        # start thread
        self.threadpool = QThreadPool()

        self.show()
        # self.battery()
        # self.cpu_ram()
        self.system_info()
        self.processes()
        self.storage()
        self.sensors()
        self.networks()
        self.psutil_thread()

    def psutil_thread(self):
        # live CPU Info
        worker = Worker(self.cpu_ram)

        # start worker
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # execute
        self.threadpool.start(worker)

        battery_worker = Worker(self.battery)

        # start worker
        battery_worker.signals.result.connect(self.print_output)
        battery_worker.signals.finished.connect(self.thread_complete)
        battery_worker.signals.progress.connect(self.progress_fn)

        # execute
        self.threadpool.start(battery_worker)

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def progress_fn(self, n):
        print(f"{n:%d%%} done")

    def networks(self):
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()
            rowPosition = self.ui.statsTable.rowCount()
            self.ui.statsTable.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "statsTable")
            self.create_table_widget(rowPosition, 1, str(z[x].isup), "statsTable")
            self.create_table_widget(rowPosition, 2, str(z[x].duplex), "statsTable")
            self.create_table_widget(rowPosition, 3, str(z[x].speed), "statsTable")
            self.create_table_widget(rowPosition, 4, str(z[x].mtu), "statsTable")

        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)
            rowPosition = self.ui.ioTable.rowCount()
            self.ui.ioTable.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "ioTable")
            self.create_table_widget(rowPosition, 1, str(z[x].bytes_sent), "ioTable")
            self.create_table_widget(rowPosition, 1, str(z[x].bytes_recv), "ioTable")
            self.create_table_widget(rowPosition, 3, str(z[x].packets_sent), "ioTable")
            self.create_table_widget(rowPosition, 4, str(z[x].packets_recv), "ioTable")
            self.create_table_widget(rowPosition, 5, str(z[x].errin), "ioTable")
            self.create_table_widget(rowPosition, 6, str(z[x].errout), "ioTable")
            self.create_table_widget(rowPosition, 7, str(z[x].dropin), "ioTable")
            self.create_table_widget(rowPosition, 8, str(z[x].dropout), "ioTable")

        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()
            for y in z[x]:
                rowPosition = self.ui.networkAddressesTable.rowCount()
                self.ui.networkAddressesTable.insertRow(rowPosition)

                self.create_table_widget(rowPosition, 0, str(x), "networkAddressesTable")
                self.create_table_widget(rowPosition, 1, str(y.family), "networkAddressesTable")
                self.create_table_widget(rowPosition, 2, str(y.address), "networkAddressesTable")
                self.create_table_widget(rowPosition, 3, str(y.netmask), "networkAddressesTable")
                self.create_table_widget(rowPosition, 4, str(y.broadcast), "networkAddressesTable")
                self.create_table_widget(rowPosition, 5, str(y.ptp), "networkAddressesTable")

        for x in psutil.net_connections():
            z = psutil.net_connections()
            rowPosition = self.ui.networkConnectionsTable.rowCount()
            self.ui.networkConnectionsTable.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0 , str(x.fd), "networkConnectionsTable")
            self.create_table_widget(rowPosition, 1, str(x.family), "networkConnectionsTable")
            self.create_table_widget(rowPosition, 2, str(x.type), "networkConnectionsTable")
            self.create_table_widget(rowPosition, 3, str(x.laddr), "networkConnectionsTable")
            self.create_table_widget(rowPosition, 4, str(x.raddr), "networkConnectionsTable")
            self.create_table_widget(rowPosition, 5, str(x.status), "networkConnectionsTable")
            self.create_table_widget(rowPosition, 6, str(x.pid), "networkConnectionsTable")

    def sensors(self):
        if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
            for x in psutil.sensors_temperatures():
                for y in psutil.sensors_temperatures()[x]:
                    rowPosition = self.ui.sensorsTable_frame.rowCount()
                    self.ui.sensorsTable.insertRow(rowPosition)

                    self.create_table_widget(rowPosition, 0, x, "sensorsTable")
                    self.create_table_widget(rowPosition, 1, y.label, "sensorsTable")
                    self.create_table_widget(rowPosition, 2, str(y.current), "sensorsTable")
                    self.create_table_widget(rowPosition, 3, str(y.high), "sensorsTable")
                    self.create_table_widget(rowPosition, 4, str(y.critical), "sensorsTable")

                    temp_per = (y.current / y.high) * 100

                    progressBar = QProgressBar(self.ui.sensorsTable)
                    progressBar.setObjectName(u"progressBar")
                    progressBar.setValue(temp_per)
                    self.ui.sensorsTable.setCellWidget(rowPosition, 5, progressBar)

        else:
            global platforms
            rowPosition = self.ui.sensorsTable.rowCount()
            self.ui.sensorsTable.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, "Function not supported on" + platforms[sys.platform], "sensorsTable")
            self.create_table_widget(rowPosition, 2, "N/A", "sensorsTable")
            self.create_table_widget(rowPosition, 3, "N/A", "sensorsTable")
            self.create_table_widget(rowPosition, 4, "N/A", "sensorsTable")
            self.create_table_widget(rowPosition, 5, "N/A", "sensorsTable")

    def storage(self):
        global platforms
        storage_device = psutil.disk_partitions(all=False)
        z = 0
        for x in storage_device:
            rowPosition = self.ui.storageTable.rowCount()
            self.ui.storageTable.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x.device, "storageTable")
            self.create_table_widget(rowPosition, 1, x.mountpoint, "storageTable")
            self.create_table_widget(rowPosition, 2, x.fstype, "storageTable")
            self.create_table_widget(rowPosition, 3, x.opts, "storageTable")

            if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
                self.create_table_widget(rowPosition, 4, str(x.maxfile), "storageTable")
                self.create_table_widget(rowPosition, 5, str(x.maxpath), "storageTable")
            else:
                self.create_table_widget(rowPosition,4, "Function not availble on" + platforms[sys.platform], "storageTable")
                self.create_table_widget(rowPosition,5,"Function not available on " + platforms[sys.platform], "storageTable")

            disk_usage = shutil.disk_usage(x.mountpoint)
            self.create_table_widget(rowPosition, 6, str((disk_usage.total / (1024 * 1024 * 1024))) + " GB", "storageTable")
            self.create_table_widget(rowPosition, 7, str((disk_usage.free / (1024 * 1024 * 1024))) + " GB", "storageTable")
            self.create_table_widget(rowPosition, 8, str((disk_usage.used / (1024 * 1024 * 1024))) + " GB", "storageTable")

            full_disk = (disk_usage.used / disk_usage.total) * 100
            progressBar = QtWidgets.QProgressBar(self.ui.storageTable)
            progressBar.setObjectName(u"progressBar")
            progressBar.setValue(full_disk)
            self.ui.storageTable.setCellWidget(rowPosition, 9, progressBar)

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

                suspend_btn = QPushButton(self.ui.activities_table)
                suspend_btn.setText('Suspend')
                suspend_btn.setStyleSheet("color: brown")
                self.ui.activities_table.setCellWidget(rowPosition, 4, suspend_btn)

                resume_btn = QPushButton(self.ui.activities_table)
                resume_btn.setText('Resume')
                resume_btn.setStyleSheet("color: green")
                self.ui.activities_table.setCellWidget(rowPosition, 5, resume_btn)

                terminate_btn = QPushButton(self.ui.activities_table)
                terminate_btn.setText('Terminate')
                terminate_btn.setStyleSheet("color: orange")
                self.ui.activities_table.setCellWidget(rowPosition, 6, terminate_btn)

                kill_btn = QPushButton(self.ui.activities_table)
                kill_btn.setText('Kill')
                kill_btn.setStyleSheet("color: red")
                self.ui.activities_table.setCellWidget(rowPosition, 7, kill_btn)

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

    def cpu_ram(self, progress_callback):
        while True:
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

            sleep(1)


    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)

    def battery(self, progress_callback):
        while True:
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

            sleep(1) # sleep 1 sec

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