import socket


def sent(server_socket:socket.socket,message:bytes,client_address)->bool:
    # Get the length of the message
    length = len(message)

    # Send the length of the message to the client
    server_socket.sendto(str(length).encode(),client_address)

    # Receive acknowledgement from the client
    ack, _ = server_socket.recvfrom(16)
    
    print('received acknowledgement:',ack)
    server_socket.sendto(message,client_address)
    response, _ = server_socket.recvfrom(16)
    sent_length = int(response.decode())
    if length==sent_length:
        return True
    else:
        return False


def send(server_socket:socket.socket,message:bytes,client_address):
    buffer_size=1024
    total_size = len(message)
    total_sent = 0
    while total_size>total_sent:
        if sent(server_socket,message[total_sent:][:buffer_size],client_address):
            total_sent+=buffer_size
            buffer_size*=2
        else:
            buffer_size/=2