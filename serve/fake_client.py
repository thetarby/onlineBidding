import socket
from threading import *
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def connect():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		while True:
			message=input()
			s.sendall(str.encode(message))



connect()	