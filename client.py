import socket
from log import ( logger, Config )

class Client(object):
    
    HEADER: int = Config.HEADER
    PORT: int = Config.PORT
    SERVER: object = Config.SERVER
    ADDR: tuple = (SERVER, PORT)
    FORMAT: str = Config.FORMAT
    DISCONNECT: str = Config.DISCONNECT

    x: object = Config.setStream(host='client', addr=ADDR)

    @staticmethod
    def filterFormat(msg: str) -> tuple:

        message = msg.encode(Client.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(Client.FORMAT)
        send_length += b' ' * (Client.HEADER - len(send_length))

        return send_length, message

    @staticmethod
    def send(msg: str):
        send_length, message = Client.filterFormat(msg=msg)
        Client.x.send(send_length)
        Client.x.send(message)
        logger.info(Client.x.recv(2048).decode(Client.FORMAT))

if __name__ == '__main__':

    logger.info('W E L C O M E')
    x = True
    while x:
        msg = input()
        if msg == 'exit':
            Client.send(msg=Client.DISCONNECT)
            x = False
        else:
            Client.send(msg=msg)