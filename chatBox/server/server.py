from chatBox import ( socket, threading, logger, Config )

class Server(object):

    HEADER: int = Config.HEADER
    PORT: int = Config.PORT
    SERVER: object = Config.SERVER
    ADDR: tuple = (SERVER, PORT)
    FORMAT: str = Config.FORMAT
    DISCONNECT: str = Config.DISCONNECT

    x: object = Config.setStream(host='server', addr=ADDR) 

    @classmethod
    def set_header(cls, size: int):
        cls.HEADER: int = size

    @classmethod
    def set_port(cls, port: int):
        cls.PORT: int = port

    @staticmethod
    def handle_client(conn: object, addr: str):
        logger.info(f'[NEW CONNECTION] {addr} connected')

        connected = True
        while connected:
            msg_length: str = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length: int = int(msg_length)
                msg: str = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT:
                    connected = False

                logger.info(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))

        conn.close()

    @staticmethod
    def start():
        Server.x.listen()
        logger.info(f'[LISTENING] Server is listening on {Server.SERVER}')
        while True:
            conn, addr = S.accept()
            thread = threading.Thread(target=Server.handle_client, args=(conn, addr))
            thread.start()
            logging.info(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

if __name__ == '__main__':

    Server.start()