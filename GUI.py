from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from Event_class import Event
# from Reminder_class import Reminder

class Event:

    def __init__(self,task):
        self.task = task

    def __repr__(self):
        return self.task 

    def __str__(self):
        return self.__repr__()

class Reminder:
    
    def __init__(self,event_list = list()):
        self.event_list = event_list
    
    def add_event(self,task_title):
        new_event = Event(task_title)
        self.event_list.append(new_event)

class ReminderGUI:

    #reminder = Reminder()

    def __init__(self,master):
        self.event_list = list()

        master.title('Simple Reminder')

        self.frame = ttk.Frame(master)
        self.frame.pack()

<<<<<<< HEAD
        ttk.Button(self.frame, text = 'Add Task',command = self.add_task).grid(row = 0, column = 1, padx = 5, pady = 5)
        #ttk.Button(self.frame, text = 'Print Reminder',command = self.print_reminder).grid(row = 1, column = 1, padx = 5, pady = 5)
        for i in range(len(self.event_list)):
            label = ttk.Label(self.frame, text= str(self.event_list[i]))
            label.grid(row=2+i,column=1)

=======
        ttk.Button(self.frame, text = 'Add Task',command = self.add_task).grid(row = 0, column = 0, padx = 5, pady = 5)
        ttk.Button(self.frame, text = 'Print Reminder',command = self.print_reminder).grid(row = 0, column = 0, padx = 5, pady = 5)
        #Entry(self.frame).grid(row=0,column=0,padx = 5, pady = 5)
>>>>>>> 4d0e49d89451b56a7360fd8f7cb7000ba5b6fecb

    def add_task(self):
        new_event = Event('yes')
        self.event_list.append(new_event)
<<<<<<< HEAD
    
    # def print_reminder(self):
    #     for i in range(len(self.event_list)):
            

    #         label = ttk.Label(self.frame, text= str(self.event_list[i]))
    #         label.grid(row=2+i,column=1)
=======
        

    def print_reminder(self):
        for i in range(len(self.event_list)):
            var = IntVar()
            Checkbutton(self.frame,text=str(self.event_list[i]),variable = var).grid(row=2+i,column=0)
            # label = ttk.Label(self.frame, text= str(self.event_list[i]))
            # # this creates x as a new label to the GUI
            # label.grid(row=2+i,column=0)
>>>>>>> 4d0e49d89451b56a7360fd8f7cb7000ba5b6fecb
        


              
root = Tk()
reminder_gui = ReminderGUI(root)
root.mainloop()