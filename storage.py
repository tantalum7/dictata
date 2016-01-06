
# Library imports
from uuid               import uuid1

# Project imports
from persistent_dict    import PersistentDict
from note               import Note, CreateNoteDict


class NoteNotFoundError(Exception):
    pass


class Storage(object):

    TOP_PARENT  = 0

    def __init__(self):
        pass

    def open(self, file_dir):

        # Open db
        self.db = PersistentDict(file_dir, "c", format="json")

    def create_db(self, file_dir):

        # Create db
        self.db = PersistentDict(file_dir, "n", format="json")

        self.db['notes']    = {}
        self.db['folders']  = {}
        self.db['index']    = {}

    def sync(self):
        if self.db:
            self.db.sync()

    def get_note(self, uid):

        # If note exists, return it
        if uid in self.db['notes']:
            return Note( db = self.db['notes'][uid] )

        # Note not found, raise exception
        else:
            raise NoteNotFoundError

    def create_note(self):

        # Create new uid
        uid = self._create_uid()

        # Prepare empty notes dict
        note_dict = CreateNoteDict(uid)

        # Store new note in db
        self.db['notes'][uid] = note_dict

        # Get the note
        return self.get_note(uid)

    def rebuild_index(self):

        # Init index dict, with an empty top parent dict
        index = { self.TOP_PARENT : {} }

        # Create a copy of the folders dict in the db
        folders = self.db['folders'].copy()

        # Prepare list of folder uid's that have been indexed
        indexed_uids = []

        # Iterate while there are still items in the folders dict
        while len(indexed_uids) < len(folders.keys()):

            # Iterate through the folders
            for uid, folder in folders.items():

                # Grab parent name
                parent = folder['parent']

                # Check we haven't aready indexed this uid
                if uid not in indexed_uids:

                    # Is this folder's parent in the index yet?
                    key_path = self._find_keypath(dict=index, key=parent)
                    if key_path is not None:

                        # Start path at the top level
                        path = index

                        # Iterate through the key path list, and descend to the correct level
                        for key in key_path:
                            path = path[key]

                        # Store this folder in the path, and append the uid to the indexed list
                        path[uid] = {}
                        indexed_uids.append(uid)

        # Iterate through all the notes, and place into the index as required
        for note in self.db['notes'].values():

            # Find the note parent is in the index
            parent_keypath = self._find_keypath(index, note['parent'])

            # Check if we found a valid path to the parent
            if parent_keypath is not None:

                # Start path at the top level
                path = index

                # Iterate through the parent key path list, and descend to the correct level
                for key in parent_keypath:
                    path = path[key]

                # Store the note title, indexed by the note's uid
                path[note['uid']] = note['title']

            else:
                Exception("Can't find note's parent. UID: {}, Parent: {}".format(note['uid'], note['parent']) )

        # Return the rebuilt index dict
        return index

    def _create_uid(self):
        return uuid1().hex

    def _find_keypath(self, dict, key):

        # If the key is in the dict's top level, return the key
        if key in dict.keys():
            return [key]

        # Key is not in the dict's top level, iterate through the dict's subdicts
        else:
            for subkey, subdict in dict.items():

                # If the subdict is not empty, search for our target key in the subdict
                if subdict:
                    keypath = self._find_keypath(subdict, key)

                    # If we found a valid keypath, insert our subkey in front of the keypath and return it
                    if keypath is not None:
                        keypath.insert(0, subkey)
                        return keypath

            # If the code reaches here, then we failed to find the key. Return None.
            return None


    """
    db : { index    : {},
           folders  : { uid : { 'name'  : string,
                                'parent': uid
                              },
                      }
           notes    : { uid : { 'title' : string,
                                'parent': uid,
                                'tags'  : [string, string, string],
                                'body'  : string,
                                'meta'  : {}
                           },
                      },
           stuff    : {},
         }
    """


if __name__ == "__main__":


    sto = Storage()

    #sto.open("test.json")

    sto.create_db("test.json")

    sto.db['notes'] = {}

    sto.sync()

    n1 = sto.create_note()
    n1.title = "Emma snores"
    n1.body  = "She liek snores all night long."

    n2 = sto.create_note()
    n2.title = "Emma farts"
    n2.body  = "She farts, leik all day long."


    n3 = sto.create_note()
    n3.title = "Emma Smells"
    n3.body  = "Emma smells really, leik bad. Even after a shower."

    sto.sync()

    pass