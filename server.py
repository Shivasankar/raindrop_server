import socket
import json


def socketconnect():
    s = socket.socket()
    host = socket.gethostname()
    port = 8777
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        message = c.recv(1024)
        decode = json.loads(message)
        if message is None:
            while True:
                c.send(message)
    return


socketconnect()

