#sending packets to UDP form
#connectionless protocol
#fast but non guaranteed transfers

import socket

target_host = socket.gethostname() #"127.0.0.1"
target_port = 8000

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.bind ((target_host, target_port))

# send some data
client.sendto("hello".encode(),(target_host, target_port))

# recieve some data
data, addr = client.recvfrom(4096)

print (data)

