from ui_generatorWindow import Ui_MainWindow
from ui_dailog import Ui_dialogWindow
from PySide2.QtWidgets import QApplication, QMainWindow
from generator import generate_Card, Person

import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def openCard():
            person = self.getPerson()
            self.OpenCardWindow(person)

        self.ui.generateCard.clicked.connect(openCard)

    def OpenCardWindow(self, person):
        self.window = QMainWindow()
        self.ui = Ui_dialogWindow()
        self.ui.setupUi(self.window)
        image = generate_Card(person)
        self.ui.imageViewer.setPixmap(image[1])
        self.window.show()

        def save():
            self.saveImg(image[0])

        def onClose():
            self.window = QMainWindow()
            self.ui = Ui_MainWindow()

        self.ui.closeTab.clicked.connect(onClose)
        self.ui.saveImage.clicked.connect(save)

    def OpenWindow(self, person):
        self.window = QMainWindow()
        self.ui = Ui_dialogWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def saveImg(self, image):
        image.save("BirthdayCard", "PNG")

    def getPerson(self):
        person = Person(self.ui.nameEdit.text())
        return person


def guiMain(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
