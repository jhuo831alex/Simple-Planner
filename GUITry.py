from tkinter import *


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
