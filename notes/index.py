
# Project imports
from notes import Note
from storage.document import Document, EncryptedDocument
from storage import Storage
from storage.document_key import DocumentKey


class NoteIndex:

    INDEX_UID = "INDEX00#########################"

    def __init__(self, storage: Storage, doc_key: DocumentKey):
        """
        This class provides dict like access to the notes in storage, indexed by uid.
        Creating/deleting of notes must be done through this class, as it keeps the index updated.

        Use like a regular dict, except you can't use __setitem__
        :param storage:
        :param doc_key:
        """
        self._storage = storage
        self._document = Document(storage=self._storage, uid=self.INDEX_UID)
        self._doc_key = doc_key

    def __getitem__(self, uid: str) -> Note:
        if uid not in self.keys():
            raise KeyError

        return Note(EncryptedDocument(storage=self._storage, uid=uid, doc_key=self._doc_key))

    def __delitem__(self, uid: str):
        if uid not in self.keys():
            raise KeyError

        del self._document[uid]

    def __len__(self):
        return len(self._document)

    def create_note(self):
        """
        Creates a new note with a random uid, inserts it into the index and returns it
        :return:
        """

        # Create new empty document at a new uid
        doc = EncryptedDocument(self._storage, self._storage.generate_uid())

        # Push note into index
        self._document[doc.uid] = None

        # Create a note instance to wrap the document, and return it
        return Note(doc, new=True)

    def values(self):
        return [self.__getitem__(uid) for uid in self._document.keys()]

    def keys(self) -> list:
        return self._document.keys()

    def items(self) -> [tuple]:
        return dict(zip(self.keys(), self.values()))