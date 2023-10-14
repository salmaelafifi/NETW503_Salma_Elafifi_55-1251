import socket
import select
import sys

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5605
server_socket.bind(('127.0.0.1',port)) 

server_socket.listen(1)

while True:
    client,add = server_socket.accept()
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        data = data.upper()
        client.send(data.encode())
        if data == 'CLOSE SOCKET':
            break

    client.close()

