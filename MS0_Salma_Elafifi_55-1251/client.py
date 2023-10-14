import socket
import select
import sys

client_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5605
client_socket.connect(('127.0.0.1',port)) 

message=input("enter your message: ")

while(message != 'CLOSE SOCKET'):
    client_socket.send(message.encode())
    data=client_socket.recv(1024).decode()
    print("recieved: " + data)
    message=input("enter your message: ")

client_socket.close()

