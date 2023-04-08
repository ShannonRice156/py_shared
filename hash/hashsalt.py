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
            self.salt = os.urandom(32)
        else:
            self.salt = salt

        self._key = to_hash.encode("utf-8")

    def generate_salted_hash(self) -> str:
        '''Returns the the _key salted and hashed'''
        return hashlib.pbkdf2_hmac('sha256', self._key, self.salt, 1000)

    @property
    def salt(self) -> bytes:
        '''Returns the the _salt'''
        return self._salt

    @salt.setter
    def salt(self, value: bytes) -> bytes:
        '''Sets value of _salt'''
        self._salt = value
