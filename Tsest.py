try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


class ScaleDemo(tk.Frame):
    def __init__(self, parent=tk.Tk()):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.parent = parent
        tk.Label(self, text="Scale/Slider").pack()
        self.var = tk.IntVar()
        self.scale1 = tk.Scale(self, label='volume',
                               command=self.onMove,
                               variable=self.var,
                               from_=0, to=255,
                               length=300, tickinterval=30,
                               showvalue='yes',
                               orient='horizontal')
        self.scale1.pack()

    def onMove(self, value):
        """ you can use value or self.scale1.get() """
        s = "moving = %s" % value
        # show result in the title
        self.parent.title(s)


ScaleDemo().mainloop()