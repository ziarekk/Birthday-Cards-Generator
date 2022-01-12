from ui_generatorWindow import Ui_MainWindow
from ui_dailog import Ui_dialogWindow
from PySide2.QtWidgets import QApplication, QMainWindow
from generator import generate_Card

import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.generateCard.clicked.connect(self.OpenCardWindow)

    def OpenCardWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_dialogWindow()
        self.ui.setupUi(self.window)
        image = generate_Card()
        self.ui.imageViewer.setPixmap(image[1])
        self.window.show()

        def save():
            self.saveImg(image[0])

        self.ui.closeTab.clicked.connect(self.window.close)
        self.ui.saveImage.clicked.connect(save)

    def saveImg(self, image):
        image.save("BirthdayCard", "PNG")


def guiMain(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
