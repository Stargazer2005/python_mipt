# Form implementation generated from reading ui file 'text editor/text.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 669)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.font = QtWidgets.QFontComboBox(parent=self.centralwidget)
        self.font.setObjectName("font")
        self.horizontalLayout.addWidget(self.font)
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.bold_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bold_pushButton.sizePolicy().hasHeightForWidth())
        self.bold_pushButton.setSizePolicy(sizePolicy)
        self.bold_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.bold_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./text editor/images/edit-bold.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bold_pushButton.setIcon(icon)
        self.bold_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.bold_pushButton.setObjectName("bold_pushButton")
        self.horizontalLayout.addWidget(self.bold_pushButton)
        self.curve_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curve_pushButton.sizePolicy().hasHeightForWidth())
        self.curve_pushButton.setSizePolicy(sizePolicy)
        self.curve_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.curve_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./text editor/images/edit-italic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.curve_pushButton.setIcon(icon1)
        self.curve_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.curve_pushButton.setObjectName("curve_pushButton")
        self.horizontalLayout.addWidget(self.curve_pushButton)
        self.ess_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ess_pushButton.sizePolicy().hasHeightForWidth())
        self.ess_pushButton.setSizePolicy(sizePolicy)
        self.ess_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.ess_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./text editor/images/edit-underline.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ess_pushButton.setIcon(icon2)
        self.ess_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.ess_pushButton.setObjectName("ess_pushButton")
        self.horizontalLayout.addWidget(self.ess_pushButton)
        self.left_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_pushButton.sizePolicy().hasHeightForWidth())
        self.left_pushButton.setSizePolicy(sizePolicy)
        self.left_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.left_pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./text editor/images/edit-alignment.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.left_pushButton.setIcon(icon3)
        self.left_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.left_pushButton.setObjectName("left_pushButton")
        self.horizontalLayout.addWidget(self.left_pushButton)
        self.center_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_pushButton.sizePolicy().hasHeightForWidth())
        self.center_pushButton.setSizePolicy(sizePolicy)
        self.center_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.center_pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./text editor/images/edit-alignment-center.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.center_pushButton.setIcon(icon4)
        self.center_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.center_pushButton.setObjectName("center_pushButton")
        self.horizontalLayout.addWidget(self.center_pushButton)
        self.right_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_pushButton.sizePolicy().hasHeightForWidth())
        self.right_pushButton.setSizePolicy(sizePolicy)
        self.right_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.right_pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./text editor/images/edit-alignment-right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.right_pushButton.setIcon(icon5)
        self.right_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.right_pushButton.setObjectName("right_pushButton")
        self.horizontalLayout.addWidget(self.right_pushButton)
        self.justify_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.justify_pushButton.sizePolicy().hasHeightForWidth())
        self.justify_pushButton.setSizePolicy(sizePolicy)
        self.justify_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.justify_pushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./text editor/images/edit-alignment-justify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.justify_pushButton.setIcon(icon6)
        self.justify_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.justify_pushButton.setObjectName("justify_pushButton")
        self.horizontalLayout.addWidget(self.justify_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(parent=MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "4"))
        self.comboBox.setItemText(3, _translate("MainWindow", "6"))
        self.comboBox.setItemText(4, _translate("MainWindow", "10"))
        self.comboBox.setItemText(5, _translate("MainWindow", "12"))
        self.comboBox.setItemText(6, _translate("MainWindow", "14"))
        self.comboBox.setItemText(7, _translate("MainWindow", "16"))
        self.comboBox.setItemText(8, _translate("MainWindow", "20"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
