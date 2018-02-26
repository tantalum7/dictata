
# Library imports
import ftplib
import io

# Project imports
from storage.generic_backend import GenericBackend
from storage.uid import UID
from exceptions import StorageOpenException, DocumentNotFoundException



class FtpJsonBackend(GenericBackend):

    def __init__(self, settings: dict):
        """
        Json based remote FTP implementation of GenericBackend.
        :param settings:
        """







if __name__ == "__main__":


    dir = "dictata"
    file = "dictatadb.json"


    ftp = ftplib.FTP("ftp.oliver-kent.co.uk")

    ftp.login("python_test@oliver-kent.co.uk", "pineapple$123")

    fp = io.BytesIO(bytes("some initial text data".encode("utf-8")))

    ftp.storlines("STOR test.txt", fp)

    ftp.quit()

    ftp.close()

    print("done")