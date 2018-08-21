import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data_complete = ""

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print('sending -------', end = ' ')
    print(message)
    # message_bytes = bytes(message, 'utf-8')
    message_bytes = message.encode('utf-8')
    sock.sendall(message_bytes)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data_bytes = sock.recv(13)
        data = data_bytes.decode()
        amount_received += len(data)
        print('received --------', end = ' ')
        print(data)
        temp = data
        data_complete = data_complete + temp
    print(data_complete)

finally:
    print('closing socket')
    sock.close()