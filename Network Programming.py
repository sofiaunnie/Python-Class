"""
Sockets are interior endpoints built for sending and receiving data.
In a basic network communication there are always 2 sockets - one for each communicating device.
These sockets are made up of IP ADDRESSES and PORT NUMBERS
Each device can have n number of sockets based on the number of port numbers.
These port are used by different protocols/services/computer processes by the communicating device when making requests
to servers and vice versa

a resmon
1. ipconfig                                IP ADDRESS FAMILIES - IPV4, IPV6
2. nslookup (provides the dns server of a website)
3. ipconfig/all

Server
A program,computer or device denoted to managing network resources. Listens for connections from clients.
Can be on the same device/ local or remote.

Client
Computer or software that receives services or information. Clients request for services from servers e.g Web browserG
"""

# BASIC CLIENT
print("Hi")
print(type("Hi"))
print(bytes("Hi","UTF-8")) #Encoding in a string
print(type(bytes("Hi","UTF-8"))) #Returns bytes

greeting = "Hi"
print(f"{greeting}")
print(type(greeting))  #Returns str
print('--------------------------------------------')
#method 2
encoded = greeting.encode()
print(type(encoded))
input()

print('--------------------------------------------')
#method 1
print(bytes(greeting,"UTF-8")) #Encoding in a string
print(type(bytes(greeting,"UTF-8"))) #Returns bytes