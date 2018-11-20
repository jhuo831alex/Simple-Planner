class Event:

    def __init__(self,item,remind_time = None,priority = None, notes = None):
        self.item = item
        self.remind_time = remind_time
        self.priority = priority
        self.notes = notes

    def modify_notes(self,new_item = None, new_remind_time = None, new_priority=None, new_notes=None):
        question=input('Do you want to modify your event?')
        if question in ['y','yes','Y','Yes']:
            features = input('What features of this event do you want to change? (Please enter: item, remind_time, priority, or notes)').split()
            for feature in features:
                if feature == 'item':
                    new_item = input('What is your new item?')
                    self.item = new_item
                else if feature == 'remind_time':
                    new_remind_time = input('What is your new remind time?')
                    self.remind_time = new_remind_time
                else if feature == 'priority':
                    new_priority = input('What is your new priority?')
                    self.priority = new_priority
                else if feature == 'notes':
                    new_notes = input('What is your new notes?')
                    self.notes = new_notes
