
# Library imports


# Project imports
from storage    import Storage
from note       import Note, NoteList


class Dictata(object):

    def __init__(self):

        self.storage = Storage()
        self.storage.open("test.json")

        self.note_list = NoteList(self.storage)

        self.note_list.load_index()

        n = self.note_list.create_note()

        n.title = "Notes title"
        n.body  = "Main body of the thing"

        self.note_list.push_all()

        n.body = "second body"

        self.note_list.push_all()

        self.storage.sync()

        print("done")




if __name__ == "__main__":


    app = Dictata()

