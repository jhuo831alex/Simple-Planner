from tkinter import messagebox
from tkinter import *
from tkinter import ttk

class ReminderGUI:
    """
    This is the class used for implementing our reminder and event command line, and
    it will show a GUI version of our reminder.
    """

    def __init__(self,master):
        #initialize the list for each feature
        self.event_list = list()
        self.time_lst = list()
        self.priority_lst = list()
        self.button_lst = list()
        self.var_lst = list()

        #set title and size
        master.title('Simple Reminder')
        master.resizable(False, False)
        
        #set frame and background
        self.frame = Frame(master,bg = '#bed2e7')
        self.frame.pack()

        #label group members on the bottom of the window
        status = Label(master,text = "Proudly Presented by Jiahao, Jiakai, Xinxin and Yingyan",
                        bd=1,relief = SUNKEN, anchor = W, font = "Helvetica 10 italic" ,bg='#b8bfd8',fg='white',height =0)
        status.pack(side=BOTTOM,fill=X)

        #set the text style and location for each feature of the event on the window
        Label(self.frame,text='Task',bg = '#bed2e7',fg = 'white',font = 'Helvetica 16 bold').grid(row = 0, column = 0, pady = 5,sticky=E)
        Label(self.frame,text='Date',bg = '#bed2e7', fg= 'white',font = 'Helvetica 16 bold').grid(row = 1, column = 0, pady = 5,sticky=E)
        Label(self.frame,text='Time',bg = '#bed2e7', fg= 'white',font = 'Helvetica 16 bold').grid(row = 2, column = 0, pady = 5,sticky=E)
        
        #set the text style and location for user-input name of the event
        self.task_name = Entry(self.frame)
        self.task_name.grid(row=0,column = 1,padx=5,pady = 5,sticky=W,columnspan = 3)

        #set the text style and location for user-input month of the event
        self.monthvar = StringVar(self.frame)
        self.monthvar.set("mm")
        month_option = OptionMenu(self.frame, self.monthvar,"01","02","03","04","05","06","07","08","09","10","11","12")
        month_option.grid(row=1,column=1,padx=5,pady = 5,sticky=W) 

        #set the text style and location for user-input date of the event
        self.dayvar = StringVar(self.frame)
        self.dayvar.set("dd")
        day_list = [str(i).zfill(2) for i in range(1,32)] 
        day_option = OptionMenu(self.frame, self.dayvar,*day_list)
        day_option.grid(row=1,column=2,padx=5,pady = 5,sticky=W) 

        #set the text style and location for user-input year of the event
        self.yearvar = StringVar(self.frame)
        self.yearvar.set("yyyy")
        year_option = OptionMenu(self.frame, self.yearvar,"2018","2019","2020","2021","2022")
        year_option.grid(row=1,column=3,padx=5,pady = 5,sticky=W)

        #set the text style and location for user-input hour of the event
        self.hourvar = StringVar(self.frame)
        self.hourvar.set("hr")
        hour_list = [str(i).zfill(2) for i in range(24)] 
        hour_option = OptionMenu(self.frame, self.hourvar,*hour_list)
        hour_option.grid(row=2,column=1,padx=5,pady = 5,sticky=W)

        #set the text style and location for user-input minute of the event
        self.minvar = StringVar(self.frame)
        self.minvar.set("min")
        min_list = [str(i).zfill(2) for i in range(60)] 
        min_option = OptionMenu(self.frame, self.minvar,*min_list)
        min_option.grid(row=2,column=2,padx=5,pady = 5,sticky=W,columnspan=2)

        #set the text style and location for priority of the event
        Label(self.frame,text='Priority',bg = '#bed2e7',fg = 'white',font = 'Helvetica 16 bold').grid(row = 3, column = 0, pady = 5,sticky=E)
        self.var = StringVar(self.frame)
        self.var.set("None") 
        #ask the user to choose priority for the event
        option = OptionMenu(self.frame, self.var, "None", "*", "**", "***")
        option.grid(row=3,column = 1,padx=5,pady = 5,sticky=W,columnspan=2)

        #add two buttons: "add" and "edit"
        self.style = ttk.Style()
        self.style.configure('TButton', foreground='#b8bfd8')
        ttk.Button(self.frame,text='Add',command = self.update_reminder).grid(row = 0, column = 6,pady = 5)
        ttk.Button(self.frame,text='Edit',command = self.modify_event).grid(row = 1, column = 6,pady = 5)

    # delete the event after user checks the checkbox
    def removeCheckButton(self,button_num):
        print(button_num)
        print(self.button_lst)
        self.button_lst[button_num].destroy()
    
    # method
    # add new event
    def update_reminder(self):
        task = self.task_name.get()
        month_value = self.monthvar.get()
        day_value = self.dayvar.get()
        year_value = self.yearvar.get()
        hour_value = self.hourvar.get()
        min_value = self.minvar.get()
        priority = self.var.get()

        self.monthvar.set('mm')
        self.dayvar.set('dd')
        self.yearvar.set('yyyy')
        self.hourvar.set('hr')
        self.minvar.set('min')
        self.var.set('None')

        if task: 
            #append event and its features to their lists 
            #and remove the content of the label after event created
            self.task_name.delete(0,END)

            self.event_list.append(task)
            self.time_lst.append([month_value,day_value,year_value,hour_value,min_value])
            self.priority_lst.append(priority)

            if len(self.event_list)==1:
                Label(self.frame,text='Reminder List',
                    bg = '#bed2e7',fg = 'white',font = 'Helvetica 20 bold underline').grid(row = 4,column = 1,pady = 5,columnspan = 3)

            display_text = ''
            if priority != 'None':
                display_text += priority + ' '
            display_text  += task
            if month_value != 'mm' and day_value != 'dd' and year_value != 'yyyy':
                display_text += '\n'+ month_value + '-' + day_value + '-' + year_value + ' ' 
                if hour_value != 'hr' and min_value != 'min':
                    display_text += hour_value + ':' + min_value
            

            n = len(self.button_lst) + 1
            var = IntVar()

            #set the style of the event information displayed 
            check = Checkbutton(self.frame,
                        wraplength = 300,
                        text=display_text,
                        variable=var,
                        fg = 'white',
                        bg = '#bed2e7',
                        font = 'Helvetica 16',
                        command=lambda ni=n-1: self.removeCheckButton(ni))
            
            check.grid(row=n+4,column=0,columnspan=7,sticky=W,padx=20)
            self.button_lst.append(check)
            self.var_lst.append(var)
    
    # method
    # modify the event, including changing each feature of the event by 
    # removing the original one and recalling the add new event method
    def modify_event(self):
        task = self.task_name.get()
        if task in self.event_list:
            for i in range(len(self.event_list)):
                if self.event_list[i]== task:
                    self.removeCheckButton(i)   


            self.update_reminder()


root = Tk()
reminder_gui = ReminderGUI(root)
root.mainloop()