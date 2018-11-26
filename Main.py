from Reminder_class import Reminder
from Event_class import Event

new_reminder = Reminder()
message = "Welcome to our awesome reminder!"
ask_User = input("What would you like to do? (Add Event/Modify Event/Check Event)")
if ask_User in ["Add Event", "add event","Add event", "Add","add"]:
    new_reminder.add_event()
    print(new_reminder)
elif ask_User in ["Modify Event","modify event","Modify event", "Modify","modify"]:
    new_reminder.event_list.modify()
elif ask_User in ["Check Event", "check event", "Check event", "Check", "check"]:
    new_reminder.check_event()
finish = "Finished!"
