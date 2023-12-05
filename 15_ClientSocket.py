"""
This program opens a socket after runninng the command python
C:\Cyber\echo_server_stream.pyc
in CMD. The command utilizes a local host server.
Thr client then sends a message, recieves a message from the server, prints it and
closes the client.

"""

import socket

HOST_IP = '127.0.0.1'
DEST_PORT = 1729

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect((HOST_IP, DEST_PORT))

user_msg = input("Please enter a message: ")
my_socket.send(user_msg)
data = my_socket.recv(1024)
print(data)
my_socket.close()


