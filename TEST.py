from tkinter import *
from PIL import Image, ImageTk

from Tkinter import *
import PIL.Image
import PIL.ImageTk

root = Toplevel()

im = PIL.Image.open("photo.png")
photo = PIL.ImageTk.PhotoImage(im)

label = Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()

root.mainloop()