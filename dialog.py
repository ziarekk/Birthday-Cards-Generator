from ui_dialog import Ui_dialogWindow
from PySide2.QtWidgets import QMainWindow, QMessageBox

from generator import generate_Card


class ShowingCardDialog(QMainWindow):
    """
    Class ShowingCardDialog.
    It is responisble for generating and showing birthday card.
    """
    def __init__(self, person, parent=None):
        super().__init__(parent)
        self.ui = Ui_dialogWindow()
        self.ui.setupUi(self)
        image = generate_Card(person)
        self.ui.imageViewer.setPixmap(image[1])

        def saveImage():
            """
            Saves generated card as BirthdayCard.png
            """
            image[0].save("BirthdayCard", "PNG")
            QMessageBox.about(self, "Image Saved",
                                    "Image has been saved as BirthdayCard.png")

        self.ui.closeTab.clicked.connect(self.close)
        self.ui.saveImage.clicked.connect(saveImage)
