from ui_generatorWindow import Ui_GeneratorWindow
from dialog import ShowingCardDialog
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QMainWindow, QMessageBox
from generator import Person


class GeneratorDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GeneratorWindow()
        self.ui.setupUi(self)
        regexp = QRegExpValidator(QRegExp(r'^[a-zA-Z]*$'))
        self.ui.nameEdit.setValidator(regexp)

        def func():
            if self.ui.nameEdit.text():
                person = Person(self.ui.nameEdit.text())
                self.close()
                self._showCard(person)
            else:
                self.showMessage()

        self.ui.generateCard.clicked.connect(func)

    def showMessage(self):
        QMessageBox.about(self, "Alert", "Input name before generating card.")

    def _getPerson(self):
        person = Person(self.ui.nameEdit.text())
        return person

    def _showCard(self, person):
        self.win = ShowingCardDialog(person)
        self.win.show()
