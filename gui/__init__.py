
from PyQt5 import QtWidgets, QtGui, QtCore
from qt.editor1 import Ui_MainWindow
import sys, traceback, time
from io import StringIO
from gui.treeview import TreeView
from gui.textarea import TextArea

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
        self._current_note = None

        self.treeview = TreeView(self.editor.notes_treeview)
        self.treeview.selection_callback = self._treeview_selection_callback


        self.textarea = TextArea(self.editor.body_textedit)
        self.tree_data_model = self.editor.notes_treeview.model()
        self.tree_selection_model = self.editor.notes_treeview.selectionModel()

        self.refresh_indextree()
        self.treeview.select(self.treeview.first)

        self.editor.notes_treeview.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.connect_callbacks()

        #self.open_note(note_index=self.tree_data_model.index(0, 0))



    @property
    def selected_note(self):
        return self.dictata.notes[self.treeview.selected.uid]

    @property
    def current_note(self):
        return self._current_note

    @current_note.setter
    def current_note(self, note):
        self._current_note = note

    def connect_callbacks(self):
        self.editor.notes_treeview.customContextMenuRequested.connect(self.contextMenuEvent)
        self.editor.notes_treeview.clicked.connect(self._clicked_notestreeview)
        self.editor.title_lineedit.textEdited.connect(self._changed_titlelineedit)
        self.editor.dbg1_button.clicked.connect(self.dbg1)
        self.editor.dbg2_button.clicked.connect(self.dbg2)

        # Text editor buttons
        self.editor.bold_button.clicked.connect(self.textarea.toggle_selected_bold)
        self.editor.italics_button.clicked.connect(self.textarea.toggle_selected_italics)
        self.editor.underline_button.clicked.connect(self.textarea.toggle_selected_underline)
        self.editor.strikethrough_button.clicked.connect(self.textarea.toggle_selected_strikethrough)
        self.editor.headings_button.clicked.connect(self.textarea.toggle_selected_heading)



    def dbg1(self):
        a = []
        doc = self.textarea._qtextedit.document()
        for i in range(doc.blockCount()):
            a.append(doc.findBlockByNumber(i).text())

        pass

    def dbg2(self):
        self.textarea.toggle_selected_underline()

    def _treeview_selection_callback(self):
        if self.treeview.has_selection():
            self.sync_current_note()
            self.open_note(self.treeview.selected.uid)

    def refresh_indextree(self):
        selection = self.treeview.selection
        item_list = [(note.title, note.uid) for note in self.dictata.notes.values()]
        self.treeview.repopulate(item_list)
        self.treeview.set_selection(selection)

    def _changed_titlelineedit(self):
        self.treeview.selected.title = self.editor.title_lineedit.text()
        self.current_note.title = self.editor.title_lineedit.text()

    def _clicked_deletebutton(self):
        uid_to_delete = self.selected_note.uid
        row = self.treeview.selected.row
        self.treeview.select(self.treeview.selected.previous)
        self.treeview.remove(row)
        del self.dictata.notes[uid_to_delete]

    def _clicked_notestreeview(self, index):
        uid = self.editor.notes_treeview.model().data(index, QtCore.Qt.UserRole)
        if uid:
            self.sync_current_note()
            self.open_note(uid)

    def sync_current_note(self):
        if self.current_note:
            self.current_note.title = self.editor.title_lineedit.text()
            self.current_note.body = self.editor.body_textedit.toPlainText()
            self.dictata.sync_storage()

    def open_note(self, note_uid=None, note_index=None):
        if note_uid:
            note = self.dictata.notes[note_uid]
        elif note_index:
            uid = self.editor.notes_treeview.model().data(note_index, QtCore.Qt.UserRole)
            note = self.dictata.note_list.notes[uid]
        else: return
        self.editor.title_lineedit.setText(note.title)
        self.editor.body_textedit.clear()
        self.editor.body_textedit.append(note.body)
        self.current_note = self.selected_note
        self.editor.created_label.setText("Created {}".format(note.creation_date))
        self.editor.lastedit_label.setText("Last edited {}".format(note.last_edit_date))

    def contextMenuEvent(self, cursor_position):
        row = self.editor.notes_treeview.indexAt(cursor_position)
        self.menu = QtWidgets.QMenu()
        action = self.menu.addAction("Delete note")
        action.setData("DELETE")
        #action
        self.menu.addAction("Insert new note")
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