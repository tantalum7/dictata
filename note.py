
# Library imports
from hashlib        import md5
from time           import time
from datetime       import date


class NoteList(object):

    def __init__(self):
        self.notes = {}

    def load_from_storage(self):


class Note(object):

    def __init__(self, db):

        # Init class vars
        self._db    = db
        self._hash  = None
        self._uid   = self._db['uid']

    @property
    def hash(self):
        if self._hash is None:
            self._rehash()

        return self._hash

    @property
    def uid(self):
        return self._uid

    @property
    def title(self):
        return self._db['title']

    @title.setter
    def title(self, new_title):
        self._db['title']       = new_title
        self._hash              = None
        self._last_edit_time    = time()

    @property
    def body(self):
        return self._db['body']

    @body.setter
    def body(self, new_body):
        self._db['body']        = new_body
        self._hash              = None

    @property
    def tags(self):
        return self._db['tags']

    @tags.setter
    def tags(self, new_tags):
        self._db['tags']        = new_tags
        self._hash              = None

    @property
    def parent(self):
        return self._db['parent']

    @parent.setter
    def parent(self, new_parent):
        self._db['parent']      = new_parent
        self._hash              = None
        self._last_edit_date    = time()

    @property
    def creation_time(self):
        return self._db['creation_time']

    @property
    def creation_date(self):
        return date(self._db['creation_time'])

    @property
    def last_edit_time(self):
        return self._db['last_edit_time']

    @property
    def last_edit_date(self):
        return date(self._db['last_edit_time'])

    @property
    def meta(self):
        return self._db['meta']

    @meta.setter
    def meta(self, new_meta):
        self._db['meta']        = new_meta
        self._hash              = None
        self._last_edit_time    = time()

    def _rehash(self):
        self._hash = md5().new( ''.join( str(x) for x in self._db.values().sort() ) ).hexdigest()

def CreateNoteDict(uid):

    # Prepare dict
    note_dict = {}
    note_dict['uid']            = uid
    note_dict['title']          = None
    note_dict['body']           = None
    note_dict['tags']           = None
    note_dict['parent']         = 0
    note_dict['creation_time']  = time()
    note_dict['last_edit_time'] = None
    note_dict['meta']           = None
    note_dict['hash']           = None

    # Return note dict
    return note_dict

if __name__ == "__main__":

    n1 = Note()

    print(hash(n1))

    n1.title = "stuff"

    print(hash(n1))

