class Watcher:
    def __init__(self):
        self.observers={}


    def register(self,user,watch_method,item_type):
        if(item_type in self.observers):
            self.observers[item_type].append((user, watch_method))   
        else:
            self.observers[item_type]=[]
            self.observers[item_type].append((user, watch_method))


    def notify(self,item_type):
        """
            if user is watching call its watch method
        """
        if(item_type in self.observers):         
            for user in self.observers[item_type]:
                user[1]()


