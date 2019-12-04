from threading import Thread,Lock,Condition
import socket
import sys
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


class Agent(Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.claddr = addr
        Thread.__init__(self)

    def run(self):
        inp = self.conn.recv(1024)
        while inp:
            req=inp.decode()
            print(req)
            self.request_handler(req)
            inp = self.conn.recv(1024)
        print('client is terminating')
        conn.close()

    def request_handler(self,req):
        if(req=='create user'):
            print('user will be created')
        elif(req=='start auction'):
            print('auction will be started')    
        else:
            print('WTF does that mean maaann? DAMN!(with two syllables)')    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


while True:
    conn, addr = s.accept()

    print('Connected by', addr)
    a = Agent(conn,addr)
    a.start()