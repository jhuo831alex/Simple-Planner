from tkinter import messagebox
from tkinter import *
from tkinter import ttk

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
        self.var_lst = list()

        master.title('Simple Reminder')
        master.resizable(False, False)

        self.frame = Frame(master,bg = '#bed2e7')
        self.frame.pack()

        status = Label(master,text = "Proudly Presented by Jiahao, Jiakai, Xinxin and Yingyan",
                        bd=1,relief = SUNKEN, anchor = W, font = "Helvetica 10 italic" ,bg='#b8bfd8',fg='white',height =0)
        status.pack(side=BOTTOM,fill=X)

        Label(self.frame,text='Task',bg = '#bed2e7',fg = 'white',font = 'Helvetica 16 bold').grid(row = 0, column = 0, pady = 5,sticky=E)
        Label(self.frame,text='Date',bg = '#bed2e7', fg= 'white',font = 'Helvetica 16 bold').grid(row = 1, column = 0, pady = 5,sticky=E)
        Label(self.frame,text='Time',bg = '#bed2e7', fg= 'white',font = 'Helvetica 16 bold').grid(row = 2, column = 0, pady = 5,sticky=E)
        
        self.task_name = Entry(self.frame)
        self.task_name.grid(row=0,column = 1,padx=5,pady = 5,sticky=W,columnspan = 3)
        #self.time = Entry(self.frame)
        self.monthvar = StringVar(self.frame)
        self.monthvar.set("mm")
        month_option = OptionMenu(self.frame, self.monthvar,"01","02","03","04","05","06","07","08","09","10","11","12")
        month_option.grid(row=1,column=1,padx=5,pady = 5,sticky=W) 
        #self.time.grid(row=1,column = 1,padx=5,pady = 5,sticky=W)
        self.dayvar = StringVar(self.frame)
        self.dayvar.set("dd")
        day_list = [str(i).zfill(2) for i in range(1,32)] 
        day_option = OptionMenu(self.frame, self.dayvar,*day_list)
        day_option.grid(row=1,column=2,padx=5,pady = 5,sticky=W) 
        self.yearvar = StringVar(self.frame)
        self.yearvar.set("yyyy")
        year_option = OptionMenu(self.frame, self.yearvar,"2018","2019","2020","2021","2022")
        year_option.grid(row=1,column=3,padx=5,pady = 5,sticky=W)
        self.hourvar = StringVar(self.frame)
        self.hourvar.set("hr")
        hour_list = [str(i).zfill(2) for i in range(24)] 
        hour_option = OptionMenu(self.frame, self.hourvar,*hour_list)
        hour_option.grid(row=2,column=1,padx=5,pady = 5,sticky=W)
        self.minvar = StringVar(self.frame)
        self.minvar.set("min")
        min_list = [str(i).zfill(2) for i in range(60)] 
        min_option = OptionMenu(self.frame, self.minvar,*min_list)
        min_option.grid(row=2,column=2,padx=5,pady = 5,sticky=W,columnspan=2)

        Label(self.frame,text='Priority',bg = '#bed2e7',fg = 'white',font = 'Helvetica 16 bold').grid(row = 3, column = 0, pady = 5,sticky=E)
        self.var = StringVar(self.frame)
        self.var.set("None") 
        option = OptionMenu(self.frame, self.var, "None", "*", "**", "***")
        option.grid(row=3,column = 1,padx=5,pady = 5,sticky=W,columnspan=2)


        self.style = ttk.Style()
        # self.style.configure('TButton', background='black')
        self.style.configure('TButton', foreground='#b8bfd8')
        ttk.Button(self.frame,text='Add',command = self.update_reminder).grid(row = 0, column = 6,pady = 5)
        ttk.Button(self.frame,text='Edit',command = self.modify_event).grid(row = 1, column = 6,pady = 5)


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

            if len(self.event_list)==1:
                Label(self.frame,text='Reminder List',
                    bg = '#bed2e7',fg = 'white',font = 'Helvetica 20 bold underline').grid(row = 4,column = 0,pady = 5,columnspan = 3)

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
                        variable=var,
                        #fg = '#3b5998',
                        fg = 'white',
                        bg = '#bed2e7',
                        font = 'Helvetica 16',
                        command=lambda ni=n-1: self.removeCheckButton(ni))
            
            check.grid(row=n+4,column=0,sticky=W,columnspan=2)
            self.button_lst.append(check)
            self.var_lst.append(var)
    
    def modify_event(self):
        task = self.task_name.get()
        if task in self.event_list:
            for i in range(len(self.event_list)):
                if self.event_list[i]== task:
                    task = self.task_name.get()
                    # if self.time.get() != None:
                    #     time_value = self.time.get() 
                    # else:
                    time_value = self.time.get()
                    priority = self.var.get()

                    self.task_name.delete(0,END)
                    self.time.delete(0,END)
                    self.event_list[i]=task
                    self.time_lst[i]=time_value
                    self.priority_lst[i]=priority
                    
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


root = Tk()
reminder_gui = ReminderGUI(root)
root.mainloop()