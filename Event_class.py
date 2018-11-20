class Event:

    def __init__(self,item,remind_time = None,priority = None, notes = None):
        self.item = item
        self.remind_time = remind_time
        self.priority = priority
        self.notes = notes

    def modify_item(self,new_item=None):
        question=input('Do you want to modify your item?')
        if question in ['y','yes','Y','Yes']:
            question = True
            new_item = input('What is your new item?')
            self.item = new_item
    
    def modify_remind_time(self,new_remind_time=None):
        question=input('Do you want to modify your remind time?')
        if question in ['y','yes','Y','Yes']:
            question = True
            new_remind_time = input('What is your new remind time?')
            self.remind_time = new_remind_time