import socket
from abc import ABC, abstractmethod
from socket_info import info

class SocketItem(ABC):
    def __init__(self, socket_information: info) -> None:
        self.info = socket_information
        self.encoding = "utf-8"
        self._socket = None
    
    def run(self) -> None:
        self.socket.listen()

    def set_encoding(self, encoding: str) -> None:
        self.encoding = encoding

    def send(self, message: str) -> None:
        self.socket.send(message.encode(self.encoding))

    def receive(self) -> str:
        return self.socket.recv(1024).decode(self.encoding)
    
    @abstractmethod
    def connect_to_socket(self) -> None:
        ...
        
    @property
    def socket(self) -> socket:
        if self._socket is None:
            self.socket = socket.socket(self.info.family, self.info.type)
            self.connect_to_socket()
        return self._socket
    
    @socket.setter
    def socket(self, new_socket: socket) -> None:
        self._socket = new_socket
        