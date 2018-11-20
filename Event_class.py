class Event:

    def __init__(self,item,remind_time = None,priority = None, notes = None):
        self.item = item
        self.remind_time = remind_time
        self.priority = priority
        self.notes = notes

<<<<<<< HEAD
    def modify_item(self,new_item=None):
        question=input('Do you want to modify your item?')
        if question in ['y','yes','Y','Yes']:
            question = True
            new_item = input('What is your new item?')
            self.item = new_item
     
        
         
=======
    
>>>>>>> e7619f81e601c11db6a1ce3b3099656869aceb8e
