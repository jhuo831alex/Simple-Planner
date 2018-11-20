class Reminder:
    import datetime
    from Event_class import *
    
    def __init__(self,category = "Reminder", event_list = list()):
        self.category = category
        self.event_list = event_list

    #methods
    def prompt_user(self,prompt_msg):
        input_ = input('prompt_msg')
        if input in ['y','yes','Y','Yes']:
            result = True
        else:
            result = False
        return result

    def add_event(self):
        item = input('What reminder would you like to add?')
        
        if_remind = prompt_msg('Would you like to be reminded on a day? (y/n)')
        if_priority = prompt_msg('Would you like to set a priority? (y/n)')
        if_notes = prompt_msg('Would you like to add notes? (y/n)')

        if if_remind:
            date_string = input('What time would you like to be reminded? (ex: 05/01/2018 23:01)')
            try:
                date_time = datetime.strptime(date_string, '%m/%d/%y %H:%M')
            except:
                print('Invalid date format. Please refer to example.')
        else:
            date_time = None
        
        if if_priority:
            priority_string = input('Which priority level would you like to assign to this event? (*/**/***)')
            if priority_string not in ['*','**','***']:
                print('Invalid priority level. Please refer to example.')
        else:
            priority_string = None
        
        if if_notes:
            notes = input("What notes would you like to add to this event?")
        else:
            notes = None
        
        new_event = Event(item,date_time,priority_string,notes)
        self.event_list.append(new_event)





#        item = input('What reminder would you like to add?')
#
#        #Ask the user if he/she wants to be alerted on a day
#        #Set True if user responds yes, and False otherwise.
#
#        if_remind = input('Would you like to be reminded on a day? (y/n)')
#        if if_remind in ['y','yes','Y','Yes']:
#            if_remind = True
#        else:
#            if_remind = False
#
#        if_priority = input('Would you like to set a priority? (y/n)')
#        if if_priority in ['y','yes','Y','Yes']:
#            if_priority = True
#        else:
#            if_priority = False
#
#        self.event_list.append(event)

    def check_event(self):
