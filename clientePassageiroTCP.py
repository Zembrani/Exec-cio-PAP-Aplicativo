#socket_echo_client.py
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

def menu():
	print("Olá digite qual o tipo de varga vc deseja transportar.")
	print("1 : Passageiro.")
	print("2 : Carga.")
	escolha = input()
	while escolha != '1' and escolha != '2':
		print("valor invalido, digite novamente")
		escolha = input()
	if(escolha=='1') :
		print("Digite a quantidade de passageiros, deve ser menor ou igual a 4")
	elif(escolha=='2'):
		print("Digite a quantidade de carga, em kg.")
	quantidade = input()
	message = (escolha + ',' + quantidade)
	return message.encode('utf-8')

try:

    # Send data
	message = menu()
	print('sending {!r}'.format(message))
	sock.sendall(message)

    # Look for the response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data_bytes = sock.recv(512)
		data = data_bytes.decode()
		amount_received += len(data)
		# print('received {!r}'.format(data))
		print(data, end = '')

finally:
	print('')
	print('closing socket')
	sock.close()