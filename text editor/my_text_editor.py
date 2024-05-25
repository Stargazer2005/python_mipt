from PyQt6 import QtWidgets, QtCore, QtGui
from text_ui import Ui_MainWindow

import pathlib


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bold = False
        self.curve = False
        self.underline = False

        self.path = pathlib.Path.cwd()
        self.name = "Untitled.html"

        self.ui.left_pushButton.clicked.connect(lambda: self.ui.textEdit.setAlignment(
                                                QtCore.Qt.AlignmentFlag.AlignLeft))
        self.ui.right_pushButton.clicked.connect(lambda: self.ui.textEdit.setAlignment(
                                                 QtCore.Qt.AlignmentFlag.AlignRight))
        self.ui.center_pushButton.clicked.connect(lambda: self.ui.textEdit.setAlignment(
                                                  QtCore.Qt.AlignmentFlag.AlignCenter))
        self.ui.justify_pushButton.clicked.connect(lambda: self.ui.textEdit.setAlignment(
                                                   QtCore.Qt.AlignmentFlag.AlignJustify))
        
        self.ui.bold_pushButton.setCheckable(True)
        self.ui.curve_pushButton.setCheckable(True)
        self.ui.ess_pushButton.setCheckable(True)

        self.ui.bold_pushButton.toggled.connect(lambda x: self.ui.textEdit.setFontWeight(QtGui.QFont.Weight.Bold if x
                                                                                         else QtGui.QFont.Weight.Normal))
        self.ui.curve_pushButton.toggled.connect(self.ui.textEdit.setFontItalic)
        self.ui.ess_pushButton.toggled.connect(self.ui.textEdit.setFontUnderline)

        self.ui.font.currentFontChanged.connect(self.ui.textEdit.setCurrentFont)
        self.ui.comboBox.currentIndexChanged.connect(lambda x: self.ui.textEdit.setFontPointSize(int(x)))

        self.ui.actionNew.triggered.connect(self.new_file)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_as.triggered.connect(self.save_file_as)

    
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if not self.maybe_save_changes_dialog():
            a0.ignore()
        else:
            a0.accept()

    def save_file_as(self):
        file_filter = "Text file (*.txt);; Word file (*.doc, *.docx);; Html file (*.html)"
        response = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            directory=str(self.path),
            caption="Save file as",
            filter=file_filter,
            initialFilter='Html file (*.html)'
        )
        
        if response[0] != '':
            self.path = pathlib.Path(response[0])
            self.name = self.path.name
            self.path = pathlib.Path(str(self.path)[:-len(self.name):])
            if self.save_file():  # Check if the file was successfully saved
                self.setWindowTitle(self.path.name)

    def save_file(self):
        text = self.ui.textEdit.toPlainText()
        try:
            with open(str(self.path /self.name) , 'w') as f:
                f.write(text)
                f.close()
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False

    def new_file(self):
        if not self.maybe_save_changes_dialog():
            return

        file_count = sum(1 for item in self.path.iterdir() if item.is_file() and item.name.startswith("Untitled"))
        self.name = f"Untitled ({file_count}).html"
        self.ui.textEdit.clear()
        self.setWindowTitle(self.name)

    def open_file(self):
        if not self.maybe_save_changes_dialog():
            return
            
        file_filter = "Text file (*.txt);; Word file (*.doc, *.docx);; Html file (*.html)"

        response =  QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            directory= str(pathlib.Path.cwd()),
            caption="Select file",
            filter=file_filter,
            initialFilter= 'Html file (*.html)'
        )

        if response[0] != '':
            self.path = pathlib.Path(response[0])
            self.name = self.path.name
            self.path = pathlib.Path(str(self.path)[:-len(self.name):])
            text = open(response[0]).read()
            self.ui.textEdit.setPlainText(text)

            self.setWindowTitle(self.path.name)

    def maybe_save_changes_dialog(self):
        if (self.path / self.name).exists() and open(self.path / self.name).read() == self.ui.textEdit.toPlainText():
            return True
    
        message = QtWidgets.QMessageBox.question(self, "Choose message",
                                                f"Do you want to save changes to {self.name}?",
                                                (QtWidgets.QMessageBox.StandardButton.Yes |
                                                QtWidgets.QMessageBox.StandardButton.No |
                                                QtWidgets.QMessageBox.StandardButton.Cancel),
                                                QtWidgets.QMessageBox.StandardButton.Cancel)

        if message == QtWidgets.QMessageBox.StandardButton.Yes:
            self.save_file()
            return True
        elif message == QtWidgets.QMessageBox.StandardButton.No:
            return True
        else:
            return False
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
