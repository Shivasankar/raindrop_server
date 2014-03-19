import socket
import json
import ast

def publish():
    return


def subscribe(message):
    if message is None:
            while True:
                socketconnect.c.send(message)
    return


def socketconnect():
    s = socket.socket()
    host = socket.gethostname()
    port = 8777
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        message = c.recv(1024)
        decode = json.dumps(message)
        splitline = decode.rsplit(',')
        fnd_req_type = splitline[1]
        req_type = fnd_req_type[2]
        if req_type is 'p':
            publish(decode)
        else:
            subscribe()
    return


socketconnect()

