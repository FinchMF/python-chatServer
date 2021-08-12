from chatBox import ( socket, logging, Config )

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

        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))

        return send_length, message

    @staticmethod
    def send(msg: str):
        send_length, message = Client.filterFormat(msg=msg)
        x.send(send_length)
        x.send(message)
        logging.info(x.recv(2048).decode(FORMAT))

if __name__ == '__main__':

    logging.info('W E L C O M E')
    x = True
    while x:
        msg = input()
        if msg == 'exit':
            Client.send(msg=Client.DISCONNECT)
        else:
            Client.send(msg=msg)