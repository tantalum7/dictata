
# Library imports
import os
import shutil

# Project imports
from storage.generic_backend import GenericBackend
from storage.uid import UID
from storage.json_cache import JsonCache
from storage.file_lock import FileLock
from exceptions import StorageOpenException, DocumentNotFoundException


class LocalJsonBackend(GenericBackend):

    def __init__(self, settings: dict):
        """
        Local JSON implementation of GenericBackend. JSON file contents are loaded into memory when opened.
        All read/write operations are in memory. Memory contents are written to json file when sync() is called
        :param settings: Not used
        """
        self._db = None
        self._settings = settings
        self._file_lock = None

    def open(self, path: str):
        """
        Opens the JSON file at the path provided, and loads contents into memory.
        :param path:
        :return:
        """

        self._file_lock = FileLock(path)
        self._path = path
        self._db = JsonCache(read_method=self._read, overwrite_method=self._overwrite,
                             set_lock_method=self._set_lock, release_lock_method=self._release_lock)

    def close(self, options: dict=None):
        """
        Closes the json file, performs a last sync() and then drops contents from memory.
        :param options:
        :return:
        """
        self.sync()
        self._db.close()
        self._db = None

    def get(self, uid: UID, key: str) -> str:
        """
        Gets the string stored against the key passed, for document with the UID passed
        :param uid:
        :param key:
        :return:
        """
        # Try and get the document with the UID passed
        try:
            doc = self._db[str(uid)]

        # Re-raise a KeyError as a DocumentNotFoundException
        except KeyError:
            raise DocumentNotFoundException

        # Return the string stored against the key passed, or None
        else:
            return str(doc.get(key, None))

    def get_document(self, uid: UID) -> dict:
        """
        Gets the entire document with the UID passed, returns it as a dict
        :param uid:
        :return:
        """
        # Try and get the document with the UID passed
        try:
            doc = self._db[str(uid)]

        # Re-raise a KeyError as a DocumentNotFoundException
        except KeyError:
            raise DocumentNotFoundException

        # Return the doc dict as is
        else:
            return doc

    def delete_document(self, uid: UID):
        """
        Deletes the entire document with the UID passed
        :param uid:
        :return:
        """
        # Try and delete the document with the UID passed
        try:
            del self._db[str(uid)]

        # Re-raise a KeyError as a DocumentNotFoundException
        except KeyError:
            raise DocumentNotFoundException

    def put(self, uid: UID, key: str, value: str):
        """
        Puts string value against string key, to the document with the UID passed.
        Put works as an insert or update command. If the document doesn't exist, it is created
        :param uid:
        :param key:
        :param value:
        :return:
        """
        # If the document with this UID can't be found, create it
        if not self._db[str(uid)]:
            self._db[str(uid)] = {}

        # Store the value string
        self._db[str(uid)][key] = str(value)

    def sync(self, options: dict=None):
        """
        Synchronises the memory cache with storage file
        :param options:
        :return:
        """
        self._db.sync()

    def count(self, uid: UID) -> int:
        """
        Returns the number of keys stored in a document with the given UID
        :param uid:
        :return:
        """
        # Return the len() of the document, or 0 if the doc can't be found
        return len(self._db[str(uid)]) if self._db[str(uid)] else 0

    def _read(self):
        with open(self._path, "r") as fp:
            return fp.read()

    def _overwrite(self, contents):

        # Concat temp file path, by appending .tmp
        tempname = self._path + '.tmp'

        # Try to open the temp file, and write contents
        try:
            fp = open(tempname, "w+")
            fp.write(contents)

        # Catch any exception, delete the temp file then re-raise exception
        except:
            os.remove(tempname)
            raise

        # Write temporary file was successful, replace the real file with the temp one
        else:
            try:
                fp.close()
                os.replace(tempname, self._path)

            except Exception as e:
                exit()

        # Make sure the file point gets closed
        finally:
            fp.close()

        pass

    def _set_lock(self):
        return self._file_lock.acquire()

    def _release_lock(self):
        self._file_lock.release()