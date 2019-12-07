from threading import Thread,Lock,Condition
import socket
import sys
import json
sys.path.insert(1, '../.')
from packages.User import User
from packages.SellItem import SellItem
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

users = {}
items={}


class Agent(Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.claddr = addr
        self.user = None
        super().__init__()


    """
        test methods for watch
    """
    def watch_func_item(self):
        print('there is a change in item')

    def watch_func_type(self):
        print('there is a new item')

    def run(self):
        inp = self.conn.recv(1024)
        while inp:
            req = json.loads(inp.decode())
            print(req)
            self.request_handler(req)
            inp = self.conn.recv(1024)
        print('client is terminating')
        conn.close()


    def make_response(self,message):
        self.conn.sendall(json.dumps({'reponse':message}).encode())


    def request_handler(self,req):
        req_type = req['type']

        if req_type == 'register':
            if(req['email'] in users):
               self.make_response('an account with this email already registered')
            else:
                self.user = User(req['email'], req['name_surname'], req['password'])
                resp=self.user.verify('A1B1C1')
                users[req['email']] = self.user
                self.make_response(resp)
            print(users)

        elif req_type == 'login':
            if req['email'] in users:
                if req['password'] == users[req['email']].password:
                    self.user = users[req['email']]
                    self.make_response('{} logged in'.format(users[req['email']].name_surname))
                else:
                    self.make_response('wrong password')
            else:
                self.make_response('You should first register')

        elif req_type == 'create_item': # sellItem parameters
            if self.user is not None:
                minbid= 1.0 if 'minbid' not in req else req['minbid'] 
                image= None if 'image' not in req else req['image'] 
                sellItem = SellItem(self.user,req['title'],req['item_type'],req['description'],req['bidtype'],req['starting'],minbid,image)
                items[sellItem.id] = sellItem
                self.make_response(1)
            else:
                self.make_response('you should login first')

        elif req_type == 'bid': # itemid bid_amount
            if self.user is not None:
                if req['itemid'] in items:
                    resp=items[req['itemid']].bid(self.user, req['bid_amount'])
                    self.make_response(resp)
                else:
                    self.make_response('No such item found')
            else:
                self.make_response('you should login first')

        elif req_type == 'start_auction':# itemid
            if self.user is not None:
                if req['itemid'] in items:
                    if self.user == items[req['itemid']].owner:
                        items[req['itemid']].start_auction()
                        self.make_response(1)
                    else:
                        self.make_response('you are not the owner')
                else:
                    self.make_response('No such item found')
            else:
                self.make_response('you should login first')       
        
        elif req_type == 'add_balance': # amount
            if self.user is not None:
                resp=self.user.add_balance(req['amount'])
                self.make_response(resp)
                print('balance is '+ str(self.user.balance))
            else:
                self.make_response('you should login first')

        elif req_type == 'change_password': # email, newpassword, old_password
            self.user=users.get([req['email']],None)
            if self.user is not None:
                resp=self.user.change_password(req['new_password'],req.get('old_password',None))
                self.make_response(resp)
            else:
                print('No user found with that email')

        elif req_type == 'list_items': #item_type, state
            if self.user is not None:
                resp=self.user.list_items(req['item_type'],req['state'])
                self.make_response(resp)
            else:
                self.make_response('you should login first')

        elif req_type == 'report':
            if self.user is not None:
                self.make_response(self.user.report())
            else:
                self.make_response('you should login first')

        elif req_type == 'view_sell_item': #itemid
            if self.user is not None:
                if req['itemid'] in items:
                    self.make_response(items[req['itemid']].view())
                else:
                    self.make_response('No such item found')
            else:
                self.make_response('you should login first')

        elif req_type == 'watch_item': #itemid
            if self.user is not None:
                if req['itemid'] in items:
                    resp=items[req['itemid']].watch(self.user, self.watch_func_item)
                    self.make_response(resp)
                else:
                    self.make_response('No such item found')
            else:
                self.make_response('you should login first')

        elif req_type == 'watch_item_type': #item_type
            if self.user is not None:
                resp=self.user.watch(self.watch_func_item,req['item_type'])
                self.make_response(resp)
            else:
                self.make_response('you should login first')

        else:
            self.make_response('WTF does that mean maaann? DAMN!(with two syllables)')    


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