# A script that integrates all the functions in Reminder and Event classes 
# in order to execute in command line. 
from Reminder_class import Reminder
from Event_class import Event

def main():
    new_reminder = Reminder()
    message = "Welcome to our awesome reminder!"
    while True:
        ask_User = input("What would you like to do? (Add Event/Modify Event/Check Event/Quit)")
        if ask_User in ["Add Event", "add event","Add event", "Add","add"]:
            new_reminder.add_event()
            print(new_reminder)
        elif ask_User in ["Modify Event","modify event","Modify event", "Modify","modify"]:
            print(new_reminder)
            while True:
                question = input("Which event would you like to modify? (Event number)") 
                try:
                    new_reminder.event_list[int(question)-1].modify()
                    print(new_reminder)
                    break
                except:
                    print("No such event.")
                    break            
        elif ask_User in ["Check Event", "check event", "Check event", "Check", "check"]:
            new_reminder.check_event()
            print(new_reminder)
        elif ask_User in ["Quit", "quit"]:
            print("Byebye.")
            break
        else:
            print("Invalid input. Please refer to example.")

