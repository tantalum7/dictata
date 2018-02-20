
# Library imports
import pickle, json, csv, os, shutil, uuid

# Project imports
from storage.generic_backend import GenericBackend
from exceptions import StorageOpenException, DocumentNotFoundException

class LocalJsonBackend(GenericBackend):

    def initialise(self, settings):
        self._db = None

    def open(self, path):
        try:
            self._db = _PersistentDict(filename=path, format='json')

        except ValueError as detail:
            raise StorageOpenException(detail)

    def close(self, options=None):
        self.sync()
        self._db.close()
        self._db = None

    def get(self, uid, key):
        try:
            obj = self._db[uid]

        except KeyError:
            raise DocumentNotFoundException

        else:
            return obj.get(key, None)

    def get_document(self, uid):
        try:
            obj = self._db[uid]

        except KeyError:
            raise DocumentNotFoundException

        else:
            return obj

    def delete_document(self, uid):
        try:
            obj = self._db[uid]

        except KeyError:
            raise DocumentNotFoundException

        else:
            del self._db[uid]

    def put(self, uid, key, value):
        if not self._db[uid]:
            self._db[uid] = {}

        self._db[uid][key] = value

    def sync(self, options=None):
        self._db.sync()

    def count(self, uid):
        return len(self._db[uid]) if self._db[uid] else 0





class _PersistentDict(dict):
    ''' Persistent dictionary with an API compatible with shelve and anydbm.

    The dict is kept in memory, so the dictionary operations run as fast as
    a regular dictionary.

    Write to disk is delayed until close or sync (similar to gdbm's fast mode).

    Input file format is automatically discovered.
    Output file format is selectable between pickle, json, and csv.
    All three serialization formats are backed by fast C implementations.

    '''

    def __init__(self, filename, flag='c', mode=None, format='pickle', *args, **kwds):
        self.flag = flag  # r=readonly, c=create, or n=new
        self.mode = mode  # None or an octal triple like 0644
        self.format = format  # 'csv', 'json', or 'pickle'
        self.filename = filename
        if flag != 'n' and os.access(filename, os.R_OK):
            fileobj = open(filename, 'rb' if format == 'pickle' else 'r')
            with fileobj:
                self.load(fileobj)
        dict.__init__(self, *args, **kwds)

    def sync(self):
        'Write dict to disk'
        if self.flag == 'r':
            return
        filename = self.filename
        tempname = filename + '.tmp'
        fileobj = open(tempname, 'wb' if self.format == 'pickle' else 'w')
        try:
            self.dump(fileobj)
        except Exception:
            os.remove(tempname)
            raise
        finally:
            fileobj.close()
        shutil.move(tempname, self.filename)  # atomic commit
        if self.mode is not None:
            os.chmod(self.filename, self.mode)

    def close(self):
        self.sync()

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.close()

    def dump(self, fileobj):
        if self.format == 'csv':
            csv.writer(fileobj).writerows(self.items())
        elif self.format == 'json':
            json.dump(self, fileobj, separators=(',', ':'))
        elif self.format == 'pickle':
            pickle.dump(dict(self), fileobj, 2)
        else:
            raise NotImplementedError('Unknown format: ' + repr(self.format))

    def load(self, fileobj):
        # try formats from most restrictive to least restrictive
        for loader in (pickle.load, json.load, csv.reader):
            fileobj.seek(0)
            try:
                return self.update(loader(fileobj))
            except Exception:
                pass
        raise ValueError('File not in a supported format')

    def as_dict(self):
        return dict(self)



if __name__ == "__main__":


    pdict = _PersistentDict(filename="pdicttest.json", format='json')

    pdict["stuff"] = 10
    pdict["other"] = "junk"

    ddict = pdict.as_dict()

    pass