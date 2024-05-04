import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
host = '192.168.50.244'
server_address = (host, 12345)

def received(client_socket:socket.socket,server_address:tuple[str,int]):
    length, _= client_socket.recvfrom(16)
    msg_length = int(length.decode())
    print('message length:',msg_length)
    client_socket.sendto('ok'.encode(),server_address)
    msg, _ = client_socket.recvfrom(int(msg_length))
    received_length = len(msg)
    print('received:',received_length)
    if received_length==msg_length:
        client_socket.sendto(str(msg_length).encode(),server_address)
        return msg
    return False

# Receive response from the server
def receive_file(file_name:str,client:socket.socket,server):
    client.sendto(file_name.encode(),server)
    data = received(client,server)
    with open(file_name,'xb') as file:
        file.write(data)

receive_file('setup.py',client_socket,server_address)
# Close the socket
client_socket.close()
