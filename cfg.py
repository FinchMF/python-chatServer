import socket

class Config(object):

    HEADER: int = 64
    PORT: int = 5050
    SERVER: object = socket.gethostbyname(socket.gethostname())
    ADDR: tuple = (SERVER, PORT)
    FORMAT: str = 'utf-8'
    DISCONNECT: str = '!DISCONNECT!'

    @staticmethod
    def setStream(host: str, addr: tuple) -> object:

        x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if host == 'client':
            x.connect(addr)
        else:
            x.bind(addr)
        
        return x