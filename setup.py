import socket
from udp import send

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print('UDP server is running on {}:{}'.format(*server_address))

# Receive and process incoming messages
while True:
    data, client_address = server_socket.recvfrom(1024)  # Receive data from client
    file_name = data.decode()
    print(f'received request, {file_name}, from {client_address}')
    with open(file_name,'rb') as file:
        send(server_socket,file.read(),client_address)
