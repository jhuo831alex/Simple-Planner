class Reminder:
    
    def __init__(self,category = "Reminder", event_list = list()):
        self.category = category
        self.event_list = event_list

    def __repr__(self):
        print_str = ''
        print_str += '\033[1m' + self.category + '\033[0m' + '\n\n'
        count = 1

        for event in self.event_list:
            print_str += '----------[' + str(count) + "]----------\n"
            print_str += str(event) + '\n\n'
            count += 1
        return print_str

    #methods
    def prompt_user(self,prompt_msg):
        input_ = input(prompt_msg)
        if input_ in ['y','yes','Y','Yes']:
            result = True
        else:
            result = False
        return result

    def add_event(self):

        from datetime import datetime
        from Event_class import Event

        item_ = input('What task would you like to add?')

        if_remind = self.prompt_user('Would you like to be reminded on a day? (y/n)')
        if if_remind:
            while True:
                date_string = input('What time would you like to be reminded? (ex: 05/01/2018 23:01)')
                try:
                    date_time = datetime.strptime(date_string, "%m/%d/%Y %H:%M")
                    break
                except:
                    print('Invalid date format. Please refer to example.')
        else:
            date_time = None

        if_priority = self.prompt_user('Would you like to set a priority? (y/n)')
        if if_priority:
            while True:
                priority_string = input('Which priority level would you like to assign to this task? (*/**/***)')
                if priority_string in ['*','**','***']:
                    break
                else:
                    print('Invalid priority level. Please refer to example.')
        else:
            priority_string = None

        if_notes = self.prompt_user('Would you like to add notes? (y/n)')
        if if_notes:
            notes = input("What notes would you like to add to this task?")
        else:
            notes = None
        
        new_event = Event(item_,date_time,priority_string,notes)
        self.event_list.append(new_event)

    def check_event(self):
        print(self.__repr__())
        while True:
            item_to_delete = input("Which task did you complete? (Input task number)")
            try:
                self.event_list.pop(int(item_to_delete)-1)
                break
            except:
                print('Invalid task number. Please refer to example.')



       

