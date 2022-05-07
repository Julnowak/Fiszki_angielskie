import tkinter as tk


def show_message():
    label = tk.Label(root, text="Hello, world!",
                     background="red",
                     foreground="white")
    label.place(anchor="n", relx=.5, y=0)
    label.after(1500, label.destroy)


root = tk.Tk()
root.geometry("600x200")

button = tk.Button(root, text="Show message", command=show_message)
button.pack(side="bottom")

root.mainloop()