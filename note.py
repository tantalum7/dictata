
# Library imports
from hashlib        import md5
from time           import time
from datetime       import date

# Project imports
from exceptions     import ObjectNotFoundException

class NoteList(object):
    INDEX_UID = "INDEX00".ljust(32, "#")

    def __init__(self, storage):
        self.notes      = {}
        self.index      = None
        self.storage    = storage

    def load_from_storage(self):
        pass

    def load_index(self):

        try:
            self.index = self.storage.get(self.INDEX_UID)

        except ObjectNotFoundException:
            self.create_index()

        except:
            raise
        self.populate_index()

    def populate_index(self):

        for uid in self.index.keys():
            self.notes[uid] = Note( uid=uid, data=self.storage.get(uid=uid) )

    def create_index(self):
        self.index = {}
        self.storage.put(uid=self.INDEX_UID, data=self.index)

    def add_to_index(self, note):
        self.index[note.uid] = note

    def push_index(self):
        self.storage.put(uid=self.INDEX_UID, data=self.index)

    def create_note(self):
        new_note = Note( uid=self.storage.uid() )
        self.storage.put(uid=new_note.uid, data=new_note.data)
        self.index[new_note.uid] = None
        self.notes[new_note.uid] = new_note


        return new_note

    def push_all(self):

        self.push_index()

        for note in self.notes.values():
            if note.hash != note.committed_hash:
                self.storage.put(uid=note.uid, data=note.data)
                note.committed_hash = note.hash

    def sync_all(self):
        self.storage.sync()



class Note(object):

    def __init__(self, uid, data=None):

        # Init class vars
        self._uid               = uid
        self._hash              = None
        self.committed_hash     = None

        if data:
            self.data = data
        else:
            self.data = {  'title'              : '',
                           'body'               : '',
                           'tags'               : '',
                           'parent'             : '',
                           'creation_time'      : time(),
                           'last_edit_time'     : time(),
                           'meta'               : '',
                         }

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
        return self.data['title']

    @title.setter
    def title(self, new_title):
        self.data['title']      = new_title
        self._hash              = None
        self._last_edit_time    = time()

    @property
    def body(self):
        return self.data['body']

    @body.setter
    def body(self, new_body):
        self.data['body']       = new_body
        self._hash              = None

    @property
    def tags(self):
        return self.data['tags']

    @tags.setter
    def tags(self, new_tags):
        self.data['tags']       = new_tags
        self._hash              = None

    @property
    def parent(self):
        return self.data['parent']

    @parent.setter
    def parent(self, new_parent):
        self.data['parent']     = new_parent
        self._hash              = None
        self._last_edit_date    = time()

    @property
    def creation_time(self):
        return self.data['creation_time']

    @property
    def creation_date(self):
        return date(self.data['creation_time'])

    @property
    def last_edit_time(self):
        return self.data['last_edit_time']

    @property
    def last_edit_date(self):
        return date(self.data['last_edit_time'])

    @property
    def meta(self):
        return self.data['meta']

    @meta.setter
    def meta(self, new_meta):
        self.data['meta']       = new_meta
        self._hash              = None
        self._last_edit_time    = time()

    def _rehash(self):
        m = md5()
        m.update( ''.join(str(self.data[x]) for x in sorted( list( self.data.keys() ) ) ).encode() )
        self._hash = m.hexdigest()

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

