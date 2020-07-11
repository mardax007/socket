import socket
import threading
from datetime import datetime

HEADER = 64
PORT = 57952
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT-0YXf$j0daPn7&^PyQ8ups&dSF4HsVASCNPReNrd%rjQ^K#JII$4yagqnw0vwReX!r3!cY3QICiM%OEUMfcZA95ulH9*km0%nr6w"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    dateandtime = datetime.now()
    print("[" + dateandtime + "] [NEW CONNECTION] " + addr + " connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                conn.send("DISCONNECTED".encode(FORMAT))
                print("[" + dateandtime + "] Bye bye " + addr)
                connected = False

            else:
                dateandtime = datetime.now()
                print("[" + dateandtime + "] [" + addr + "] " + msg)
                conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    dateandtime = datetime.now()
    print("[" + dateandtime + "] [LISTENING] Server is listening on " + SERVER)
    while True:
        connections = threading.activeCount() - 1
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[" + dateandtime + "] [ACTIVE CONNECTIONS] " + connections)
dateandtime = datetime.now()
print("[" + dateandtime + "] [STARTING] server is starting...")
start()
