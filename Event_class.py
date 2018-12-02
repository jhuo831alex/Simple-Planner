class Event:
    """
    This class allows users to modify the existing events that they created through class Reminder,
    users can change the features for each event, including remind time, priority, and the notes for the event.

    """
    
    def __init__(self,item,remind_time = None,priority = None, notes = None): 
        #initiate event features
        self.item = item
        self.remind_time = remind_time
        self.priority = priority
        self.notes = notes

    def __repr__(self):
        #set the style for the features 
        import datetime
        print_attr = {'PURPLE': '\033[95m',
                      'CYAN': '\033[96m',
                      'DARKCYAN': '\033[36m',
                      'BLUE': '\033[94m',
                      'GREEN': '\033[92m',
                      'YELLOW': '\033[93m',
                      'RED': '\033[91m',
                      'BOLD': '\033[1m',
                      'UNDERLINE': '\033[4m',
                      'END': '\033[0m'}

        print_result = ''
        if self.priority:
            #print the priority
            print_result += print_attr['PURPLE'] + self.priority + print_attr['END'] + ' '
        print_result += print_attr['BOLD']+ print_attr['DARKCYAN'] + self.item + print_attr['END']

        if self.remind_time:
            #print remind time
            if datetime.datetime.now() > self.remind_time:
                print_result += '\n' + print_attr['RED'] + str(self.remind_time) + print_attr['END'] 
            else:
                print_result += '\n' + str(self.remind_time)
        
        if self.notes:
            #print notes
            print_result += '\n' + print_attr['UNDERLINE'] + self.notes + print_attr['END']
 
        return print_result

    def __str__(self):
        return self.__repr__()


    def modify_item(self,new_item=None):
        #ask users to enter the name of the event she/he wants to modify
        while True:
            new_item = input('What is your new task? ')
            if new_item != '':
                self.item = new_item
                break
            else:
                print('You must enter your task.')


    def modify_remind_time(self,new_remind_time=None):
        #ask user to enter the new remind time for the modified event
        import datetime
        while True:
            new_remind_string = input('What is your new remind time? (ex: 05/01/2018 23:01)')
            if new_remind_string == '':
                self.remind_time = None
                break
            try:
                new_remind_time = datetime.datetime.strptime(new_remind_string, "%m/%d/%Y %H:%M") 
                self.remind_time = new_remind_time
                break
            except:
                print('Invalid date format. Please refer to example.')
                
        

    def modify_priority(self,new_priority=None):
        #ask user to enter the new priority for the modified event
        while True:
            new_priority = input('What is your new priority?(ex:*/**/***) ')
            if new_priority == '':
                self.priority = None
                break
            elif new_priority in ['*','**','***']:
                self.priority = new_priority
                break
            else:
                print('Invalid priority format. Please refer to example.')


    def modify_notes(self,new_notes=None):
        #ask user to enter the new notes for the modified event
        new_notes = input('What is your new notes? ')
        if new_notes == '':
            self.notes = None
        else:
            self.notes = new_notes
            
            

    def modify(self):
        # ask the user if he/she wants to modify the selected event
        while True:
            change = input ('What feature would you like to change first? (Task/Time/Priority/Notes)')
            #ask user the feature that they want to modify
            if change in ['task','Task']:
                self.modify_item()
                break
            elif change in ['Time','time']:
                self.modify_remind_time()
                break
            elif change in ['priority','Priority']:
                self.modify_priority()
                break
            elif change in ['Notes','notes']:
                self.modify_notes()
                break
            else:
                print('Please enter the features with correct format: (Task/Time/Priority/Notes)')

        while True:
            # ask again if user wants to modify another feature 
            # and reask as long as the user wants to keeping changing the features
            question2=input('Would you like to modify other features of your event? ')
            if question2 in ['y','yes','Y','Yes']:
                while True:
                    change = input ('What feature would you like to change? (Task/Time/Priority/Notes)')
                    if change in ['task','Task']:
                        self.modify_item()
                        break
                    elif change in ['Time','time']:
                        self.modify_remind_time()
                        break
                    elif change in ['priority','Priority']:
                        self.modify_priority()
                        break
                    elif change in ['Notes','notes']:
                        self.modify_notes()
                        break
                    else:
                        print('Please enter the features with correct format: (Task/Time/Priority/Notes)')
            else:
                break 

