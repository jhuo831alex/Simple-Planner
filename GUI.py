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
        self.time_lst = list()
        self.priority_lst = list()
        self.button_lst = list()

        master.title('Simple Reminder')

        self.frame = ttk.Frame(master)
        self.frame.pack()
        self.bottom_frame = ttk.Frame(master)
        self.bottom_frame.pack(side = BOTTOM)

        ttk.Label(self.frame,text='Task').grid(row = 0, column = 0, pady = 5,sticky=W)
        ttk.Label(self.frame,text='Time').grid(row = 1, column = 0, pady = 5,sticky=W)

        self.task_name = ttk.Entry(self.frame)
        self.task_name.grid(row=0,column = 1,padx=5,pady = 5,sticky=W)
        self.time = ttk.Entry(self.frame)
        self.time.grid(row=1,column = 1,padx=5,pady = 5,sticky=W)

        ttk.Label(self.frame,text='Priority').grid(row = 3, column = 0, pady = 5,sticky=W)
        self.var = StringVar(self.frame)
        self.var.set("None") 
        option = OptionMenu(self.frame, self.var, "None", "*", "**", "***")
        option.grid(row=3,column = 1,padx=5,pady = 5,sticky=W)
        ttk.Button(self.frame,text='Add',command = self.update_reminder).grid(row = 0, column = 2,pady = 5)
        ttk.Button(self.frame,text='Edit',command = self.modify_event).grid(row = 1, column = 2,pady = 5)

    def removeCheckButton(self,button_num):
        self.button_lst[button_num].destroy()

        
    def update_reminder(self):
        task = self.task_name.get()
        time_value = self.time.get()
        priority = self.var.get()

        if task: 
            self.task_name.delete(0,END)
            self.time.delete(0,END)

            self.event_list.append(task)
            self.time_lst.append(time_value)
            self.priority_lst.append(priority)

            display_text = ''
            if priority != 'None':
                display_text += priority + ' '
            display_text  += task
            if time_value:
                display_text += '\n'+ time_value 

            n = len(self.event_list)
            var = IntVar()

            check = Checkbutton(self.frame,
                        wraplength = 220,
                        text=display_text,
                        variable=task,
                        fg = "#6897bb",
                        command=lambda ni=n-1: self.removeCheckButton(ni))
            
            check.grid(row=n+3,column=0,sticky=W,columnspan=2)
            self.button_lst.append(check)
    
    def modify_event(self):
        self.task = self.task_name.get()
        if self.task in self.event_list:
            time_value = self.time.get()
            priority = self.var.get()
            new_event = Event(self.task_name.get())
            self.task_name.delete(0,END)
            self.event_list.append(new_event)
            n = len(self.event_list)
            var = IntVar()

            check = Checkbutton(self.frame,
                        text=self.event_list[n-1],
                        variable=self.event_list[n-1],
                        command=lambda ni=n-1: self.removeCheckButton(ni))
            
            check.grid(row=n+3,column=0,sticky=W,columnspan=2)
            self.button_lst.append(check)

root = Tk()
reminder_gui = ReminderGUI(root)
root.mainloop()