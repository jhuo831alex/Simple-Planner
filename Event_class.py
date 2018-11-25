class Event:
    
    def __init__(self,item,remind_time = None,priority = None, notes = None):
        self.item = item
        self.remind_time = remind_time
        self.priority = priority
        self.notes = notes

    def __repr__(self):
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
            print_result += print_attr['PURPLE'] + self.priority + print_attr['END'] + ' '
        print_result += print_attr['BOLD']+ print_attr['DARKCYAN'] + self.item + print_attr['END']

        if self.remind_time:
            if datetime.datetime.now() > self.remind_time:
                print_result += '\n' + print_attr['RED'] + str(self.remind_time) + print_attr['END'] 
            else:
                print_result += '\n' + str(self.remind_time)
        
        if self.notes:
            print_result += '\n' + print_attr['UNDERLINE'] + self.notes + print_attr['END']
 
        return print_result

    def __str__(self):
        return self.__repr__()


    def modify_item(self,new_item=None):
        while True:
            new_item = input('What is your new item?')
            if new_item != '':
                self.item = new_item
                break
            else:
                print('You must enter your new_item')


    def modify_remind_time(self,new_remind_time=None):
        import datetime
        while True:
            new_remind_string = input('What is your new remind time?(ex: 05/01/2018 23:01)')
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
        while True:
            new_priority = input('What is your new priority?(ex:*/**/***)
            if new_priority == '':
                self.priority = None
                break
            try:
                new_priority in ['*','**','***']
                self.priority = new_priority
                break
            except:
                print('Invalid priority format. Please refer to example.')

    def modify_notes(self,new_notes=None):
        new_notes = input('What is your new notes?')
        if new_notes == '':
            self.notes = None
        else:
            self.notes = new_notes
            
            

    def modify(self):
        question=input('Do you want to modify your event?')
        if question in ['y','yes','Y','Yes']:
            while True:
                change = input ('What feature would you like to change first?')
                if change == 'item':
                    modify_item()
                    break
                elif change == 'remind_time':
                    modify_remind_time()
                    break
                elif change == 'priority':
                    modify_priority()
                    break
                elif change == 'notes':
                    modify_notes()
                    break
                else:
                    print('Please enter the features with correct format: item, remind_time, priority, notes')

        while True:
        question2=input('Do you want to modify other features of your event?')
        if question2 in ['y','yes','Y','Yes']:
            while True:
                change = input ('What feature would you like to change?')
                if change == 'item':
                    modify_item()
                    break
                elif change == 'remind_time':
                    modify_remind_time()
                    break
                elif change == 'priority':
                    modify_priority()
                    break
                elif change == 'notes':
                    modify_notes()
                    break
                else:
                    print('Please enter the features with correct format: item, remind_time, priority, notes')
        else:
            break 

