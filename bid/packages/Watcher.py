def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Watcher:
    def __init__(self):
        """
        observers:
            {
                'car':[(user, method),(user,method)],
                'phone':[(user, method),(user,method)],
            }
        """
        self.observers={}
        self.item_watchers={}

    def register(self,user,watch_method,item_type):
        if(item_type in self.observers):
            temp=[1 for user_method_pair in self.observers[item_type] if user_method_pair[0]==user]
            if(len(temp)):
                return('user already watching the item with the same method')
            else:
                self.observers[item_type].append((user, watch_method))
                return 1   
        else:
            self.observers[item_type]=[]
            self.observers[item_type].append((user, watch_method))
            return 1


    def item_watcher_register(self,item,user,watch_method):
        if(item in self.item_watchers):
            temp=[1 for user_method_pair in self.item_watchers[item] if user_method_pair[0]==user]
            if(len(temp)):
                return('item is already being watched by the user')
            else:
                self.item_watchers[item].append((user,watch_method))
                return 1
        else:
            self.item_watchers[item]=[]
            self.item_watchers[item].append((user,watch_method))
            return 1

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

