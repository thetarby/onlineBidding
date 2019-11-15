class Watcher:
    def __init__(self):
        self.observers={}
        self.item_watchers={}

    def register(self,user,watch_method,item_type):
        if(item_type in self.observers):
            self.observers[item_type].append((user, watch_method))   
        else:
            self.observers[item_type]=[]
            self.observers[item_type].append((user, watch_method))


    def item_watcher_register(self,item,user,watch_method):
        if(item.title in self.item_watchers): # there may be mistake since two items could have same title
            self.item_watchers[item].append((item,watch_method))
        else:
            self.item_watchers=[]
            self.item_watchers.append((item,watch_method))

    """
        if user is watching, call its watch method
    """
    def notify(self,key):
        if(key in self.observers):         
            for user in self.observers[key]:
                user[1]()

        if(key in self.item_watchers):
            for item in self.item_watchers[key]:
                item[1]()

