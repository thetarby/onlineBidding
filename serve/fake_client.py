import socket
import re
import pickle
from threading import *

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def connect():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		request = {
		'type': None, 
		'email': None, 
		'name_surname': None,
		'password': None, 
		'new_passwpord': None, 
		'bid_amount': None,

		}
		
		# as an example, msg should be in format: connect email=azd@gmail.com password=123  
		while True:
			message = input()
			message = re.sub(' = ', '=', message) # both 'a=b' and 'a = b' are handled
			tokens = message.split(' ')
			request['type'] = tokens[0] # connect, bid etc.
			for tk in tokens[1:]:
				key, value = tk.split('=')
				request[key] = value
			s.sendall(pickle.dumps(request))


connect()	