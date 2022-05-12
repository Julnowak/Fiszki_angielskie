# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")



label2 = Label(root, text="Welcome")
label2.pack(pady=50)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady=20)

entryText = StringVar()
entry = Entry( root, textvariable=entryText )
entryText.set( "Hello World" )
entry.pack()

# Execute tkinter
root.mainloop()