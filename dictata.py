
# Library imports


# Project imports
from storage    import Storage
from note       import Note, NoteList


class Dictata(object):

    def __init__(self):

        self.storage = Storage()
        self.storage.open("test.json")

        self.note_list = NoteList()

