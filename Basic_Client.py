import socket
host = socket.gethostname()
port = 4041
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
#msg = s.recv(1024)
#print(msg.decode("UTF-8"))

full_msg =""
while True:
    msg = s.recv(8)
    if len(msg) <=0:
        print("No message")
        break
    full_msg = full_msg + msg.decode("UTF-8")
print(full_msg)