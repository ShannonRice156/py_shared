'''A module that uses haslib and salting to encode a string'''
import os
import hashlib

class HashSalt():
    '''Generates a hashed and salted version
       of the string provided when the class is instantiated'''
    def  __init__(self, to_hash: str , salt = None) -> None:
        '''Generates random bytes for the salt and
           assigns the encoded version of the input string to a variable'''
        if salt is None:
            self._salt = os.urandom(32)
        else:
            self._salt = salt

        self._key = to_hash.encode("utf-8")

    def generate_salted_hash(self) -> str:
        '''Returns the the _key salted and hashed'''
        return hashlib.pbkdf2_hmac('sha256', self._key, self._salt, 1000)
