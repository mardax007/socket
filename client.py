import socket
import tkinter as tk

HEADER = 64
PORT = 57952
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

messagefromuser = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def show_entry_fields():
    send(e1.get())
    print("Message: %s" % (e1.get()))
    messagefromuser = e1.get()

def exitapp():
    send(DISCONNECT_MESSAGE)
    master.quit()
    exit()

while True:
    master = tk.Tk()
    tk.Label(master, text="Message").grid(row=0)

    e1 = tk.Entry(master)

    e1.grid(row=0, column=1)

    tk.Button(master, text='Quit', command=exitapp).grid(row=3, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Send', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

    tk.mainloop()
