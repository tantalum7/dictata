
# Library imports
import uuid

# Project imports
from backend    import StorageBackend

class Storage(object):

    def __init__(self):
        self._db = StorageBackend()

    def open(self, path):
        return self._db.open(path)

    def close(self):
        return self._db.close()

    #TODO: Encrypt/decrypt the get/put methods into safe strings
    def get(self, uid):
        return self._db.get(uid)

    def put(self, uid, data):
        return self._db.put(uid=uid, data=data)

    def sync(self):
        return self._db.sync()

    def uid(self):
        return uuid.uuid4().hex