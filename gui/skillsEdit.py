# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skillsEdit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(766, 612)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCreate_edited_files = QAction(MainWindow)
        self.actionCreate_edited_files.setObjectName(u"actionCreate_edited_files")
        self.actionSave_Config_File_and_Create_Edited_Files = QAction(MainWindow)
        self.actionSave_Config_File_and_Create_Edited_Files.setObjectName(u"actionSave_Config_File_and_Create_Edited_Files")
        self.actionLoad_Config_File_2 = QAction(MainWindow)
        self.actionLoad_Config_File_2.setObjectName(u"actionLoad_Config_File_2")
        self.actionLoad_and_Create_Edited_Files = QAction(MainWindow)
        self.actionLoad_and_Create_Edited_Files.setObjectName(u"actionLoad_and_Create_Edited_Files")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionSave_and_Create_Edited_Files = QAction(MainWindow)
        self.actionSave_and_Create_Edited_Files.setObjectName(u"actionSave_and_Create_Edited_Files")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionNew_Config_File = QAction(MainWindow)
        self.actionNew_Config_File.setObjectName(u"actionNew_Config_File")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainTabs = QTabWidget(self.centralwidget)
        self.MainTabs.setObjectName(u"MainTabs")
        self.MainTabs.setGeometry(QRect(0, 0, 761, 531))
        self.MainTabs.setTabShape(QTabWidget.Rounded)
        self.MainTabs.setIconSize(QSize(40, 45))
        self.MainTabs.setTabsClosable(False)
        self.MainTabs.setMovable(False)
        self.SkillGrowthTableTab = QWidget()
        self.SkillGrowthTableTab.setObjectName(u"SkillGrowthTableTab")
        self.SkillGrowthCharTabs = QTabWidget(self.SkillGrowthTableTab)
        self.SkillGrowthCharTabs.setObjectName(u"SkillGrowthCharTabs")
        self.SkillGrowthCharTabs.setGeometry(QRect(0, 10, 431, 241))
        font = QFont()
        font.setPointSize(10)
        self.SkillGrowthCharTabs.setFont(font)
        self.Duran = QWidget()
        self.Duran.setObjectName(u"Duran")
        self.DuranListWidget = QListWidget(self.Duran)
        self.DuranListWidget.setObjectName(u"DuranListWidget")
        self.DuranListWidget.setGeometry(QRect(0, 0, 421, 211))
        font1 = QFont()
        font1.setFamily(u"Tempus Sans ITC")
        font1.setPointSize(10)
        self.DuranListWidget.setFont(font1)
        self.SkillGrowthCharTabs.addTab(self.Duran, "")
        self.Angela = QWidget()
        self.Angela.setObjectName(u"Angela")
        self.AngelaListWidget = QListWidget(self.Angela)
        self.AngelaListWidget.setObjectName(u"AngelaListWidget")
        self.AngelaListWidget.setGeometry(QRect(0, 0, 421, 211))
        self.AngelaListWidget.setFont(font1)
        self.SkillGrowthCharTabs.addTab(self.Angela, "")
        self.Kevin = QWidget()
        self.Kevin.setObjectName(u"Kevin")
        self.KevinListWidget = QListWidget(self.Kevin)
        self.KevinListWidget.setObjectName(u"KevinListWidget")
        self.KevinListWidget.setGeometry(QRect(0, 0, 421, 211))
        self.KevinListWidget.setFont(font1)
        self.SkillGrowthCharTabs.addTab(self.Kevin, "")
        self.Charlotte = QWidget()
        self.Charlotte.setObjectName(u"Charlotte")
        self.CharloListWidget = QListWidget(self.Charlotte)
        self.CharloListWidget.setObjectName(u"CharloListWidget")
        self.CharloListWidget.setGeometry(QRect(0, 0, 421, 211))
        self.CharloListWidget.setFont(font1)
        self.SkillGrowthCharTabs.addTab(self.Charlotte, "")
        self.Hawkeye = QWidget()
        self.Hawkeye.setObjectName(u"Hawkeye")
        self.HawkListWidget = QListWidget(self.Hawkeye)
        self.HawkListWidget.setObjectName(u"HawkListWidget")
        self.HawkListWidget.setGeometry(QRect(0, 0, 421, 211))
        self.HawkListWidget.setFont(font1)
        self.SkillGrowthCharTabs.addTab(self.Hawkeye, "")
        self.Riesz = QWidget()
        self.Riesz.setObjectName(u"Riesz")
        self.RieszListWidget = QListWidget(self.Riesz)
        self.RieszListWidget.setObjectName(u"RieszListWidget")
        self.RieszListWidget.setGeometry(QRect(0, 0, 421, 211))
        self.RieszListWidget.setFont(font1)
        self.SkillGrowthCharTabs.addTab(self.Riesz, "")
        self.UniqueSkillNameLabel = QLabel(self.SkillGrowthTableTab)
        self.UniqueSkillNameLabel.setObjectName(u"UniqueSkillNameLabel")
        self.UniqueSkillNameLabel.setGeometry(QRect(440, 60, 301, 23))
        font2 = QFont()
        font2.setFamily(u"MV Boli")
        font2.setPointSize(14)
        self.UniqueSkillNameLabel.setFont(font2)
        self.UniqueSkillNameLabel.setAlignment(Qt.AlignCenter)
        self.UniqueSkillNameLabel.setWordWrap(True)
        self.SkillNameLabel_4 = QLabel(self.SkillGrowthTableTab)
        self.SkillNameLabel_4.setObjectName(u"SkillNameLabel_4")
        self.SkillNameLabel_4.setGeometry(QRect(440, 14, 94, 23))
        font3 = QFont()
        font3.setPointSize(14)
        self.SkillNameLabel_4.setFont(font3)
        self.SkillNameLabel_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget = QWidget(self.SkillGrowthTableTab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(440, 140, 185, 27))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.IsLinkLabel_4 = QLabel(self.layoutWidget)
        self.IsLinkLabel_4.setObjectName(u"IsLinkLabel_4")
        self.IsLinkLabel_4.setFont(font3)

        self.horizontalLayout.addWidget(self.IsLinkLabel_4)

        self.IsLinkComboBox = QComboBox(self.layoutWidget)
        self.IsLinkComboBox.addItem("")
        self.IsLinkComboBox.addItem("")
        self.IsLinkComboBox.setObjectName(u"IsLinkComboBox")
        self.IsLinkComboBox.setMaximumSize(QSize(130, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        self.IsLinkComboBox.setFont(font4)

        self.horizontalLayout.addWidget(self.IsLinkComboBox)

        self.SaveEditsBtn = QPushButton(self.SkillGrowthTableTab)
        self.SaveEditsBtn.setObjectName(u"SaveEditsBtn")
        self.SaveEditsBtn.setGeometry(QRect(530, 440, 131, 41))
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.SaveEditsBtn.setPalette(palette)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.SaveEditsBtn.setFont(font5)
        self.SaveEditsBtn.setToolTipDuration(-1)
        self.SaveEditsBtn.setAutoFillBackground(False)
        self.TrainingPointsLabel_4 = QLabel(self.SkillGrowthTableTab)
        self.TrainingPointsLabel_4.setObjectName(u"TrainingPointsLabel_4")
        self.TrainingPointsLabel_4.setGeometry(QRect(440, 210, 301, 40))
        self.TrainingPointsLabel_4.setFont(font3)
        self.TPointsFrame = QFrame(self.SkillGrowthTableTab)
        self.TPointsFrame.setObjectName(u"TPointsFrame")
        self.TPointsFrame.setGeometry(QRect(440, 250, 301, 182))
        self.TPointsFrame.setFrameShape(QFrame.StyledPanel)
        self.TPointsFrame.setFrameShadow(QFrame.Raised)
        self.TPointsLineEdit_1A = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_1A.setObjectName(u"TPointsLineEdit_1A")
        self.TPointsLineEdit_1A.setGeometry(QRect(80, 11, 62, 20))
        self.TPointsLineEdit_1A.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_1A.setLayoutDirection(Qt.LeftToRight)
        self.ClassLabel_1A = QLabel(self.TPointsFrame)
        self.ClassLabel_1A.setObjectName(u"ClassLabel_1A")
        self.ClassLabel_1A.setGeometry(QRect(11, 11, 67, 19))
        self.ClassLabel_1A.setFont(font4)
        self.ClassLabel_4D = QLabel(self.TPointsFrame)
        self.ClassLabel_4D.setObjectName(u"ClassLabel_4D")
        self.ClassLabel_4D.setGeometry(QRect(160, 123, 67, 19))
        self.ClassLabel_4D.setFont(font4)
        self.TPointsLineEdit_4D = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_4D.setObjectName(u"TPointsLineEdit_4D")
        self.TPointsLineEdit_4D.setGeometry(QRect(230, 123, 63, 20))
        self.TPointsLineEdit_4D.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_4D.setLayoutDirection(Qt.LeftToRight)
        self.ClassLabel_3C = QLabel(self.TPointsFrame)
        self.ClassLabel_3C.setObjectName(u"ClassLabel_3C")
        self.ClassLabel_3C.setGeometry(QRect(11, 151, 66, 19))
        self.ClassLabel_3C.setFont(font4)
        self.TPointsLineEdit_3C = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_3C.setObjectName(u"TPointsLineEdit_3C")
        self.TPointsLineEdit_3C.setGeometry(QRect(80, 151, 62, 20))
        self.TPointsLineEdit_3C.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_3C.setLayoutDirection(Qt.LeftToRight)
        self.ClassLabel_3B = QLabel(self.TPointsFrame)
        self.ClassLabel_3B.setObjectName(u"ClassLabel_3B")
        self.ClassLabel_3B.setGeometry(QRect(11, 123, 65, 19))
        self.ClassLabel_3B.setFont(font4)
        self.TPointsLineEdit_3B = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_3B.setObjectName(u"TPointsLineEdit_3B")
        self.TPointsLineEdit_3B.setGeometry(QRect(80, 123, 62, 20))
        self.TPointsLineEdit_3B.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_3B.setLayoutDirection(Qt.LeftToRight)
        self.TPointsLineEdit_3A = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_3A.setObjectName(u"TPointsLineEdit_3A")
        self.TPointsLineEdit_3A.setGeometry(QRect(80, 95, 62, 20))
        self.TPointsLineEdit_3A.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_3A.setLayoutDirection(Qt.LeftToRight)
        self.ClassLabel_3A = QLabel(self.TPointsFrame)
        self.ClassLabel_3A.setObjectName(u"ClassLabel_3A")
        self.ClassLabel_3A.setGeometry(QRect(11, 95, 67, 19))
        self.ClassLabel_3A.setFont(font4)
        self.ClassLabel_2B = QLabel(self.TPointsFrame)
        self.ClassLabel_2B.setObjectName(u"ClassLabel_2B")
        self.ClassLabel_2B.setGeometry(QRect(11, 67, 65, 19))
        self.ClassLabel_2B.setFont(font4)
        self.TPointsLineEdit_2B = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_2B.setObjectName(u"TPointsLineEdit_2B")
        self.TPointsLineEdit_2B.setGeometry(QRect(80, 67, 62, 20))
        self.TPointsLineEdit_2B.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_2B.setLayoutDirection(Qt.LeftToRight)
        self.TPointsLineEdit_2A = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_2A.setObjectName(u"TPointsLineEdit_2A")
        self.TPointsLineEdit_2A.setGeometry(QRect(80, 39, 62, 20))
        self.TPointsLineEdit_2A.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_2A.setLayoutDirection(Qt.LeftToRight)
        self.ClassLabel_2A = QLabel(self.TPointsFrame)
        self.ClassLabel_2A.setObjectName(u"ClassLabel_2A")
        self.ClassLabel_2A.setGeometry(QRect(11, 39, 67, 19))
        self.ClassLabel_2A.setFont(font4)
        self.ClassLabel_4B = QLabel(self.TPointsFrame)
        self.ClassLabel_4B.setObjectName(u"ClassLabel_4B")
        self.ClassLabel_4B.setGeometry(QRect(160, 67, 65, 19))
        self.ClassLabel_4B.setFont(font4)
        self.TPointsLineEdit_4B = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_4B.setObjectName(u"TPointsLineEdit_4B")
        self.TPointsLineEdit_4B.setGeometry(QRect(230, 67, 62, 20))
        self.TPointsLineEdit_4B.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_4B.setLayoutDirection(Qt.LeftToRight)
        self.TPointsLineEdit_4A = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_4A.setObjectName(u"TPointsLineEdit_4A")
        self.TPointsLineEdit_4A.setGeometry(QRect(230, 39, 63, 20))
        self.TPointsLineEdit_4A.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_4A.setLayoutDirection(Qt.LeftToRight)
        self.ClassLabel_4A = QLabel(self.TPointsFrame)
        self.ClassLabel_4A.setObjectName(u"ClassLabel_4A")
        self.ClassLabel_4A.setGeometry(QRect(160, 39, 67, 19))
        self.ClassLabel_4A.setFont(font4)
        self.ClassLabel_3D = QLabel(self.TPointsFrame)
        self.ClassLabel_3D.setObjectName(u"ClassLabel_3D")
        self.ClassLabel_3D.setGeometry(QRect(160, 11, 67, 19))
        self.ClassLabel_3D.setFont(font4)
        self.TPointsLineEdit_3D = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_3D.setObjectName(u"TPointsLineEdit_3D")
        self.TPointsLineEdit_3D.setGeometry(QRect(230, 11, 63, 20))
        self.TPointsLineEdit_3D.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_3D.setLayoutDirection(Qt.LeftToRight)
        self.TPointsLineEdit_4C = QLineEdit(self.TPointsFrame)
        self.TPointsLineEdit_4C.setObjectName(u"TPointsLineEdit_4C")
        self.TPointsLineEdit_4C.setGeometry(QRect(230, 95, 64, 20))
        self.TPointsLineEdit_4C.setMaximumSize(QSize(100, 16777215))
        self.TPointsLineEdit_4C.setLayoutDirection(Qt.LeftToRight)
        self.ClassLabel_4C = QLabel(self.TPointsFrame)
        self.ClassLabel_4C.setObjectName(u"ClassLabel_4C")
        self.ClassLabel_4C.setGeometry(QRect(160, 95, 66, 19))
        self.ClassLabel_4C.setFont(font4)
        self.editsTree = QTreeWidget(self.SkillGrowthTableTab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font4);
        self.editsTree.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.editsTree)
        QTreeWidgetItem(self.editsTree)
        QTreeWidgetItem(self.editsTree)
        QTreeWidgetItem(self.editsTree)
        QTreeWidgetItem(self.editsTree)
        QTreeWidgetItem(self.editsTree)
        self.editsTree.setObjectName(u"editsTree")
        self.editsTree.setGeometry(QRect(0, 260, 431, 241))
        self.editsTree.setIndentation(10)
        self.editsTree.setColumnCount(1)
        self.removeSelectionBtn = QPushButton(self.SkillGrowthTableTab)
        self.removeSelectionBtn.setObjectName(u"removeSelectionBtn")
        self.removeSelectionBtn.setGeometry(QRect(320, 260, 111, 30))
        self.MainTabs.addTab(self.SkillGrowthTableTab, "")
        self.FINISHlabel = QLabel(self.centralwidget)
        self.FINISHlabel.setObjectName(u"FINISHlabel")
        self.FINISHlabel.setGeometry(QRect(110, 530, 301, 41))
        self.FINISHlabel.setWordWrap(True)
        self.FINISHbtn = QPushButton(self.centralwidget)
        self.FINISHbtn.setObjectName(u"FINISHbtn")
        self.FINISHbtn.setGeometry(QRect(10, 535, 91, 31))
        self.CurrentConfigLabel = QLabel(self.centralwidget)
        self.CurrentConfigLabel.setObjectName(u"CurrentConfigLabel")
        self.CurrentConfigLabel.setGeometry(QRect(430, 530, 331, 16))
        self.CurrentConfigEditLabel = QLabel(self.centralwidget)
        self.CurrentConfigEditLabel.setObjectName(u"CurrentConfigEditLabel")
        self.CurrentConfigEditLabel.setGeometry(QRect(450, 550, 311, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 766, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSave_Config_File = QMenu(self.menuFile)
        self.menuSave_Config_File.setObjectName(u"menuSave_Config_File")
        self.menuLoad_Config_File = QMenu(self.menuFile)
        self.menuLoad_Config_File.setObjectName(u"menuLoad_Config_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew_Config_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuSave_Config_File.menuAction())
        self.menuFile.addAction(self.menuLoad_Config_File.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_edited_files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSave_Config_File.addAction(self.actionSave)
        self.menuSave_Config_File.addAction(self.actionSave_as)
        self.menuSave_Config_File.addSeparator()
        self.menuSave_Config_File.addAction(self.actionSave_and_Create_Edited_Files)
        self.menuLoad_Config_File.addAction(self.actionLoad_Config_File_2)
        self.menuLoad_Config_File.addAction(self.actionLoad_and_Create_Edited_Files)

        self.retranslateUi(MainWindow)

        self.MainTabs.setCurrentIndex(0)
        self.SkillGrowthCharTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionCreate_edited_files.setText(QCoreApplication.translate("MainWindow", u"Create edited files without saving", None))
        self.actionSave_Config_File_and_Create_Edited_Files.setText(QCoreApplication.translate("MainWindow", u"Save Config File and Create Edited Files", None))
        self.actionLoad_Config_File_2.setText(QCoreApplication.translate("MainWindow", u"Load Into Edits Tree", None))
        self.actionLoad_and_Create_Edited_Files.setText(QCoreApplication.translate("MainWindow", u"Load and Create Edited Files", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.actionSave_and_Create_Edited_Files.setText(QCoreApplication.translate("MainWindow", u"Save and Create Edited Files", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionNew_Config_File.setText(QCoreApplication.translate("MainWindow", u"New Config File", None))
#if QT_CONFIG(tooltip)
        self.MainTabs.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.SkillGrowthCharTabs.setTabText(self.SkillGrowthCharTabs.indexOf(self.Duran), QCoreApplication.translate("MainWindow", u"DURAN", None))
        self.SkillGrowthCharTabs.setTabText(self.SkillGrowthCharTabs.indexOf(self.Angela), QCoreApplication.translate("MainWindow", u"ANGELA", None))
        self.SkillGrowthCharTabs.setTabText(self.SkillGrowthCharTabs.indexOf(self.Kevin), QCoreApplication.translate("MainWindow", u"KEVIN", None))
        self.SkillGrowthCharTabs.setTabText(self.SkillGrowthCharTabs.indexOf(self.Charlotte), QCoreApplication.translate("MainWindow", u"CHARLOTTE", None))
        self.SkillGrowthCharTabs.setTabText(self.SkillGrowthCharTabs.indexOf(self.Hawkeye), QCoreApplication.translate("MainWindow", u"HAWKEYE", None))
        self.SkillGrowthCharTabs.setTabText(self.SkillGrowthCharTabs.indexOf(self.Riesz), QCoreApplication.translate("MainWindow", u"RIESZ", None))
        self.UniqueSkillNameLabel.setText(QCoreApplication.translate("MainWindow", u"<Selected Skill Shows Here>", None))
        self.SkillNameLabel_4.setText(QCoreApplication.translate("MainWindow", u"Skill Name:", None))
        self.IsLinkLabel_4.setText(QCoreApplication.translate("MainWindow", u"Is Link Ability:", None))
        self.IsLinkComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.IsLinkComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

#if QT_CONFIG(tooltip)
        self.SaveEditsBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.SaveEditsBtn.setText(QCoreApplication.translate("MainWindow", u"Save Edits", None))
        self.TrainingPointsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Training Points required (per class):", None))
        self.ClassLabel_1A.setText(QCoreApplication.translate("MainWindow", u"Class 1A:", None))
        self.ClassLabel_4D.setText(QCoreApplication.translate("MainWindow", u"Class 4D:", None))
        self.ClassLabel_3C.setText(QCoreApplication.translate("MainWindow", u"Class 3C:", None))
        self.ClassLabel_3B.setText(QCoreApplication.translate("MainWindow", u"Class 3B:", None))
        self.ClassLabel_3A.setText(QCoreApplication.translate("MainWindow", u"Class 3A:", None))
        self.ClassLabel_2B.setText(QCoreApplication.translate("MainWindow", u"Class 2B:", None))
        self.ClassLabel_2A.setText(QCoreApplication.translate("MainWindow", u"Class 2A:", None))
        self.ClassLabel_4B.setText(QCoreApplication.translate("MainWindow", u"Class 4B:", None))
        self.ClassLabel_4A.setText(QCoreApplication.translate("MainWindow", u"Class 4A:", None))
        self.ClassLabel_3D.setText(QCoreApplication.translate("MainWindow", u"Class 3D:", None))
        self.ClassLabel_4C.setText(QCoreApplication.translate("MainWindow", u"Class 4C:", None))
        ___qtreewidgetitem = self.editsTree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Edits:", None));

        __sortingEnabled = self.editsTree.isSortingEnabled()
        self.editsTree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.editsTree.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Duran", None));
        ___qtreewidgetitem2 = self.editsTree.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Angela", None));
        ___qtreewidgetitem3 = self.editsTree.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Kevin", None));
        ___qtreewidgetitem4 = self.editsTree.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Charlotte", None));
        ___qtreewidgetitem5 = self.editsTree.topLevelItem(4)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Hawkeye", None));
        ___qtreewidgetitem6 = self.editsTree.topLevelItem(5)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Riesz", None));
        self.editsTree.setSortingEnabled(__sortingEnabled)

        self.removeSelectionBtn.setText(QCoreApplication.translate("MainWindow", u"Remove Selection", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.SkillGrowthTableTab), QCoreApplication.translate("MainWindow", u"Skill Growth Table", None))
        self.FINISHlabel.setText(QCoreApplication.translate("MainWindow", u"Click 'FINISH' when you want to create the edited files to be paked. Options that include saving and loading config files can be found in the 'File' Menu.", None))
        self.FINISHbtn.setText(QCoreApplication.translate("MainWindow", u"FINISH", None))
        self.CurrentConfigLabel.setText(QCoreApplication.translate("MainWindow", u"Current config file:", None))
        self.CurrentConfigEditLabel.setText(QCoreApplication.translate("MainWindow", u"New config file", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSave_Config_File.setTitle(QCoreApplication.translate("MainWindow", u"Save Config File", None))
        self.menuLoad_Config_File.setTitle(QCoreApplication.translate("MainWindow", u"Load Config File", None))
    # retranslateUi

