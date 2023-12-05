import socket

SERVER_IP = '0.0.0.0' # Symbolic name meaning all available interfaces
DEST_PORT = 1729

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, DEST_PORT))
server_socket.listen(1)

client_socket, address = server_socket.accept()

data = client_socket.recv(1024)
client_socket.send("Hello, " +data)
client_socket.close()
server_socket.close()