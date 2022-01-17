from ui_generatorWindow import Ui_GeneratorWindow
from dialog import ShowingCardDialog
from PySide2.QtWidgets import QMainWindow
from generator import Person


class GeneratorDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GeneratorWindow()
        self.ui.setupUi(self)

        def func():
            person = Person(self.ui.nameEdit.text())
            self.close()
            self._showCard(person)

        self.ui.generateCard.clicked.connect(func)

    def _getPerson(self):
        person = Person(self.ui.nameEdit.text())
        return person

    def _showCard(self, person):
        self.win = ShowingCardDialog(person)
        self.win.show()
