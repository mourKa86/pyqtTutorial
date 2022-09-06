# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1113, 646)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(36, 55, 76);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerLeft_frame = QFrame(self.header_frame)
        self.headerLeft_frame.setObjectName(u"headerLeft_frame")
        self.headerLeft_frame.setStyleSheet(u"padding:0;\n"
"margin:0;")
        self.headerLeft_frame.setFrameShape(QFrame.StyledPanel)
        self.headerLeft_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.headerLeft_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.headerLeft_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        font = QFont()
        font.setPointSize(10)
        self.menu_btn.setFont(font)
        self.menu_btn.setStyleSheet(u"margin:0;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/white/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menu_btn, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.headerLeft_frame, 0, Qt.AlignLeft)

        self.headerCenter_frame = QFrame(self.header_frame)
        self.headerCenter_frame.setObjectName(u"headerCenter_frame")
        self.headerCenter_frame.setFrameShape(QFrame.StyledPanel)
        self.headerCenter_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerCenter_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mainWindowIcon_lbl = QLabel(self.headerCenter_frame)
        self.mainWindowIcon_lbl.setObjectName(u"mainWindowIcon_lbl")
        self.mainWindowIcon_lbl.setFont(font)
        self.mainWindowIcon_lbl.setPixmap(QPixmap(u":/icons/icons/white/airplay.svg"))

        self.horizontalLayout_3.addWidget(self.mainWindowIcon_lbl, 0, Qt.AlignRight)

        self.mainWindowTitle_lbl = QLabel(self.headerCenter_frame)
        self.mainWindowTitle_lbl.setObjectName(u"mainWindowTitle_lbl")
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.mainWindowTitle_lbl.setFont(font1)

        self.horizontalLayout_3.addWidget(self.mainWindowTitle_lbl)


        self.horizontalLayout.addWidget(self.headerCenter_frame)

        self.headerRight_frame = QFrame(self.header_frame)
        self.headerRight_frame.setObjectName(u"headerRight_frame")
        self.headerRight_frame.setFrameShape(QFrame.StyledPanel)
        self.headerRight_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerRight_frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeWindow_btn = QPushButton(self.headerRight_frame)
        self.minimizeWindow_btn.setObjectName(u"minimizeWindow_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/white/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindow_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimizeWindow_btn)

        self.maximizeWindow_btn = QPushButton(self.headerRight_frame)
        self.maximizeWindow_btn.setObjectName(u"maximizeWindow_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/white/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeWindow_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.maximizeWindow_btn)

        self.closeWindow_btn = QPushButton(self.headerRight_frame)
        self.closeWindow_btn.setObjectName(u"closeWindow_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/white/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindow_btn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.closeWindow_btn)


        self.horizontalLayout.addWidget(self.headerRight_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.mainBody_frame = QFrame(self.centralwidget)
        self.mainBody_frame.setObjectName(u"mainBody_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody_frame.sizePolicy().hasHeightForWidth())
        self.mainBody_frame.setSizePolicy(sizePolicy)
        self.mainBody_frame.setFrameShape(QFrame.NoFrame)
        self.mainBody_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBody_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.leftMenuCont_frame = QFrame(self.mainBody_frame)
        self.leftMenuCont_frame.setObjectName(u"leftMenuCont_frame")
        self.leftMenuCont_frame.setMinimumSize(QSize(60, 0))
        self.leftMenuCont_frame.setMaximumSize(QSize(20, 16777215))
        self.leftMenuCont_frame.setStyleSheet(u"background-color: rgb(36, 55, 76);")
        self.leftMenuCont_frame.setFrameShape(QFrame.StyledPanel)
        self.leftMenuCont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.leftMenuCont_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.leftMenuCont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setStyleSheet(u"")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.activities_btn = QPushButton(self.menu_frame)
        self.activities_btn.setObjectName(u"activities_btn")
        self.activities_btn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/white/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activities_btn.setIcon(icon4)
        self.activities_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activities_btn, 3, 0, 1, 1, Qt.AlignLeft)

        self.storage_btn = QPushButton(self.menu_frame)
        self.storage_btn.setObjectName(u"storage_btn")
        self.storage_btn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/white/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_btn.setIcon(icon5)
        self.storage_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.storage_btn, 4, 0, 1, 1, Qt.AlignLeft)

        self.sensors_btn = QPushButton(self.menu_frame)
        self.sensors_btn.setObjectName(u"sensors_btn")
        self.sensors_btn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/white/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_btn.setIcon(icon6)
        self.sensors_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sensors_btn, 5, 0, 1, 1, Qt.AlignLeft)

        self.battery_btn = QPushButton(self.menu_frame)
        self.battery_btn.setObjectName(u"battery_btn")
        self.battery_btn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/white/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_btn.setIcon(icon7)
        self.battery_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.battery_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.cpu_btn = QPushButton(self.menu_frame)
        self.cpu_btn.setObjectName(u"cpu_btn")
        self.cpu_btn.setFont(font)
        self.cpu_btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/white/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_btn.setIcon(icon8)
        self.cpu_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cpu_btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.cpu_lbl = QLabel(self.menu_frame)
        self.cpu_lbl.setObjectName(u"cpu_lbl")
        self.cpu_lbl.setFont(font)
        self.cpu_lbl.setMargin(5)

        self.gridLayout.addWidget(self.cpu_lbl, 0, 1, 1, 1, Qt.AlignLeft)

        self.sysInfo_btn = QPushButton(self.menu_frame)
        self.sysInfo_btn.setObjectName(u"sysInfo_btn")
        self.sysInfo_btn.setFont(font)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/white/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sysInfo_btn.setIcon(icon9)
        self.sysInfo_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sysInfo_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.networks_btn = QPushButton(self.menu_frame)
        self.networks_btn.setObjectName(u"networks_btn")
        self.networks_btn.setFont(font)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/white/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.networks_btn.setIcon(icon10)
        self.networks_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.networks_btn, 6, 0, 1, 1, Qt.AlignLeft)

        self.battery_lbl = QLabel(self.menu_frame)
        self.battery_lbl.setObjectName(u"battery_lbl")
        self.battery_lbl.setFont(font)
        self.battery_lbl.setMargin(5)

        self.gridLayout.addWidget(self.battery_lbl, 1, 1, 1, 1, Qt.AlignLeft)

        self.sysInfo_lbl = QLabel(self.menu_frame)
        self.sysInfo_lbl.setObjectName(u"sysInfo_lbl")
        self.sysInfo_lbl.setFont(font)
        self.sysInfo_lbl.setMargin(5)

        self.gridLayout.addWidget(self.sysInfo_lbl, 2, 1, 1, 1, Qt.AlignLeft)

        self.activities_lbl = QLabel(self.menu_frame)
        self.activities_lbl.setObjectName(u"activities_lbl")
        self.activities_lbl.setFont(font)
        self.activities_lbl.setMargin(5)

        self.gridLayout.addWidget(self.activities_lbl, 3, 1, 1, 1, Qt.AlignLeft)

        self.storage_lbl = QLabel(self.menu_frame)
        self.storage_lbl.setObjectName(u"storage_lbl")
        self.storage_lbl.setFont(font)
        self.storage_lbl.setMargin(5)

        self.gridLayout.addWidget(self.storage_lbl, 4, 1, 1, 1, Qt.AlignLeft)

        self.sensors_lbl = QLabel(self.menu_frame)
        self.sensors_lbl.setObjectName(u"sensors_lbl")
        self.sensors_lbl.setFont(font)
        self.sensors_lbl.setMargin(5)

        self.gridLayout.addWidget(self.sensors_lbl, 5, 1, 1, 1, Qt.AlignLeft)

        self.networks_lbl = QLabel(self.menu_frame)
        self.networks_lbl.setObjectName(u"networks_lbl")
        self.networks_lbl.setFont(font)
        self.networks_lbl.setMargin(5)

        self.gridLayout.addWidget(self.networks_lbl, 6, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.leftMenuCont_frame)

        self.mainBodyCont_frame = QFrame(self.mainBody_frame)
        self.mainBodyCont_frame.setObjectName(u"mainBodyCont_frame")
        self.mainBodyCont_frame.setFrameShape(QFrame.StyledPanel)
        self.mainBodyCont_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyCont_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.mainBodyCont_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpuMemory_page = QWidget()
        self.cpuMemory_page.setObjectName(u"cpuMemory_page")
        self.verticalLayout_3 = QVBoxLayout(self.cpuMemory_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cpuTitle_frame = QFrame(self.cpuMemory_page)
        self.cpuTitle_frame.setObjectName(u"cpuTitle_frame")
        self.cpuTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.cpuTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.cpuTitle_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cpuMemoryTitle_lbl = QLabel(self.cpuTitle_frame)
        self.cpuMemoryTitle_lbl.setObjectName(u"cpuMemoryTitle_lbl")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.cpuMemoryTitle_lbl.setFont(font2)

        self.verticalLayout_4.addWidget(self.cpuMemoryTitle_lbl)


        self.verticalLayout_3.addWidget(self.cpuTitle_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.cpu_frame = QFrame(self.cpuMemory_page)
        self.cpu_frame.setObjectName(u"cpu_frame")
        sizePolicy.setHeightForWidth(self.cpu_frame.sizePolicy().hasHeightForWidth())
        self.cpu_frame.setSizePolicy(sizePolicy)
        self.cpu_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.cpu_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.cpuCount_lbl = QLabel(self.cpu_frame)
        self.cpuCount_lbl.setObjectName(u"cpuCount_lbl")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.cpuCount_lbl.setFont(font3)

        self.gridLayout_2.addWidget(self.cpuCount_lbl, 0, 0, 1, 1)

        self.cpuMainCoreVal_lbl = QLabel(self.cpu_frame)
        self.cpuMainCoreVal_lbl.setObjectName(u"cpuMainCoreVal_lbl")
        self.cpuMainCoreVal_lbl.setFont(font)

        self.gridLayout_2.addWidget(self.cpuMainCoreVal_lbl, 2, 1, 1, 1)

        self.cpuPerVal_lbl = QLabel(self.cpu_frame)
        self.cpuPerVal_lbl.setObjectName(u"cpuPerVal_lbl")
        self.cpuPerVal_lbl.setFont(font)

        self.gridLayout_2.addWidget(self.cpuPerVal_lbl, 1, 1, 1, 1)

        self.cpuMainCore_lbl = QLabel(self.cpu_frame)
        self.cpuMainCore_lbl.setObjectName(u"cpuMainCore_lbl")
        self.cpuMainCore_lbl.setFont(font3)

        self.gridLayout_2.addWidget(self.cpuMainCore_lbl, 2, 0, 1, 1)

        self.cpuPer_lbl = QLabel(self.cpu_frame)
        self.cpuPer_lbl.setObjectName(u"cpuPer_lbl")
        self.cpuPer_lbl.setFont(font3)

        self.gridLayout_2.addWidget(self.cpuPer_lbl, 1, 0, 1, 1)

        self.cpuCountVal_lbl = QLabel(self.cpu_frame)
        self.cpuCountVal_lbl.setObjectName(u"cpuCountVal_lbl")
        self.cpuCountVal_lbl.setFont(font)

        self.gridLayout_2.addWidget(self.cpuCountVal_lbl, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.cpu_frame)

        self.memory_frame = QFrame(self.cpuMemory_page)
        self.memory_frame.setObjectName(u"memory_frame")
        sizePolicy.setHeightForWidth(self.memory_frame.sizePolicy().hasHeightForWidth())
        self.memory_frame.setSizePolicy(sizePolicy)
        self.memory_frame.setFrameShape(QFrame.StyledPanel)
        self.memory_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.memory_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.usedRamVal_lbl = QLabel(self.memory_frame)
        self.usedRamVal_lbl.setObjectName(u"usedRamVal_lbl")
        self.usedRamVal_lbl.setFont(font)

        self.gridLayout_3.addWidget(self.usedRamVal_lbl, 2, 3, 1, 1)

        self.ramUsageVal_lbl = QLabel(self.memory_frame)
        self.ramUsageVal_lbl.setObjectName(u"ramUsageVal_lbl")
        self.ramUsageVal_lbl.setFont(font)

        self.gridLayout_3.addWidget(self.ramUsageVal_lbl, 4, 3, 1, 1)

        self.totalRamVal_lbl = QLabel(self.memory_frame)
        self.totalRamVal_lbl.setObjectName(u"totalRamVal_lbl")
        self.totalRamVal_lbl.setFont(font)

        self.gridLayout_3.addWidget(self.totalRamVal_lbl, 0, 3, 1, 1)

        self.totalRam_lbl = QLabel(self.memory_frame)
        self.totalRam_lbl.setObjectName(u"totalRam_lbl")
        self.totalRam_lbl.setFont(font3)

        self.gridLayout_3.addWidget(self.totalRam_lbl, 0, 1, 1, 1)

        self.freeRamVal_lbl = QLabel(self.memory_frame)
        self.freeRamVal_lbl.setObjectName(u"freeRamVal_lbl")
        self.freeRamVal_lbl.setFont(font)

        self.gridLayout_3.addWidget(self.freeRamVal_lbl, 3, 3, 1, 1)

        self.usedRam_lbl = QLabel(self.memory_frame)
        self.usedRam_lbl.setObjectName(u"usedRam_lbl")
        self.usedRam_lbl.setFont(font3)

        self.gridLayout_3.addWidget(self.usedRam_lbl, 2, 1, 1, 1)

        self.availableMemVal_lbl = QLabel(self.memory_frame)
        self.availableMemVal_lbl.setObjectName(u"availableMemVal_lbl")
        self.availableMemVal_lbl.setFont(font)

        self.gridLayout_3.addWidget(self.availableMemVal_lbl, 1, 3, 1, 1)

        self.availableMem_lbl = QLabel(self.memory_frame)
        self.availableMem_lbl.setObjectName(u"availableMem_lbl")
        self.availableMem_lbl.setFont(font3)

        self.gridLayout_3.addWidget(self.availableMem_lbl, 1, 1, 1, 1)

        self.freeRam_lbl = QLabel(self.memory_frame)
        self.freeRam_lbl.setObjectName(u"freeRam_lbl")
        self.freeRam_lbl.setFont(font3)

        self.gridLayout_3.addWidget(self.freeRam_lbl, 3, 1, 1, 1)

        self.ramUsage_lbl = QLabel(self.memory_frame)
        self.ramUsage_lbl.setObjectName(u"ramUsage_lbl")
        self.ramUsage_lbl.setFont(font3)

        self.gridLayout_3.addWidget(self.ramUsage_lbl, 4, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.memory_frame)

        self.stackedWidget.addWidget(self.cpuMemory_page)
        self.battery_page = QWidget()
        self.battery_page.setObjectName(u"battery_page")
        self.verticalLayout_6 = QVBoxLayout(self.battery_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.batteryTitle_frame = QFrame(self.battery_page)
        self.batteryTitle_frame.setObjectName(u"batteryTitle_frame")
        self.batteryTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.batteryTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.batteryTitle_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.batteryTitle_lbl = QLabel(self.batteryTitle_frame)
        self.batteryTitle_lbl.setObjectName(u"batteryTitle_lbl")
        self.batteryTitle_lbl.setFont(font2)

        self.verticalLayout_5.addWidget(self.batteryTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.batteryTitle_frame)

        self.battery_frame = QFrame(self.battery_page)
        self.battery_frame.setObjectName(u"battery_frame")
        sizePolicy.setHeightForWidth(self.battery_frame.sizePolicy().hasHeightForWidth())
        self.battery_frame.setSizePolicy(sizePolicy)
        self.battery_frame.setFrameShape(QFrame.StyledPanel)
        self.battery_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.battery_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.status_lbl = QLabel(self.battery_frame)
        self.status_lbl.setObjectName(u"status_lbl")
        self.status_lbl.setFont(font3)

        self.gridLayout_4.addWidget(self.status_lbl, 0, 0, 1, 1)

        self.statusVal_lbl = QLabel(self.battery_frame)
        self.statusVal_lbl.setObjectName(u"statusVal_lbl")
        self.statusVal_lbl.setFont(font)

        self.gridLayout_4.addWidget(self.statusVal_lbl, 0, 1, 1, 1)

        self.charge_lbl = QLabel(self.battery_frame)
        self.charge_lbl.setObjectName(u"charge_lbl")
        self.charge_lbl.setFont(font3)

        self.gridLayout_4.addWidget(self.charge_lbl, 1, 0, 1, 1)

        self.chargeVal_lbl = QLabel(self.battery_frame)
        self.chargeVal_lbl.setObjectName(u"chargeVal_lbl")
        self.chargeVal_lbl.setFont(font)

        self.gridLayout_4.addWidget(self.chargeVal_lbl, 1, 1, 1, 1)

        self.timeLeft_lbl = QLabel(self.battery_frame)
        self.timeLeft_lbl.setObjectName(u"timeLeft_lbl")
        self.timeLeft_lbl.setFont(font3)

        self.gridLayout_4.addWidget(self.timeLeft_lbl, 2, 0, 1, 1)

        self.timeLeftVal_lbl = QLabel(self.battery_frame)
        self.timeLeftVal_lbl.setObjectName(u"timeLeftVal_lbl")
        self.timeLeftVal_lbl.setFont(font)

        self.gridLayout_4.addWidget(self.timeLeftVal_lbl, 2, 1, 1, 1)

        self.pluggedIn_lbl = QLabel(self.battery_frame)
        self.pluggedIn_lbl.setObjectName(u"pluggedIn_lbl")
        self.pluggedIn_lbl.setFont(font3)

        self.gridLayout_4.addWidget(self.pluggedIn_lbl, 3, 0, 1, 1)

        self.pluggedInVal_lbl = QLabel(self.battery_frame)
        self.pluggedInVal_lbl.setObjectName(u"pluggedInVal_lbl")
        self.pluggedInVal_lbl.setFont(font)

        self.gridLayout_4.addWidget(self.pluggedInVal_lbl, 3, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.battery_frame)

        self.stackedWidget.addWidget(self.battery_page)
        self.sysInfo_page = QWidget()
        self.sysInfo_page.setObjectName(u"sysInfo_page")
        self.verticalLayout_8 = QVBoxLayout(self.sysInfo_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.sysInfoTitle_frame = QFrame(self.sysInfo_page)
        self.sysInfoTitle_frame.setObjectName(u"sysInfoTitle_frame")
        self.sysInfoTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.sysInfoTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.sysInfoTitle_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sysInfoTitle_lbl = QLabel(self.sysInfoTitle_frame)
        self.sysInfoTitle_lbl.setObjectName(u"sysInfoTitle_lbl")
        self.sysInfoTitle_lbl.setFont(font2)

        self.verticalLayout_7.addWidget(self.sysInfoTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.sysInfoTitle_frame)

        self.frame = QFrame(self.sysInfo_page)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.osVal_lbl = QLabel(self.frame)
        self.osVal_lbl.setObjectName(u"osVal_lbl")
        self.osVal_lbl.setFont(font)

        self.gridLayout_5.addWidget(self.osVal_lbl, 0, 0, 1, 1)

        self.platform_lbl = QLabel(self.frame)
        self.platform_lbl.setObjectName(u"platform_lbl")
        self.platform_lbl.setFont(font3)

        self.gridLayout_5.addWidget(self.platform_lbl, 1, 0, 1, 1)

        self.platformVal_lbl = QLabel(self.frame)
        self.platformVal_lbl.setObjectName(u"platformVal_lbl")
        self.platformVal_lbl.setFont(font)

        self.gridLayout_5.addWidget(self.platformVal_lbl, 1, 1, 1, 1)

        self.processor_lbl = QLabel(self.frame)
        self.processor_lbl.setObjectName(u"processor_lbl")
        self.processor_lbl.setFont(font3)

        self.gridLayout_5.addWidget(self.processor_lbl, 1, 2, 1, 1)

        self.version_lbl = QLabel(self.frame)
        self.version_lbl.setObjectName(u"version_lbl")
        self.version_lbl.setFont(font3)

        self.gridLayout_5.addWidget(self.version_lbl, 2, 0, 1, 1)

        self.versionVal_lbl = QLabel(self.frame)
        self.versionVal_lbl.setObjectName(u"versionVal_lbl")
        self.versionVal_lbl.setFont(font)

        self.gridLayout_5.addWidget(self.versionVal_lbl, 2, 1, 1, 1)

        self.machine_lbl = QLabel(self.frame)
        self.machine_lbl.setObjectName(u"machine_lbl")
        self.machine_lbl.setFont(font3)

        self.gridLayout_5.addWidget(self.machine_lbl, 2, 2, 1, 1)

        self.machineVal_lbl = QLabel(self.frame)
        self.machineVal_lbl.setObjectName(u"machineVal_lbl")
        self.machineVal_lbl.setFont(font)

        self.gridLayout_5.addWidget(self.machineVal_lbl, 2, 3, 1, 1)

        self.systemDate_lbl = QLabel(self.frame)
        self.systemDate_lbl.setObjectName(u"systemDate_lbl")
        self.systemDate_lbl.setFont(font3)

        self.gridLayout_5.addWidget(self.systemDate_lbl, 3, 0, 1, 1)

        self.systemDateVal_lbl = QLabel(self.frame)
        self.systemDateVal_lbl.setObjectName(u"systemDateVal_lbl")
        self.systemDateVal_lbl.setFont(font)

        self.gridLayout_5.addWidget(self.systemDateVal_lbl, 3, 1, 1, 1)

        self.systemTime_lbl = QLabel(self.frame)
        self.systemTime_lbl.setObjectName(u"systemTime_lbl")
        self.systemTime_lbl.setFont(font3)

        self.gridLayout_5.addWidget(self.systemTime_lbl, 3, 2, 1, 1)

        self.systemTimeVal_lbl = QLabel(self.frame)
        self.systemTimeVal_lbl.setObjectName(u"systemTimeVal_lbl")
        self.systemTimeVal_lbl.setFont(font)

        self.gridLayout_5.addWidget(self.systemTimeVal_lbl, 3, 3, 1, 1)


        self.verticalLayout_8.addWidget(self.frame)

        self.stackedWidget.addWidget(self.sysInfo_page)
        self.activities_page = QWidget()
        self.activities_page.setObjectName(u"activities_page")
        self.verticalLayout_10 = QVBoxLayout(self.activities_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.activitiesTitel_frame = QFrame(self.activities_page)
        self.activitiesTitel_frame.setObjectName(u"activitiesTitel_frame")
        self.activitiesTitel_frame.setFrameShape(QFrame.StyledPanel)
        self.activitiesTitel_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.activitiesTitel_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.activitiesTitle_lbl = QLabel(self.activitiesTitel_frame)
        self.activitiesTitle_lbl.setObjectName(u"activitiesTitle_lbl")
        self.activitiesTitle_lbl.setFont(font2)

        self.horizontalLayout_10.addWidget(self.activitiesTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)

        self.activitiesTitleLeft_frame = QFrame(self.activitiesTitel_frame)
        self.activitiesTitleLeft_frame.setObjectName(u"activitiesTitleLeft_frame")
        self.activitiesTitleLeft_frame.setFrameShape(QFrame.StyledPanel)
        self.activitiesTitleLeft_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.activitiesTitleLeft_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.activties_lineEdit = QLineEdit(self.activitiesTitleLeft_frame)
        self.activties_lineEdit.setObjectName(u"activties_lineEdit")
        self.activties_lineEdit.setFont(font)

        self.horizontalLayout_11.addWidget(self.activties_lineEdit, 0, Qt.AlignRight|Qt.AlignTop)

        self.activitiesSearch_btn_2 = QPushButton(self.activitiesTitleLeft_frame)
        self.activitiesSearch_btn_2.setObjectName(u"activitiesSearch_btn_2")
        self.activitiesSearch_btn_2.setFont(font)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/white/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activitiesSearch_btn_2.setIcon(icon11)
        self.activitiesSearch_btn_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_11.addWidget(self.activitiesSearch_btn_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.activitiesTitleLeft_frame, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.activitiesTitel_frame)

        self.activitiesTable_frame = QFrame(self.activities_page)
        self.activitiesTable_frame.setObjectName(u"activitiesTable_frame")
        self.activitiesTable_frame.setFrameShape(QFrame.StyledPanel)
        self.activitiesTable_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.activitiesTable_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.activities_table = QTableWidget(self.activitiesTable_frame)
        if (self.activities_table.columnCount() < 8):
            self.activities_table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.activities_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.activities_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.activities_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.activities_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.activities_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.activities_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.activities_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.activities_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.activities_table.setObjectName(u"activities_table")
        self.activities_table.setFont(font)

        self.verticalLayout_9.addWidget(self.activities_table)


        self.verticalLayout_10.addWidget(self.activitiesTable_frame)

        self.activitiesTableButtons_frame = QFrame(self.activities_page)
        self.activitiesTableButtons_frame.setObjectName(u"activitiesTableButtons_frame")
        self.activitiesTableButtons_frame.setFrameShape(QFrame.StyledPanel)
        self.activitiesTableButtons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.activitiesTableButtons_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.activitiesSuspend_btn = QPushButton(self.activitiesTableButtons_frame)
        self.activitiesSuspend_btn.setObjectName(u"activitiesSuspend_btn")
        self.activitiesSuspend_btn.setFont(font)

        self.horizontalLayout_13.addWidget(self.activitiesSuspend_btn, 0, Qt.AlignBottom)

        self.activitiesResume_btn = QPushButton(self.activitiesTableButtons_frame)
        self.activitiesResume_btn.setObjectName(u"activitiesResume_btn")
        self.activitiesResume_btn.setFont(font)

        self.horizontalLayout_13.addWidget(self.activitiesResume_btn, 0, Qt.AlignBottom)

        self.activitiesTerminate_btn = QPushButton(self.activitiesTableButtons_frame)
        self.activitiesTerminate_btn.setObjectName(u"activitiesTerminate_btn")
        self.activitiesTerminate_btn.setFont(font)

        self.horizontalLayout_13.addWidget(self.activitiesTerminate_btn, 0, Qt.AlignBottom)

        self.activitiesKill_btn = QPushButton(self.activitiesTableButtons_frame)
        self.activitiesKill_btn.setObjectName(u"activitiesKill_btn")
        self.activitiesKill_btn.setFont(font)

        self.horizontalLayout_13.addWidget(self.activitiesKill_btn, 0, Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.activitiesTableButtons_frame)

        self.stackedWidget.addWidget(self.activities_page)
        self.storage_page = QWidget()
        self.storage_page.setObjectName(u"storage_page")
        self.verticalLayout_13 = QVBoxLayout(self.storage_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.storageTitle_frame = QFrame(self.storage_page)
        self.storageTitle_frame.setObjectName(u"storageTitle_frame")
        self.storageTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.storageTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.storageTitle_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.storageTitle_lbl = QLabel(self.storageTitle_frame)
        self.storageTitle_lbl.setObjectName(u"storageTitle_lbl")
        self.storageTitle_lbl.setFont(font2)

        self.verticalLayout_11.addWidget(self.storageTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.storageTitle_frame)

        self.storageTable_frame = QFrame(self.storage_page)
        self.storageTable_frame.setObjectName(u"storageTable_frame")
        self.storageTable_frame.setFrameShape(QFrame.StyledPanel)
        self.storageTable_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.storageTable_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.storageTable = QTableWidget(self.storageTable_frame)
        if (self.storageTable.columnCount() < 9):
            self.storageTable.setColumnCount(9)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        self.storageTable.setObjectName(u"storageTable")

        self.verticalLayout_12.addWidget(self.storageTable)


        self.verticalLayout_13.addWidget(self.storageTable_frame)

        self.stackedWidget.addWidget(self.storage_page)
        self.sensors_page = QWidget()
        self.sensors_page.setObjectName(u"sensors_page")
        self.verticalLayout_16 = QVBoxLayout(self.sensors_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sensorsTitle_frame = QFrame(self.sensors_page)
        self.sensorsTitle_frame.setObjectName(u"sensorsTitle_frame")
        self.sensorsTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.sensorsTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.sensorsTitle_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sensorsTitle_lbl = QLabel(self.sensorsTitle_frame)
        self.sensorsTitle_lbl.setObjectName(u"sensorsTitle_lbl")
        self.sensorsTitle_lbl.setFont(font2)

        self.verticalLayout_14.addWidget(self.sensorsTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.sensorsTitle_frame)

        self.sensorsTable_frame = QFrame(self.sensors_page)
        self.sensorsTable_frame.setObjectName(u"sensorsTable_frame")
        self.sensorsTable_frame.setFrameShape(QFrame.StyledPanel)
        self.sensorsTable_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.sensorsTable_frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sensorsTable = QTableWidget(self.sensorsTable_frame)
        if (self.sensorsTable.columnCount() < 6):
            self.sensorsTable.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.sensorsTable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.sensorsTable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.sensorsTable.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.sensorsTable.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.sensorsTable.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.sensorsTable.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        self.sensorsTable.setObjectName(u"sensorsTable")

        self.verticalLayout_15.addWidget(self.sensorsTable)


        self.verticalLayout_16.addWidget(self.sensorsTable_frame)

        self.stackedWidget.addWidget(self.sensors_page)
        self.networks_page = QWidget()
        self.networks_page.setObjectName(u"networks_page")
        self.verticalLayout_31 = QVBoxLayout(self.networks_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.networks_scroll = QScrollArea(self.networks_page)
        self.networks_scroll.setObjectName(u"networks_scroll")
        self.networks_scroll.setFont(font)
        self.networks_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 208, 568))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.networks_frame = QFrame(self.scrollAreaWidgetContents)
        self.networks_frame.setObjectName(u"networks_frame")
        self.networks_frame.setFrameShape(QFrame.StyledPanel)
        self.networks_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.networks_frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.stats_frame = QFrame(self.networks_frame)
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setFrameShape(QFrame.StyledPanel)
        self.stats_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.stats_frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.statsTitle_frame = QFrame(self.stats_frame)
        self.statsTitle_frame.setObjectName(u"statsTitle_frame")
        self.statsTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.statsTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.statsTitle_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.statsTitle_lbl = QLabel(self.statsTitle_frame)
        self.statsTitle_lbl.setObjectName(u"statsTitle_lbl")
        self.statsTitle_lbl.setFont(font2)

        self.verticalLayout_17.addWidget(self.statsTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_21.addWidget(self.statsTitle_frame)

        self.statsTable_frame = QFrame(self.stats_frame)
        self.statsTable_frame.setObjectName(u"statsTable_frame")
        self.statsTable_frame.setFrameShape(QFrame.StyledPanel)
        self.statsTable_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.statsTable_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tableWidget = QTableWidget(self.statsTable_frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)

        self.verticalLayout_20.addWidget(self.tableWidget)


        self.verticalLayout_21.addWidget(self.statsTable_frame)


        self.verticalLayout_26.addWidget(self.stats_frame)

        self.io_frame = QFrame(self.networks_frame)
        self.io_frame.setObjectName(u"io_frame")
        self.io_frame.setFrameShape(QFrame.StyledPanel)
        self.io_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.io_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.ioTitle_frame = QFrame(self.io_frame)
        self.ioTitle_frame.setObjectName(u"ioTitle_frame")
        self.ioTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.ioTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.ioTitle_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ioTitle_lbl = QLabel(self.ioTitle_frame)
        self.ioTitle_lbl.setObjectName(u"ioTitle_lbl")
        self.ioTitle_lbl.setFont(font2)

        self.verticalLayout_18.addWidget(self.ioTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_23.addWidget(self.ioTitle_frame)

        self.ioTable_frame = QFrame(self.io_frame)
        self.ioTable_frame.setObjectName(u"ioTable_frame")
        self.ioTable_frame.setFrameShape(QFrame.StyledPanel)
        self.ioTable_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.ioTable_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.ioTable = QTableWidget(self.ioTable_frame)
        if (self.ioTable.columnCount() < 9):
            self.ioTable.setColumnCount(9)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.ioTable.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        self.ioTable.setObjectName(u"ioTable")
        self.ioTable.setFont(font)

        self.verticalLayout_22.addWidget(self.ioTable)


        self.verticalLayout_23.addWidget(self.ioTable_frame)


        self.verticalLayout_26.addWidget(self.io_frame)

        self.networksAddresses_frame = QFrame(self.networks_frame)
        self.networksAddresses_frame.setObjectName(u"networksAddresses_frame")
        self.networksAddresses_frame.setFrameShape(QFrame.StyledPanel)
        self.networksAddresses_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.networksAddresses_frame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.networkAddressesTitle_frame = QFrame(self.networksAddresses_frame)
        self.networkAddressesTitle_frame.setObjectName(u"networkAddressesTitle_frame")
        self.networkAddressesTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.networkAddressesTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.networkAddressesTitle_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.networkAddressesTitle_lbl = QLabel(self.networkAddressesTitle_frame)
        self.networkAddressesTitle_lbl.setObjectName(u"networkAddressesTitle_lbl")
        self.networkAddressesTitle_lbl.setFont(font2)

        self.verticalLayout_19.addWidget(self.networkAddressesTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_25.addWidget(self.networkAddressesTitle_frame)

        self.networksAddressesTable_frame = QFrame(self.networksAddresses_frame)
        self.networksAddressesTable_frame.setObjectName(u"networksAddressesTable_frame")
        self.networksAddressesTable_frame.setFrameShape(QFrame.StyledPanel)
        self.networksAddressesTable_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.networksAddressesTable_frame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.networkAddressesTable = QTableWidget(self.networksAddressesTable_frame)
        if (self.networkAddressesTable.columnCount() < 6):
            self.networkAddressesTable.setColumnCount(6)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.networkAddressesTable.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.networkAddressesTable.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.networkAddressesTable.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.networkAddressesTable.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.networkAddressesTable.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.networkAddressesTable.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        self.networkAddressesTable.setObjectName(u"networkAddressesTable")
        self.networkAddressesTable.setFont(font)

        self.verticalLayout_24.addWidget(self.networkAddressesTable)


        self.verticalLayout_25.addWidget(self.networksAddressesTable_frame)


        self.verticalLayout_26.addWidget(self.networksAddresses_frame)

        self.networkConnections_frame = QFrame(self.networks_frame)
        self.networkConnections_frame.setObjectName(u"networkConnections_frame")
        self.networkConnections_frame.setFrameShape(QFrame.StyledPanel)
        self.networkConnections_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.networkConnections_frame)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.networkConnectionsTitle_frame = QFrame(self.networkConnections_frame)
        self.networkConnectionsTitle_frame.setObjectName(u"networkConnectionsTitle_frame")
        self.networkConnectionsTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.networkConnectionsTitle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.networkConnectionsTitle_frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.networkConnectionsTitle_lbl = QLabel(self.networkConnectionsTitle_frame)
        self.networkConnectionsTitle_lbl.setObjectName(u"networkConnectionsTitle_lbl")
        self.networkConnectionsTitle_lbl.setFont(font2)

        self.verticalLayout_27.addWidget(self.networkConnectionsTitle_lbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_29.addWidget(self.networkConnectionsTitle_frame)

        self.networkConnectionsTable_frame = QFrame(self.networkConnections_frame)
        self.networkConnectionsTable_frame.setObjectName(u"networkConnectionsTable_frame")
        self.networkConnectionsTable_frame.setFrameShape(QFrame.StyledPanel)
        self.networkConnectionsTable_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.networkConnectionsTable_frame)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.networkConnectionsTable = QTableWidget(self.networkConnectionsTable_frame)
        if (self.networkConnectionsTable.columnCount() < 7):
            self.networkConnectionsTable.setColumnCount(7)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.networkConnectionsTable.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.networkConnectionsTable.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.networkConnectionsTable.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.networkConnectionsTable.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.networkConnectionsTable.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.networkConnectionsTable.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.networkConnectionsTable.setHorizontalHeaderItem(6, __qtablewidgetitem49)
        self.networkConnectionsTable.setObjectName(u"networkConnectionsTable")
        self.networkConnectionsTable.setFont(font)

        self.verticalLayout_28.addWidget(self.networkConnectionsTable)


        self.verticalLayout_29.addWidget(self.networkConnectionsTable_frame)


        self.verticalLayout_26.addWidget(self.networkConnections_frame)


        self.verticalLayout_30.addWidget(self.networks_frame)

        self.networks_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_31.addWidget(self.networks_scroll)

        self.stackedWidget.addWidget(self.networks_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.mainBodyCont_frame)

        self.rightCont_frame = QFrame(self.mainBody_frame)
        self.rightCont_frame.setObjectName(u"rightCont_frame")
        self.rightCont_frame.setStyleSheet(u"background-color: rgb(36, 55, 76);")
        self.rightCont_frame.setFrameShape(QFrame.StyledPanel)
        self.rightCont_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.rightCont_frame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.about_frame = QFrame(self.rightCont_frame)
        self.about_frame.setObjectName(u"about_frame")
        self.about_frame.setFrameShape(QFrame.StyledPanel)
        self.about_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.about_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.aboutTitle_lbl = QLabel(self.about_frame)
        self.aboutTitle_lbl.setObjectName(u"aboutTitle_lbl")
        self.aboutTitle_lbl.setFont(font2)

        self.verticalLayout_33.addWidget(self.aboutTitle_lbl, 0, Qt.AlignTop)

        self.aboutDesc_lbl = QLabel(self.about_frame)
        self.aboutDesc_lbl.setObjectName(u"aboutDesc_lbl")
        sizePolicy.setHeightForWidth(self.aboutDesc_lbl.sizePolicy().hasHeightForWidth())
        self.aboutDesc_lbl.setSizePolicy(sizePolicy)

        self.verticalLayout_33.addWidget(self.aboutDesc_lbl)


        self.verticalLayout_32.addWidget(self.about_frame, 0, Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.rightCont_frame)


        self.verticalLayout.addWidget(self.mainBody_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footLeft_frame = QFrame(self.footer_frame)
        self.footLeft_frame.setObjectName(u"footLeft_frame")
        self.footLeft_frame.setFrameShape(QFrame.StyledPanel)
        self.footLeft_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footLeft_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.footerVersion_lbl = QLabel(self.footLeft_frame)
        self.footerVersion_lbl.setObjectName(u"footerVersion_lbl")
        self.footerVersion_lbl.setFont(font)

        self.horizontalLayout_6.addWidget(self.footerVersion_lbl, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footLeft_frame)

        self.footerRight_frame = QFrame(self.footer_frame)
        self.footerRight_frame.setObjectName(u"footerRight_frame")
        self.footerRight_frame.setFrameShape(QFrame.StyledPanel)
        self.footerRight_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footerRight_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.footerHelp_btn = QPushButton(self.footerRight_frame)
        self.footerHelp_btn.setObjectName(u"footerHelp_btn")
        self.footerHelp_btn.setFont(font)

        self.horizontalLayout_7.addWidget(self.footerHelp_btn, 0, Qt.AlignRight)

        self.sizeGrip_frame = QFrame(self.footerRight_frame)
        self.sizeGrip_frame.setObjectName(u"sizeGrip_frame")
        self.sizeGrip_frame.setMinimumSize(QSize(10, 10))
        self.sizeGrip_frame.setMaximumSize(QSize(10, 10))
        self.sizeGrip_frame.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.sizeGrip_frame, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.footerRight_frame)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.mainWindowIcon_lbl.setText("")
        self.mainWindowTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"PSUTIL MANAGER", None))
        self.minimizeWindow_btn.setText("")
        self.maximizeWindow_btn.setText("")
        self.closeWindow_btn.setText("")
        self.activities_btn.setText("")
        self.storage_btn.setText("")
        self.sensors_btn.setText("")
        self.battery_btn.setText("")
        self.cpu_btn.setText("")
        self.cpu_lbl.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.sysInfo_btn.setText("")
        self.networks_btn.setText("")
        self.battery_lbl.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.sysInfo_lbl.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.activities_lbl.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.storage_lbl.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.sensors_lbl.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.networks_lbl.setText(QCoreApplication.translate("MainWindow", u"Networks", None))
        self.cpuMemoryTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"System Memory", None))
        self.cpuCount_lbl.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.cpuMainCoreVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpuPerVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpuMainCore_lbl.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core ", None))
        self.cpuPer_lbl.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.cpuCountVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.usedRamVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ramUsageVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.totalRamVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.totalRam_lbl.setText(QCoreApplication.translate("MainWindow", u"Total Ram", None))
        self.freeRamVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.usedRam_lbl.setText(QCoreApplication.translate("MainWindow", u"Used Ram", None))
        self.availableMemVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.availableMem_lbl.setText(QCoreApplication.translate("MainWindow", u"Available Ram", None))
        self.freeRam_lbl.setText(QCoreApplication.translate("MainWindow", u"Free Ram", None))
        self.ramUsage_lbl.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.batteryTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.status_lbl.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.charge_lbl.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.chargeVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.timeLeft_lbl.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.timeLeftVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.pluggedIn_lbl.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.pluggedInVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.sysInfoTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.osVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.platform_lbl.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.platformVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.processor_lbl.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.version_lbl.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.versionVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.machine_lbl.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.machineVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.systemDate_lbl.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.systemDateVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.systemTime_lbl.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.systemTimeVal_lbl.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.activitiesTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activties_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.activitiesSearch_btn_2.setText("")
        ___qtablewidgetitem = self.activities_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PROCESS ID", None));
        ___qtablewidgetitem1 = self.activities_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PROCESS NAME", None));
        ___qtablewidgetitem2 = self.activities_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PROCESS STATUS", None));
        ___qtablewidgetitem3 = self.activities_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"STARTED", None));
        ___qtablewidgetitem4 = self.activities_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SUSPENDED", None));
        ___qtablewidgetitem5 = self.activities_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"RESUMED", None));
        ___qtablewidgetitem6 = self.activities_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TERMINATED", None));
        ___qtablewidgetitem7 = self.activities_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"KILLED", None));
        self.activitiesSuspend_btn.setText(QCoreApplication.translate("MainWindow", u"SUSPEND", None))
        self.activitiesResume_btn.setText(QCoreApplication.translate("MainWindow", u"RESUME", None))
        self.activitiesTerminate_btn.setText(QCoreApplication.translate("MainWindow", u"TERMINATE", None))
        self.activitiesKill_btn.setText(QCoreApplication.translate("MainWindow", u"KILL", None))
        self.storageTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"Disk Partitions", None))
        ___qtablewidgetitem8 = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"DEVICE", None));
        ___qtablewidgetitem9 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"MOUNT POINT", None));
        ___qtablewidgetitem10 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem11 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"MAX FILE", None));
        ___qtablewidgetitem12 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"MAX PATH", None));
        ___qtablewidgetitem13 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"MAX BW", None));
        ___qtablewidgetitem14 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TOTAL STORAGE", None));
        ___qtablewidgetitem15 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"USED STORAGE", None));
        ___qtablewidgetitem16 = self.storageTable.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"FREE STORAGE", None));
        self.sensorsTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem17 = self.sensorsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"SESNOR", None));
        ___qtablewidgetitem18 = self.sensorsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"LABEL", None));
        ___qtablewidgetitem19 = self.sensorsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"CURRENT", None));
        ___qtablewidgetitem20 = self.sensorsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"HIGH", None));
        ___qtablewidgetitem21 = self.sensorsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"CRITICAL", None));
        self.statsTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"DUPLEX", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"SPEED", None));
        ___qtablewidgetitem25 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.ioTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"Network IO Counters", None))
        ___qtablewidgetitem26 = self.ioTable.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem27 = self.ioTable.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"BYTES SENT", None));
        ___qtablewidgetitem28 = self.ioTable.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"BYTES RECEIVED", None));
        ___qtablewidgetitem29 = self.ioTable.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"PACKETS SENT", None));
        ___qtablewidgetitem30 = self.ioTable.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"PACKETS RECEIVED", None));
        ___qtablewidgetitem31 = self.ioTable.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERRIN", None));
        ___qtablewidgetitem32 = self.ioTable.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ERROUT", None));
        ___qtablewidgetitem33 = self.ioTable.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"DROP IN", None));
        ___qtablewidgetitem34 = self.ioTable.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"DROP OUT", None));
        self.networkAddressesTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"Networks Addresses", None))
        ___qtablewidgetitem35 = self.networkAddressesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem36 = self.networkAddressesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem37 = self.networkAddressesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"NETMASK", None));
        ___qtablewidgetitem38 = self.networkAddressesTable.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"BROADCAST", None));
        ___qtablewidgetitem39 = self.networkAddressesTable.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.networkConnectionsTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem40 = self.networkConnectionsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem41 = self.networkConnectionsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem42 = self.networkConnectionsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem43 = self.networkConnectionsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem44 = self.networkConnectionsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem45 = self.networkConnectionsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem46 = self.networkConnectionsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.aboutTitle_lbl.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.aboutDesc_lbl.setText(QCoreApplication.translate("MainWindow", u"More information to be added", None))
        self.footerVersion_lbl.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright Spinn Co.", None))
        self.footerHelp_btn.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

