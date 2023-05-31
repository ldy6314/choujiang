# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(19)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.display_area = QLabel(self.centralwidget)
        self.display_area.setObjectName(u"display_area")
        font2 = QFont()
        font2.setPointSize(60)
        self.display_area.setFont(font2)
        self.display_area.setStyleSheet(u"background-color:balck;\n"
"color:yellow;\n"
"text-align:center;")

        self.verticalLayout.addWidget(self.display_area)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")

        self.horizontalLayout.addWidget(self.load_button)

        self.ok_button = QPushButton(self.centralwidget)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout.addWidget(self.ok_button)

        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")

        self.horizontalLayout.addWidget(self.clear_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.wzj_area = QTextEdit(self.groupBox)
        self.wzj_area.setObjectName(u"wzj_area")

        self.horizontalLayout_2.addWidget(self.wzj_area)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.zj_area = QTextEdit(self.groupBox_2)
        self.zj_area.setObjectName(u"zj_area")

        self.horizontalLayout_3.addWidget(self.zj_area)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 38))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u5408\u80a5\u5e02\u9526\u57ce\u5c0f\u5b6610\u5468\u5e74\u62bd\u5956</p></body></html>", None))
        self.display_area.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.ok_button.setText(QCoreApplication.translate("MainWindow", u"\u62bd\u5956", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6682\u672a\u4e2d\u5956", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5df2\u4e2d\u5956", None))
    # retranslateUi

