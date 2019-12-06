from threading import Thread,Lock,Condition
import socket
import sys
import pickle
sys.path.insert(1, '../.')
from packages.User import User

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


class Agent(Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.claddr = addr
        self.user = None
        super().__init__()

    def run(self):
        inp = self.conn.recv(1024)
        while inp:
            req = pickle.loads(inp)
            print(req)
            self.request_handler(req)
            inp = self.conn.recv(1024)
        print('client is terminating')
        conn.close()

    def request_handler(self,req):
        req_type = req['type']

        if req_type == 'register':
            print('user will be created')
            self.user = User(req['email'], req['name_surname'], req['password'])
            self.user.verify('A1B1C1')

        elif req_type == 'start_auction':
            print('auction will be started')
        elif req_type == 'change_password':
            pass
        elif req_type == 'list_items':
            pass
        elif req_type == 'report':
            pass
        else:
            print('WTF does that mean maaann? DAMN!(with two syllables)')    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

try:
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        a = Agent(conn,addr)
        a.start()
finally:
    s.close()