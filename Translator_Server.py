import socket
dest = input("Please enter the destination lamuage: ")
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5557))
server.listen(5)
print("Listening now.....")
client_comn, address = server.accept()
print("Connection established from {}",format(address))

while True:
    newmsg = input("Enter some text to translate: ")
    if newmsg == "" or newmsg == 'q':
        print("Quitting program....")
        client_comn.close()
        break
    client_comn.send(f"{dest}:{newmsg}".encode())