import random
from PyQt6 import QtWidgets

from main_gui import Ui_MainWindow

class Dice:
    def __init__(self, edges) -> None:
        self.edges = edges

    def roll(self) -> int:
        self.value = random.randint(1,self.edges)
        return self.value

class DiceGame:
    NUMBEROFDICES = 1
    DICEEDGENUMBER = 6
    def __init__(self) -> None:
        self.dices = [Dice(self.DICEEDGENUMBER) for _ in range(self.NUMBEROFDICES)]
    
    def start(self):
        self.result1 = 0
        self.scores1 = ''
        for dice in self.dices:
            res = dice.roll()
            self.result1 += res
            if(self.scores1 != ''):
                self.scores1 += (', ' + str(res))
            else:
                self.scores1 = str(res)

        self.result2 = 0
        self.scores2 = ''
        for dice in self.dices:
            res = dice.roll()
            self.result2 += res
            if(self.scores2 != ''):
                self.scores2 += (', ' + str(res))
            else:
                self.scores2 = str(res)
    
    def change_number_of_dices(self, dices_number):
        self.NUMBEROFDICES = dices_number
        self.__init__()

    def change_number_of_edges(self, edges_number):
        self.DICEEDGENUMBER = edges_number
        self.__init__()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.game = DiceGame()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_pushButton.clicked.connect(self.start_game)
        self.ui.restart_pushButton.clicked.connect(self.start_game)
        self.ui.settings_pushButton.clicked.connect(self.open_settings)

        self.ui.back_pushButton.clicked.connect(self.open_menu)
        self.ui.back_pushButton_1.clicked.connect(self.open_menu)

        self.show()

    def start_game(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.game.start()
        self.ui.lcdNumber.display(self.game.result1)
        self.ui.score_label.setText(self.game.scores1)
        self.ui.lcdNumber_2.display(self.game.result2)
        self.ui.score_label_2.setText(self.game.scores2)
        if(self.game.result1 > self.game.result2):
            self.ui.winner_label.setText("Player 1 wins!")
        elif(self.game.result1 < self.game.result2):
            self.ui.winner_label.setText("Player 2 wins!")
        else:   
             self.ui.winner_label.setText("Draw!")

    def open_menu(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def open_settings(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.diceNumberSpinBox.setValue(self.game.NUMBEROFDICES) 
        self.ui.edgeNumberSpinBox.setValue(self.game.DICEEDGENUMBER)

        self.ui.diceNumberSpinBox.valueChanged.connect(self.update_dice_number)
        self.ui.edgeNumberSpinBox.valueChanged.connect(self.update_edge_number)

    def update_dice_number(self, value):
        self.game.change_number_of_dices(value)

    def update_edge_number(self, value):
        self.game.change_number_of_edges(value)

if __name__ == "__main__":  
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





