
# socket_echo_server.py
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listaDeEsperaPassageiro = []
listaDeEsperaCarga = []

def decisao(message):
	message = message.split(',')
	print(message)

	if(message[0].upper()=='1'.upper()): # Passageiro
		listaDeEsperaPassageiro.append((message[0], message[1]))
		if(listaDeEsperaPassageiro.count((message[0], message[1]))==1):
			print("Requisição do passageiro registrada com Sucesso!")
			return 'Requisição do passageiro registrada com Sucesso!'.encode('utf-8')
	elif(message[0].upper()=='2'.upper()): # Carga
		listaDeEsperaCarga.append((message[0], message[1]))
		if(listaDeEsperaCarga.count((message[0], message[1]))==1):
			print("Requisição do passageiro registrada com Sucesso!")
			return 'Requisição do passageiro registrada com Sucesso!'.encode('utf-8')
	# elif(message[0].upper()=='motorista'.upper())
		# funcao para definicao do motorista

# Bind the socket to the port
server_address = ('localhost', 10001)
print('starting up on {} port {}'.format(*server_address))
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
            data = connection.recv(512)
            print('received {!r}'.format(data))
            data = decisao(data.decode())
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()