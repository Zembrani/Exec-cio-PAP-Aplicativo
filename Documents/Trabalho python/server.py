import socket
import sys
import string

import struct #estrutura que representa a header do tcp

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:

        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data_byte = connection.recv(13)
            print('received ---------', end = ' ')
            data = data_byte.decode()
            data = data.upper()
            print(data)
            if data:
                print('sending data back to the client')
                data_byte = data.encode()
                connection.sendall(data_byte)
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()