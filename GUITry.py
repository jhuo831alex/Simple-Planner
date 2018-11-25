from tkinter import *


<<<<<<< HEAD
e=Event('item1')
fields = ('item','remind_time')

def get_new_item(entries):
    # item:
    item = entries['new_item'].get()
    print("item:", item)

def get_new_remind_time(entries):   
    # remind_time: 
    new_remind_time = entries['new_remind_time'].get()
    print('new_remind_time',new_remind_time)


    print("remind_time:", new_remind_time)

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0,"0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = Button(root, text='Show Event List',
          command=(lambda e=ents: get_new_item(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Add new event',
          command=(lambda e=ents: get_new_remind_time(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
=======


class App(object):

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.addFrame = Frame(master)
        self.addFrame.grid(row=0, column=0, columnspan=2, sticky='N')
        self.listFrame = Frame(master)
        self.listFrame.grid(row=1, column=0, columnspan=2, sticky='NW')
        self.todoList = []
        self.buttonList = []  #<--- button list is here now
        self.initUI()

    def initUI(self):

        self.entryBox = Entry(self.frame, width = 15)
        self.entryBox.grid(row=0, column=0, sticky='N')

        self.addButton = Button(self.frame, text="<-ADD->", command=self.add)
        self.addButton.grid(row=0, column=1, sticky='N')


    def removeCheckButton(self, button_no):
        # - CONFUSED HOW TO REMOVE THE SPECIFIC CHECKBUTTON
       # print(button_no, self.buttonList[button_no])
        #self.buttonList[button_no].grid_forget()
        self.buttonList[button_no].destroy()
       # del self.buttonList[button_no]
       # del self.todoList[button_no]


    def add(self):
        entry = self.entryBox.get()
        self.entryBox.delete(0, END)
        self.todoList.append(entry)
        print(self.todoList)
        var1 = IntVar()
        #self.buttonList = [] #<--- not sense having this here
      #  for n in range(len(self.todoList)): #<-- this for also very strange here.
        n = len(self.buttonList)
        lx = Checkbutton(self.listFrame,
                         text=self.todoList[n],
                         variable=self.todoList[n],
                         command=lambda ni=n: self.removeCheckButton(ni))
        lx.grid(row=n, column=0, sticky='NW')
        self.buttonList.append(lx)
         #   print(self.buttonList)


root = Tk()
app = App(root)
root.mainloop()
>>>>>>> 61b91a6296e0d263e8333be2d1f93910a272f647
