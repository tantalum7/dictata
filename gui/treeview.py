
from PyQt5 import QtWidgets, QtGui, QtCore

class TreeView:

    """
    TODO: Only works as a flat list (column = 0). Implement hierarchy support
    """
    class Item:
        def __init__(self, treeview, qIndex):
            self._treeview = treeview
            self.index = qIndex

        @property
        def title(self):
            return self._treeview._data_model.data(self.index, QtCore.Qt.DisplayRole)

        @title.setter
        def title(self, new_title):
            self._treeview._data_model.setData(self.index, new_title, QtCore.Qt.DisplayRole)

        @property
        def uid(self):
            return self._treeview._data_model.data(self.index, QtCore.Qt.UserRole)

        @uid.setter
        def uid(self, new_uid):
            self._treeview._data_model.setData(self.index, new_uid, QtCore.Qt.UserRole)

        @property
        def row(self):
            return self.index.row()

        @property
        def column(self):
            return self.index.column()

        @property
        def previous(self):
            """
            Returns the item before this one in the treeview order
            :return:
            """
            return self._treeview.get(row=self.row - 1)

    def __init__(self, qt_treeview):
        self._treeview = qt_treeview
        self._data_model = qt_treeview.model()
        self._selection_model = qt_treeview.selectionModel()
        self.selection_callback = None
        self._selection_model.selectionChanged.connect(
            lambda: self.selection_callback() if callable(self.selection_callback) else None
        )

    def get(self, row):
        """
        Returns the item at the given row
        :param row:
        :param col:
        :return:
        """
        return self.Item(self, self._data_model.index(row, 0))

    def find(self, uid=None, name=None):
        """
        Returns a list of items that match the uid or the name. Returns none if no uid or name is passed
        :param uid:
        :param name:
        :return:
        """
        # Search by uid
        if uid:
            index_list = self._data_model.match(start=self._data_model.index(0,0),
                                                role=QtCore.Qt.UserRole, value=uid )
        # Search by name
        elif name:
            index_list = self._data_model.match(start=self._data_model.index(0, 0),
                                                role=QtCore.Qt.DisplayRole, value=name)
        # No search parameter passed, return none
        else: return

        # Return matches as a list of items
        return [self.Item(self, index) for index in index_list]

    @property
    def first(self):
        """
        Wrapped for self.get(0). Will throw exception if there treeview is empty
        :return:
        """
        return self.get(0)

    @property
    def selection(self):
        """
        Returns a list of selected items
        :return:
        """
        index_list = self._selection_model.selectedIndexes()
        return [self.Item(self, index) for index in index_list]

    @property
    def selected(self):
        """
        Returns the first of the list of selected items (ignores multiple selections)
        :return:
        """
        return self.selection[0]

    def select(self, item):
        """
        Clears the current selection, then selects the item passed
        :param item:
        :return:
        """
        self.clear_selection()
        self._selection_model.select(item.index, self._selection_model.Select)

    def append_select(self, item):
        """
        Appends the item passed to the selection list, instead of clearing it like self.select()
        :param item:
        :return:
        """
        self._selection_model.select(item.index, self._selection_model.Select)

    def set_selection(self, item_list):
        """
        Clears the current selection, and then sets it to the item list provided
        :param item_list:
        :return:
        """
        self.clear_selection()
        for item in item_list:
            self._selection_model.select(item.index, self._selection_model.Select)

    def clear_selection(self):
        """
        Clear current selection
        :return:
        """
        self._selection_model.clear()

    def has_selection(self):
        """
        Returns true if at least one item is selected
        :return:
        """
        return bool(self.selection)

    def clear(self):
        """
        Clears the entire treeview of all items
        :return:
        """
        self._data_model.removeRows(0, self._data_model.rowCount())

    def insert(self, row, name, uid):
        """
        Inserts an item into the treeview and the row given
        :param row:
        :param name:
        :param uid:
        :return:
        """
        self._data_model.insertRow(row)
        self._data_model.setData(self._data_model.index(row, 0), name, QtCore.Qt.DisplayRole)
        self._data_model.setData(self._data_model.index(row, 0), uid, QtCore.Qt.UserRole)

    def append(self, name, uid):
        """
        Appends an item to the end of the treeview
        :param name:
        :param uid:
        :return:
        """
        self.insert(row=self._data_model.rowCount(), name=name, uid=uid)

    def remove(self, row):
        """
        Removes the row number passed
        :param row:
        :return:
        """
        self._data_model.removeRow(row)

    def populate(self, items):
        """
        Takes a list of tuples [ (item name, item uid), ... ] and adds them to the treeview in order
        :param items:
        :return:
        """
        for name, uid in items:
            self.append(name, uid)

    def repopulate(self, items):
        """
        Wrapper function clears before doing a populate
        :param items:
        :return:
        """
        self.clear()
        self.populate(items)