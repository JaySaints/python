#!/usr/bin/python3

# import de library socket
import socket

# create the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get ip localhost == 192.168.25.10
host = socket.gethostname()
# Set the port connect
port = 444
# Binding to socket
serversocket.bind(('192.168.25.5', port)) # host will be replaced/substituted with IP, if changed and not running on host
# start TCP listener
serversocket.listen(3)

while True:
    # start the connection
    clientsocket, address = serversocket.accept()    
    print("received connection from %s" % str(address))
    message = "Hello! Thank you for conneting to the server" + "\r\n"
    # replay message to the client
    clientsocket.send(message.encode('ascii'))
    # End the connection 
    clientsocket.close()  
    


