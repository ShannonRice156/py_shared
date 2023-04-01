''' A module that holds any additional classes and functions that hold data about a socket'''
from dataclasses import dataclass
from socket import AddressFamily, gethostname, SocketKind

@dataclass
class Info():
    '''A dataclass that stores the socket details with defaulted values that can be used'''
    host: str = gethostname()
    port: int = 9999
    family: AddressFamily = AddressFamily.AF_INET
    type: SocketKind = SocketKind.SOCK_STREAM
