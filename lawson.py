# CLIENT-SIDE

import socket

clientsoc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target_host = ''
target_port = 4700
clientsoc.connect((target_port,target_host))

while True:
    servmsg = clientsoc.recv(1024)
    print(f"New message from server: {servmsg.decode('utf-8')}")
    cmsg = input("Client Message: ")
    clientsoc.send(cmsg.encode("utf-8"))
    print("Message Sent to server")