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
        print_result += print_attr['BOLD']+ print_attr['DARKCYAN'] + self.item + print_attr['END'] +'\n'

        print_result = ''
        if self.priority:
            print_result += print_attr['PURPLE'] + self.priority + print_attr['END'] + ' '
        print_result += print_attr['BOLD']+ print_attr['CYAN'] + self.item + print_attr['END'] +'\n'


        if self.remind_time:
            if datetime.datetime.now() > self.remind_time:
                print_result += print_attr['RED'] + str(self.remind_time) + print_attr['END'] + "\n"
            else:
                print_result += self.remind_time + "\n"
        
        if self.notes:
            print_result += print_attr['UNDERLINE'] + self.notes + print_attr['END']
 
        return print_result
        

    # def modify_notes(self,new_item = None, new_remind_time = None, new_priority=None, new_notes=None):
    #     question=input('Do you want to modify your event?')
    #     if question in ['y','yes','Y','Yes']:
    #         features = input('What features of this event do you want to change? (Please enter: item, remind_time, priority, or notes)').split()
    #         for feature in features:
    #             if feature == 'item':
    #                 new_item = input('What is your new item?')
    #                 self.item = new_item
    #             else if feature == 'remind_time':
    #                 new_remind_time = input('What is your new remind time?')
    #                 self.remind_time = new_remind_time
    #             else if feature == 'priority':
    #                 new_priority = input('What is your new priority?')
    #                 self.priority = new_priority
    #             else if feature == 'notes':
    #                 new_notes = input('What is your new notes?')
    #                 self.notes = new_notes

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

