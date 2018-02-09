
from PyQt5 import QtWidgets, QtGui, QtCore
from qt.editor1 import Ui_MainWindow
import sys

class Editor(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.show()

        #self.notes_treeview.clicked.connect(self.myclicked)



    def myclicked(self, index):
        display_data = self.notes_treeview.model().data(index, QtCore.Qt.DisplayRole)
        secret_data = self.notes_treeview.model().data(index, QtCore.Qt.UserRole)
        print("clicked: {0}, {1}".format(display_data, secret_data))


class GUI(QtWidgets.QApplication):

    def __init__(self, args, dictata):
        QtWidgets.QApplication.__init__(self, args)
        self.editor = Editor()
        self.dictata = dictata
        self.current_note = None

        self.editor.notes_treeview.clicked.connect(self.click_treeview)
        self.editor.sync_button.clicked.connect(self.click_syncbutton)
        self.editor.delete_button.clicked.connect(self.click_deletebutton)

        self.refresh_indextree()

    def refresh_indextree(self):
        tree_model = self.editor.notes_treeview.model()
        tree_model.removeRows(0, tree_model.rowCount())
        for row, note in enumerate(self.dictata.note_list.notes.values()):
            tree_model.insertRow(row)
            self.setTreeData(row, 0, note.title, note.uid)
        row = tree_model.rowCount()
        tree_model.insertRow(row)
        self.setTreeData(row, 0, "Add new note", "NEW NOTE")

    def click_syncbutton(self):
        self.current_note.title = self.editor.title_lineedit.text()
        self.current_note.body = self.editor.body_textedit.toPlainText()
        self.dictata.storage.sync()
        self.refresh_indextree()

    def click_deletebutton(self):
        self.dictata.note_list.delete(self.current_note.uid)
        self.refresh_indextree()

    def click_treeview(self, index):
        uid = self.editor.notes_treeview.model().data(index, QtCore.Qt.UserRole)
        self.open_note(uid)

    def setTreeData(self, row, col, display_data, user_data):
        tree_model = self.editor.notes_treeview.model()
        tree_model.setData(tree_model.index(row, col), display_data, QtCore.Qt.DisplayRole)
        tree_model.setData(tree_model.index(row, col), user_data, QtCore.Qt.UserRole)

    def open_note(self, note_uid):
        self.current_note = self.dictata.note_list.notes[note_uid]
        self.editor.title_lineedit.setText(self.current_note.title)
        self.editor.body_textedit.clear()
        self.editor.body_textedit.append(self.current_note.body)


    def show(self):
        self.editor.show()

    def run(self):
        return self.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()