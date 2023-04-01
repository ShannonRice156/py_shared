''' Module to handle all core socket classes, functions and methods'''
import socket
from abc import ABC, abstractmethod
from .socket_info import Info

class SocketItem(ABC):
    '''Base class for any class that needs to use socket'''
    def __init__(self, socket_information: Info) -> None:
        self.info = socket_information
        self.encoding = "utf-8"
        self._socket = None

    def run(self) -> None:
        '''Method that listens for any incoming information'''
        self.socket.listen()

    def set_encoding(self, encoding: str) -> None:
        '''Method that allows the user of the class to set a different encoding'''
        self.encoding = encoding

    def send(self, message: str) -> None:
        '''Method that sends encoded information to the socket'''
        self.socket.send(message.encode(self.encoding))

    def receive(self) -> str:
        '''Returns the decoded data received through the socket'''
        return self.socket.recv(1024).decode(self.encoding)

    @abstractmethod
    def connect_to_socket(self) -> None:
        ...

    @property
    def socket(self) -> socket:
        '''Returns an instance of a socket, creates one if one has not already been created'''
        if self._socket is None:
            self.socket = socket.socket(self.info.family, self.info.type)
            self.connect_to_socket()
        return self._socket

    @socket.setter
    def socket(self, new_socket: socket) -> None:
        '''Sets class instance of _socket to the new socket provided'''
        self._socket = new_socket
