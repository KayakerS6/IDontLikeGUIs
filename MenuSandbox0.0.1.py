'''TO DO:
Logo doesn't display properly; need to use a monospace font
Add buttons
Add additional screens that can be navigated to with the afore mentioned buttons
Add text input fields'''


from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("PassPY")
class tkinter.font.Font(family = Courier)
label = Label(root, text ='________                     __________  __\n___  __ \_____ _________________  __ \ \/ /\n__  /_/ /  __ `/_  ___/_  ___/_  /_/ /_  / \n_  ____// /_/ /_(__  )_(__  )_  ____/_  /  \n/_/     \__,_/ /____/ /____/ /_/     /_/   \n\n\n\n\n').pack()


label2 = Label(root, text = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG \nthe quick brown fox jumps over the lazy dog').pack()




root.mainloop()
