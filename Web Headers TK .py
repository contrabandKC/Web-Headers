from tkinter import *
from tkinter import ttk




def out_put():

    f = open(user_file.get())


    fh = open(file_to_save.get(), 'w')


    lines = f.readlines()

    headings = str(lines)

    for idx in lines:
        if idx.startswith('<h1>'):

            print(str(idx).strip().replace('<h1>','*').replace('</h1>',''), file=fh)
    f.close()
    fh.close()

root = Tk()
root.title("Web Header")
mainframe = ttk.Frame(root) #padding="20 5 15 15")
mainframe.grid(column=0, row=0)#, sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=100)
# mainframe.rowconfigure(0, weight=30)


user_file = StringVar()

file_to_save = StringVar()

user_input = ttk.Entry(mainframe,width = 7, textvariable = user_file)
user_input.grid(column = 2, row = 1, sticky = (W,E))
user_output =ttk.Entry(mainframe,width = 7, textvariable = file_to_save)
user_output.grid(column = 2, row = 2, sticky = (W,E))

ttk.Label(mainframe, text='Enter HTML file to open').grid(column = 1, row = 1, sticky = E)
ttk.Label(mainframe, text = 'Enter name of html file to write to').grid(column = 1,row = 2, sticky = E)

ttk.Button(mainframe,text = 'Run',command = out_put).grid(column = 2, row = 3)




root.mainloop()