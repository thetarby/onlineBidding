from packages.SellItem import *

class SellItemIncrement(SellItemBase):
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid=1.0,image=None):
        super().__init__(owner,title,item_type,decsription,bidtype,starting,minbid,image)

    #override
    def start_auction(self, stopbid=None):
        self.watcher.notify(self.item_type)
        self.watcher.notify(self)

        # TODO: add min delta functionality
        if stopbid is not None:
            self.stopbid = stopbid
        else:
            print('stopbid is not defined')  