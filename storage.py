
# Library imports
from uuid               import uuid1

# Project imports
from backend            import StorageBackend
from note               import Note, CreateNoteDict


class NoteNotFoundError(Exception):
    pass


class Storage(object):

    def __init__(self):
        self._db = StorageBackend()

    def open(self, file_dir):
        self._db.open(file_dir)

    def put(self, object_id, object):
        self._db.put_object(object_id=object_id, object=object)

    def get(self, object_id):
        self._db.get_object(object_id)

    def close(self):
        self._db.close()