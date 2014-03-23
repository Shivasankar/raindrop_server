import socket
import json
import ast


def hold_message(msg):
    print type(msg)
    channel = msg.keys()
    message = msg.values()
    print "hld msg", channel
    print "hld msg", message
    return


def publish(decode):
    lst = list(decode)
    print hold_message(lst[0])
    return 'msg from p'


def subscribe(channel):

    if channel is hold_message.hld_msg.has_key(channel):
        message = channel.values()
        print message
    return message


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
        decode1 = json.dumps(message)
        splitline = decode1.rsplit(',')
        fnd_req_type = splitline[1]
        req_type = fnd_req_type[2]
        if req_type is 'p':
            publish(decode)
        else:
            subscribe(message)
            c.send(message)
    return


socketconnect()

