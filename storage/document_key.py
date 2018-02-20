
# Library imports
from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes
import base64
import hashlib


class DocumentKey:

    REVISION = "0010"

    class _payload:

        START_MARKER = "!CRYPT!"
        END_MARKER = "STOP"
        NONCE_LEN = 8
        MESSAGE_SEP = "_"

        def __init__(self, crypt_text=None, nonce=None, revision=None, pickle=None):
            if crypt_text and nonce and revision:
                self.crypt_text = bytes(crypt_text)
                self.nonce = bytes(nonce)
                self.revision = str(revision)
            elif pickle:
                self.unpickle(pickle)
            else:
                Exception("Package missing parameters")

        def pickle(self):
            return self.MESSAGE_SEP.join([self.START_MARKER, DocumentKey.REVISION, self._encode_b64(self.nonce),
                                          self._encode_b64(self.crypt_text), self.END_MARKER])

        def unpickle(self, pickle_str):
            pickle_list = pickle_str.split(self.MESSAGE_SEP)
            self.start = pickle_list[0]
            self.revision = pickle_list[1]
            self.nonce = self._decode_b64(pickle_list[2])
            self.crypt_text = self._decode_b64(pickle_list[3])
            self.end = pickle_list[4]
            assert self.start == self.START_MARKER and self.end == self.END_MARKER

        @staticmethod
        def _encode_b64(plaintext):
            return base64.b16encode(bytes(plaintext)).decode("utf-8")

        @staticmethod
        def _decode_b64(bytes):
            return base64.b16decode(bytes)

    def __init__(self, key: bytes=None, plaintext_password: str=None):
        """
        This class contains the encryption key, and provides encryption and decryption methods
        Key format is sha256 of a plaintext password.
        Encryption is achieved using Salsa20 256bit symmetric stream
        :param key:
        :param plaintext_password:
        """
        if key:
            self._key = key
        elif plaintext_password:
            self._key = self._password_to_key(plaintext_password)
        else:
            raise Exception("No key or password provided")

    def encrypt(self, plaintext: str):
        """
        Encrypts the plaintext string, and packs it into a base64 encoded string which includes the nonce
        :param plaintext:
        :return:
        """

        # Create new cipher instance (new nonce)
        cipher = Salsa20.new(self._key)

        # Encode plaintext to bytes, and encrypt
        crypt_text = cipher.encrypt(plaintext.encode())

        # Pack up message
        p = self._payload(crypt_text, cipher.nonce, self.REVISION)

        # Pickle the payload into a string and return
        return p.pickle()

    def decrypt(self, packed_crypt_text: str, encoding: str ="utf-8"):
        """
        Decrypts the packed crypt text string, expecting the format from the encrypt method above.
        If the encryption payload start marker isn't found, it assumes the string isn't encrypted and returns it as is
        :param packed_crypt_text:
        :param encoding:
        :return:
        """
        # If we can't find the encryption start marker, just return the string as is
        if not packed_crypt_text.startswith(self._payload.START_MARKER):
            return packed_crypt_text

        # Unpickle payload string
        payload = self._payload(pickle=packed_crypt_text)

        # Create new cipher instance, with our key and the payload nonce
        cipher = Salsa20.new(self._key, payload.nonce)

        # Decrypt the payload, apply the string encoding specified and return
        return cipher.decrypt(payload.crypt_text).decode(encoding)

    def _password_to_key(self, plaintext_password):
        return hashlib.sha256(plaintext_password.encode()).digest()


if __name__ == "__main__":

    k1 = DocumentKey(get_random_bytes(16))

    plain = "lorem ipsum, attack at dawn, Eve is about to get it"
    crypt = k1.encrypt(plain)
    decrypt = k1.decrypt(crypt)
    assert plain == decrypt
