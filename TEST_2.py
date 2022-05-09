# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file="tło.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

label2 = Label(root, text="Welcome")
label2.pack(pady=50)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady=20)


# Execute tkinter
root.mainloop()