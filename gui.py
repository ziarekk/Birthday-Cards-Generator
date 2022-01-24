from ui_mainMenu import Ui_MainMenu
from generatorWindow import GeneratorDialog
from PySide2.QtWidgets import QApplication, QMainWindow

import sys


class MainMenu(QMainWindow):
    """
    Class MainMenu is used to display window with stack:
    [0] - menu buttons and calendar
    [1] - author & credits
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
    """
    Main function - initializes Gui
    """
    app = QApplication(args)
    window = MainMenu()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
