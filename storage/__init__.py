
# Library imports
import uuid

# Project imports
from storage.local_json_backend import LocalJsonBackend
from storage.ftp_json_backend import FtpJsonBackend

# Define StorageBackend as localJsonBackend. TODO: Make backend selection programmatic
#StorageBackend = LocalJsonBackend
StorageBackend = FtpJsonBackend

class Storage:

    def __init__(self, settings: dict):
        """
        Thin wrapper class around the specific implementation of GenericBackend used
        :param settings:
        """
        self._backend = StorageBackend(settings=settings)

    def open(self):
        self._backend.open()

    def close(self, options=None):
        self._backend.close(options=options)

    def get(self, uid, key):
        return self._backend.get(uid=uid, key=key)

    def get_dict(self, uid):
        return self._backend.get_document(uid=uid)

    def put(self, uid, key, value):
        self._backend.put(uid=uid, key=key, value=value)

    def delete(self, uid, key):
        self._backend.delete(uid=uid, key=key)

    def delete_document(self, uid):
        self._backend.delete_document(uid=uid)

    def sync(self, options=None):
        self._backend.sync(options=options)

    def count(self, uid):
        return self._backend.count(uid=uid)

    def generate_uid(self):
        return uuid.uuid4().hex
