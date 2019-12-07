import socket
import re
import pickle
from threading import *
import json

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
{"type":"register", "email":"naber@gmail.com", "password":"123", "name_surname":"cenk kol"}
{"type":"create_item","title":"iphone x", "item_type":"phone","description":"desc", "bidtype":["increment",0,15], "starting":0}
{"type":"start_auction","itemid":1}
{"type":"bid","bid_amount":10,"itemid":1}
"""
client1
{"type":"register", "email":"azad@gmail.com", "password":"123", "name_surname":"AZad kol"}
{"type":"add_balance","amount":10}
{"type":"watch_item","itemid":1}
{"type":"bid","bid_amount":20,"itemid":1} 

"""

"""
client2
{"type":"register", "email":"naber@gmail.com", "password":"123", "name_surname":"cenk kol"}
{"type":"add_balance","amount":10}
{"type":"bid","bid_amount":20,"itemid":1} 
"""

"""
client3 satici
{"type":"register", "email":"satici@gmail.com", "password":"123", "name_surname":"satici kol"}
{"type":"create_item","title":"iphone x", "item_type":"phone","description":"desc", "bidtype":["increment",0,15], "starting":0}
{"type":"start_auction","itemid":1}
"""
def connect():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))

		
		# as an example, msg should be in format: connect email=azd@gmail.com password=123  
		while True:
			message = input()
			#message = re.sub(' = ', '=', message) # both 'a=b' and 'a = b' are handled
			#tokens = message.split(' ')
			try:
				json.loads(message)
			except Exception as e:
				print(str(e))
				continue
			s.sendall(message.encode())
			data = s.recv(1024)
			print(json.loads(data.decode()))


connect()	