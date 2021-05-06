#creating a multithread TCP server

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print ("[*] listening on: %s: %d" % (bind_ip, bind_port))

#this is our client handling thread
def handle_client (client_socket):
        #print out what client sends
        request = client_socket.recv(9999)

        print ("[*] Received: %s" % request)
        #sends back a packet

        client_socket.send("ACK!".encode())

        client_socket.close()

#these below are from other file
        #target_host = socket.gethostname() #"127.0.0.1"
        #target_port = 9999

        # create a socket object
        #client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        #client.bind ((target_host, target_port))

        # send some data
        #client.sendto("someone entered local host".encode(),(target_host, target_port))

        # recieve some data
        #data, addr = client.recvfrom(4096)

        #print (data)
#these above is from other file

while True:
    client, addr = server.accept()

    print ("[*] Accepted connection from: %s : %d"% (addr[0], addr[1]))

    #spin up our client thread to handle incoming data
    client_handler = threading.Thread(target = handle_client, args = (client,))

    client_handler.start()
