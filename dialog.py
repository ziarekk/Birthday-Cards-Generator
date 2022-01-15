from ui_dailog import Ui_dialogWindow
from PySide2.QtWidgets import QDialog

from generator import generate_Card


class ReceiptDialog(QDialog):
    def __init__(self, person, parent=None):
        super().__init__(parent)
        self.ui = Ui_dialogWindow()
        self.ui.setupUi(self)
        image = generate_Card(person)
        self.ui.imageViewer.setPixmap(image[1])
        self.window.show()

        def save():
            self.saveImg(image[0])

        def onClose():
            self.window.close()
            self.__init__()

        self.ui.closeTab.clicked.connect(onClose)
        self.ui.saveImage.clicked.connect(save)
