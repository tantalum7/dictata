
# Library imports
import shelve
import collections

# Project imports
from persistent_dict    import PersistentDict
from note               import Note

class Storage(object):

    TOP_PARENT  = 0

    def __init__(self):
        pass

    def open(self, file_dir):

        # Open db
        self.db = PersistentDict("file_dir", "c", format="json")

    def sync(self):
        if self.db:
            self.db.sync()

    def get_note(self, uid):

        # If note exists, return it
        if uid in self.db['notes']:
            return Note(seed_dict=self.db['notes'][uid])

    def create_note(self):
        pass

    def rebuild_index(self):

        # Init index dict
        index = {}

        # Create a copy of the folders dict in the db
        #folders = self.db['folders'].copy()
        folders = { 100 : {'parent' : 0},
                    200 : {'parent' : 0},
                    300 : {'parent' : 0},
                    110 : {'parent' : 100},
                    111 : {'parent' : 110},
                    210 : {'parent' : 200},
                    211 : {'parent' : 210},
                    310 : {'parent' : 300},
                  }

        # Prepare list of folder uid's that have been indexed
        indexed_uids = []

        # Iterate while there are still items in the folders dict
        while len(indexed_uids) < len(folders.keys()):

            # Iterate through the folders
            for uid, folder in folders.items():

                # Grab parent name
                parent = folder['parent']

                if uid not in indexed_uids:

                    # If this a top level folder, store at the top index level and add to the indexed list
                    if parent == self.TOP_PARENT:
                        index[uid] = {}
                        indexed_uids.append(uid)

                    # This is not a top level folder
                    else:
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

        # Return the rebuilt index dict
        return index

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
    db : { index : {},
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

    print sto.rebuild_index()

    pass