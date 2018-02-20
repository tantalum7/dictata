
# Project imports
from storage import Storage
from storage.document_key import DocumentKey

class Document:

    def __init__(self, storage: Storage, uid: str):
        """
        This is a dict like storage class that maps arbitrary key strings with value strings.
        The values aren't stored in the class, the object is a wrapper for accessing through a Storage object
        :param storage:
        :param uid:
        """
        self._storage = storage
        self._uid = uid

    @property
    def uid(self) -> str:
        return self._uid

    def __getitem__(self, key: str) -> str:
        return self._storage.get(self._uid, str(key))

    def __setitem__(self, key: str, value: str):
        self._storage.put(self._uid, key, str(value))

    def __delitem__(self, key: str):
        self._storage.delete(self.uid, key)

    def __iter__(self):
        raise NotImplemented

    def __len__(self):
        return self._storage.count(self.uid)

    def values(self) -> [str]:
        return self._storage.get_dict(self._uid).values()

    def keys(self) -> [str]:
        return self._storage.get_dict(self._uid).keys()

    def items(self) -> [(str, str)]:
        return self._storage.get_dict(self._uid).items()


class EncryptedDocument(Document):

    def __init__(self, storage: Storage, uid: str, doc_key: DocumentKey):
        """
        Encrypted variant of Document. Inserts an encrypt/decrypt stage in set/get
        :param storage:
        :param uid:
        :param doc_key:
        """
        super(EncryptedDocument, self).__init__(storage=storage, uid=uid)
        self._doc_key = doc_key

    def __getitem__(self, key: str) -> str:
        return self._doc_key.decrypt(self._storage.get(self._uid, str(key)))

    def __setitem__(self, key: str, value: str):
        self._storage.put(self._uid, key, self._doc_key.encrypt(str(value)))
