class Reminder:
    
    def __init__(self,category = "Reminder", event_list = list()):
        self.category = category
<<<<<<< HEAD

    def modify
=======
        self.event_list = event_list

    #methods

    def add_event(self):
        item = input('What reminder would you like to add?')

        #Ask the user if he/she wants to be alerted on a day
        #Set True if user responds yes, and False otherwise. 

        if_remind = input('Would you like to be reminded on a day? (y/n)')
        if if_remind in ['y','yes','Y','Yes']:
            if_remind = True
        else:
            if_remind = False
        
        if_priority = input('Would you like to set a priority? (y/n)')
        if if_priority in ['y','yes','Y','Yes']:
            if_priority = True
        else:
            if_priority = False

        self.event_list.append(event)

    def check_event(self):
>>>>>>> f50545809c9f1682c25ab6e5d251c878763d06ac
