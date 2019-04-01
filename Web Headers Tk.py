##########################################################################
# CS 101
# Program : 4 Web Headers
# Name Erik Marquez
# Email eemxr9@mail.umkc.edu
# PROBLEM : Web Headers - Take input from a user. open a txt file and return the headers from that file
# ALGORITHM :
#   1. Ask user for a file to open
#   2. Validate the input
#   3. Ask user for a file to save to
#   4. Validate the input
#   5. Repeat
#   6. User Quit button
# ERROR HANDLING:
# Any Special Error handling to be noted: Tried to figure out how to change the color on the status bar.
#                                         Could not figure it out.
# COMMENTS: This is my TkInter Attempt. I also turned in the regular assignment.
# Any special comments
###########################################################################

from tkinter import *
from tkinter import ttk




headers = ('<h1>','<h2>','<h3>','<h4>','<h5>','<h6>','<h7>','<h8>',)

# umkc works

# Tried to break into multiple functions and but had trouble since it was my first time using TKinter

def header_script():
    """Main script -
    Take input and output names - Validate names
    search for headers
    close files
    """
    try:
        fh =open(user_file.get())
        lines = fh.readlines()

    except FileNotFoundError:
        satus.set("File not found '{}'. Please enter a valid file".format(user_file.get()))



    try:
        sv =open(file_to_save.get(),'w')
        print('Here are your headers!\n', file=sv)

    except IOError:
        satus.set("IO Error {}. Please enter a valid file".format(file_to_save.get()))

    try:
        for idx in lines:
            idx = idx.strip()
            if idx[0:4] in headers:
                key = headers.index(idx[0:4])
                print(('\t'* key),idx[4:len(idx)-5], file=sv)
                print(('\t' * key), idx[4:len(idx) - 5])
        print('\n\nThank you for using Web Headers!\n', file=sv)
        fh.close()
        sv.close()

    except UnboundLocalError:
        print('Nothing to iterate')



    satus.set("Successfully output to file '{}'".format(file_to_save.get()))



## Tk Code
## Sorry for slopy code. My first time using TKinter

# Tk Main windW
root = Tk()
root.title("Web Headers")
root.configure(background = '#EEEEEE')

title = Label(root, text ='Welcome to Web Headers', font = 'Times 30 bold',background = '#EEEEEE',justify = CENTER).grid(column = 1,row=0 ,columnspan=3,sticky = N)


# String Variables
user_file = StringVar()
file_to_save = StringVar()
satus = StringVar()
satus.set('Ready')



# user input Entry boxes
user_input = ttk.Entry(root, width = 30,textvariable = user_file).grid(column = 2, row = 3,sticky = W)
user_save = ttk.Entry(root, width = 30,textvariable = file_to_save).grid(column = 2, row = 4, sticky = W)

# Labels. Some with text and some are spacers
ttk.Label(root, text ='Enter HTML file to open ==>').grid(column = 1, row = 3, sticky = E)
save_label = ttk.Label(root, text ='Enter name of html file to write to ==>').grid(column = 1, row = 4, sticky = W)

status_label = Label(root, textvariable = satus,relief=SUNKEN, bd = 3,padx=20, anchor = W,background = '#EEEEEE').grid(column = 1, row = 8,columnspan=10,sticky = "we")

ttk.Label(root).grid(column = 1, row = 7,columnspan=10,sticky = "we")
ttk.Label(root).grid(column = 1, row = 5,columnspan=10,sticky = "we")
ttk.Label(root).grid(column = 0, row = 1,columnspan=10,sticky = "we")
ttk.Label(root).grid(column = 0, row = 0)


# buttons
submit = ttk.Button(root, text = "Submit",command = header_script).grid(column = 2, row = 6, sticky = W)

exit_button =ttk.Button(root, text = "Quit",command = root.destroy).grid(column = 3, row = 6, sticky = W)



# main loop and size of window
root.geometry("625x225+100+100")
root.resizable(width=False,height=False)
root.mainloop()





