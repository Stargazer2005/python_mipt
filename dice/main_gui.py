# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 527)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_pushButton = QtWidgets.QPushButton(parent=self.page)
        self.start_pushButton.setObjectName("start_pushButton")
        self.verticalLayout.addWidget(self.start_pushButton)
        self.settings_pushButton = QtWidgets.QPushButton(parent=self.page)
        self.settings_pushButton.setObjectName("settings_pushButton")
        self.verticalLayout.addWidget(self.settings_pushButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.page_2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_5.addWidget(self.lcdNumber, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.page_2)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 2, 1, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(parent=self.page_2)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_5.addWidget(self.lcdNumber_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.page_2)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.page_2)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.score_label_2 = QtWidgets.QLabel(parent=self.page_2)
        self.score_label_2.setText("")
        self.score_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_label_2.setObjectName("score_label_2")
        self.gridLayout_5.addWidget(self.score_label_2, 3, 1, 1, 1)
        self.score_label = QtWidgets.QLabel(parent=self.page_2)
        self.score_label.setText("")
        self.score_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_label.setObjectName("score_label")
        self.gridLayout_5.addWidget(self.score_label, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.winner_label = QtWidgets.QLabel(parent=self.page_2)
        self.winner_label.setText("")
        self.winner_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.winner_label.setObjectName("winner_label")
        self.verticalLayout_2.addWidget(self.winner_label)
        self.restart_pushButton = QtWidgets.QPushButton(parent=self.page_2)
        self.restart_pushButton.setObjectName("restart_pushButton")
        self.verticalLayout_2.addWidget(self.restart_pushButton)
        self.back_pushButton = QtWidgets.QPushButton(parent=self.page_2)
        self.back_pushButton.setObjectName("back_pushButton")
        self.verticalLayout_2.addWidget(self.back_pushButton)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.page_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.edgeNumberSpinBox = QtWidgets.QSpinBox(parent=self.page_3)
        self.edgeNumberSpinBox.setMinimum(2)
        self.edgeNumberSpinBox.setMaximum(16)
        self.edgeNumberSpinBox.setObjectName("edgeNumberSpinBox")
        self.verticalLayout_3.addWidget(self.edgeNumberSpinBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.page_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.diceNumberSpinBox = QtWidgets.QSpinBox(parent=self.page_3)
        self.diceNumberSpinBox.setMinimum(1)
        self.diceNumberSpinBox.setMaximum(20)
        self.diceNumberSpinBox.setObjectName("diceNumberSpinBox")
        self.verticalLayout_3.addWidget(self.diceNumberSpinBox)
        self.back_pushButton_1 = QtWidgets.QPushButton(parent=self.page_3)
        self.back_pushButton_1.setObjectName("back_pushButton_1")
        self.verticalLayout_3.addWidget(self.back_pushButton_1)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_pushButton.setText(_translate("MainWindow", "Start Game"))
        self.settings_pushButton.setText(_translate("MainWindow", "Settings"))
        self.label_2.setText(_translate("MainWindow", "Player 2:"))
        self.label_4.setText(_translate("MainWindow", "Scores:"))
        self.label_3.setText(_translate("MainWindow", "Scores:"))
        self.label.setText(_translate("MainWindow", "Player 1:"))
        self.restart_pushButton.setText(_translate("MainWindow", "Restart"))
        self.back_pushButton.setText(_translate("MainWindow", "Back"))
        self.lineEdit.setText(_translate("MainWindow", "Dice edge number:"))
        self.lineEdit_2.setText(_translate("MainWindow", "Number of dices:"))
        self.back_pushButton_1.setText(_translate("MainWindow", "Back"))