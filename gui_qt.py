
from PyQt5 import QtWidgets, QtGui
from test_ui import Ui_MainWindow
import sys

class Editor(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()