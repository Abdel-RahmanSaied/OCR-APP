import pyttsx3
from PyQt5 import QtWidgets , QtCore , QtGui
from views import main_view
import pytesseract


class MainManager(QtWidgets.QWidget, main_view.Ui_Form):
    # checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(MainManager, self).__init__()
        self.setupUi(self)

    def getfiles(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '', 'Images (*.png, *.jpeg , *.jpg) ')


        self.PathTextBox_2.setText("")
        self.PathTextBox_2.setPixmap(QtGui.QPixmap(self.fileName))

        #self.PathTextBox_2.setText(self.fileName)


    def readFimage(self):
        path = self.fileName

        if path:
            im = Image.open(path)
            text = pytesseract.image_to_string(im, lang='eng')

            self.ResultTextBox_2.setText("")
            self.ResultTextBox_2.setText(text)
            #Fun.append(text)

        else:
            self.ResultTextBox_2.setText("")
            self.ResultTextBox_2.setText("FILE CANNOT BE READ")

    def read(self):
        text = "".join(text)

        engine = pyttsx3.init()
        voices = engine.getProperty("voices")

        engine.setProperty("rate", 150)
        engine.setProperty("voice", voices[1].id)
        engine.say(text)
        engine.runAndWait()


if __name__ == "__main__":
    #import qdarkstyle

    app = QtWidgets.QApplication([])
    w = MainManager()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()