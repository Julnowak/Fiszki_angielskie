import tkinter as tk

def countdown(count):
    # change text in label
    mins = count//60
    sec = count - 60*mins
    label['text'] = mins
    label2['text'] = sec

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)

root = tk.Tk()

label = tk.Label(root)
label.place(x=35, y=15)
label2 = tk.Label(root)
label2.place(x=55, y=35)

# call countdown first time
countdown(100)
# root.after(0, countdown, 5)

root.mainloop()