from ui_mainMenu import Ui_MainMenu
from generatorWindow import GeneratorDialog
from PySide2.QtWidgets import QApplication, QMainWindow

import sys


class MainMenu(QMainWindow):
    """
    MainMenu Window, displays stack:
    [page 0] shows main menu and calendar.
    [page 1] shows info about the author and credits
    MainMenu consits of 2 buttons:
        goCredits: changes stackIndex showing info about author&credits
        goGenerator: opens up window with iteractive Birthday Card Generator
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.stack.setCurrentIndex(0)

        self.ui.goCredits.clicked.connect(self._openCredits)
        self.ui.goGenerator.clicked.connect(self._openGenerator)
        self.ui.returnMenu.clicked.connect(self._returnToMainMenu)

    def _openCredits(self):
        """
        Changes stack, showing user author&credits
        """
        self.ui.stack.setCurrentIndex(1)

    def _returnToMainMenu(self):
        """
        Returns user back to main menu
        """
        self.ui.stack.setCurrentIndex(0)

    def _openGenerator(self):
        """
        Opens dialog window with generator
        """
        self.w = GeneratorDialog()
        self.w.show()


def guiMain(args):
    app = QApplication(args)
    window = MainMenu()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
