from channels.generic.websocket import WebsocketConsumer
import json
import threading
import time

x=0
t = threading.Timer(5, lambda x:x+1, args=(x,))
t.start()
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.t = threading.Timer(5, self.receive)
        self.t.start()

    def disconnect(self, close_code):
        pass

    def receive(self):
        global x
        x=x+1
        self.send(text_data=json.dumps({
            'message': x
        }))
        self.t = threading.Timer(5, self.receive)
        self.t.start()