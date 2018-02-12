
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

        self.sync_timer = QtCore.QTimer()
        self.sync_timer.start(5000)
        self.sync_timer.timeout.connect(self._sync_timercallback)

        self.tree_model = self.editor.notes_treeview.model()

        self.refresh_indextree()

        self.editor.notes_treeview.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.connect_callbacks()

        self.open_note(note_index=self.tree_model.index(0, 0))

    def connect_callbacks(self):

        self.editor.delete_button.clicked.connect(self._click_deletebutton)
        self.sync_timer.timeout.connect(self._sync_timercallback)
        self.editor.notes_treeview.customContextMenuRequested.connect(self.contextMenuEvent)
        self.editor.notes_treeview.clicked.connect(self._click_notestreeview)
        self.editor.title_lineedit.textChanged.connect(self.refresh_indextree)

    def _sync_timercallback(self):
        if self.editor.body_textedit.document().isModified():
            self.editor.body_textedit.document().setModified(False)
            self.current_note.body = self.editor.body_textedit.toPlainText()
            self.dictata.storage.sync()

    def refresh_indextree(self):
        if self.current_note:
            self.current_note.title = self.editor.title_lineedit.text()
        self.tree_model.removeRows(0, self.tree_model.rowCount())
        for row, note in enumerate(self.dictata.note_list.notes.values()):
            self.tree_model.insertRow(row)
            self.setTreeData(row, 0, note.title, note.uid)
        row = self.tree_model.rowCount()
        self.tree_model.insertRow(row)
        self.setTreeData(row, 0, "+", "")

    def _click_deletebutton(self):
        #self.open_note(self.editor.notes_treeview.indexAbove()
        self.dictata.note_list.delete(self.current_note.uid)
        self.refresh_indextree()

    def _click_notestreeview(self, index):
        uid = self.editor.notes_treeview.model().data(index, QtCore.Qt.UserRole)
        if uid:
            self.sync_current_note()
            self.open_note(uid)

    def sync_current_note(self):
        if self.current_note:
            self.current_note.title = self.editor.title_lineedit.text()
            self.current_note.body = self.editor.body_textedit.toPlainText()
            self.dictata.storage.sync()

    def setTreeData(self, row, col, display_data, user_data):
        tree_model = self.editor.notes_treeview.model()
        tree_model.setData(tree_model.index(row, col), display_data, QtCore.Qt.DisplayRole)
        tree_model.setData(tree_model.index(row, col), user_data, QtCore.Qt.UserRole)

    def open_note(self, note_uid=None, note_index=None):
        if note_uid:
            self.current_note = self.dictata.note_list.notes[note_uid]
        elif note_index:
            uid = self.editor.notes_treeview.model().data(note_index, QtCore.Qt.UserRole)
            self.current_note = self.dictata.note_list.notes[uid]

        self.editor.title_lineedit.setText(self.current_note.title)
        self.editor.body_textedit.clear()
        self.editor.body_textedit.append(self.current_note.body)

    def contextMenuEvent(self, cursor_position):
        row = self.editor.notes_treeview.indexAt(cursor_position)
        self.menu = QtWidgets.QMenu()
        action = self.menu.addAction("Delete note")
        action.setData("DELETE")
        #action
        self.menu.addAction("Insert new note", )
        self.menu.addAction("Duplicate note")
        self.menu.triggered.connect(self.pop)
        self.menu.exec(self.editor.notes_treeview.mapToGlobal(cursor_position))
        pass

    def pop(self, action):
        t = action.text()
        d = action.data()
        pass

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