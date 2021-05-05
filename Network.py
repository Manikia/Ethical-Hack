#creating clients and serveres
#since Im using python 3 I have to decode from string to bytes
#slow and reliable transfers


#TCP CLIENT CODE:

import socket

target_host = "www.google.com"
target_port = 80

#creating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF and SOCK are parameters
#AF means we are using standard PIv4 address or hostname
#SOCK means that this is the TCP client

#connecting to client
client.connect((target_host, target_port))
#server_address = (target_host, target_port)
#we are connecting the client to server

#sending data
data = ("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send(data.encode('utf-8'))

#recieving data 
response = client.recv(4096).decode('utf-8')

print(response)

#this code is a simple representation and 
#assumption that there is nothing blocking us from accessing 
# the information or sending information