
# Library imports
import collections

# Project imports
from storage import Storage
from storage.document import EncryptedDocument, Document
from storage.document_key import DocumentKey
from notes import Note, NoteIndex


class Dictata(object):

    def __init__(self, args, json_file):

        # Initialise storage
        self._storage = Storage()
        self._storage.open(json_file)
        self.doc_key = DocumentKey(plaintext_password="password")
        self.notes = NoteIndex(self._storage, self.doc_key)


    def create_note(self, title="", body="", tags="", parent=None):

        # Create the new note, and set title/data etc
        note = self.notes.create_note()
        note.title = title
        note.body = body
        note.tags = tags
        note.parent = parent

        # Return the note
        return note

    def sync_storage(self):
        self._storage.sync()

if __name__ == "__main__":


    app = Dictata()

