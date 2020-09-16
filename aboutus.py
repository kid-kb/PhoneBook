from tkinter import *


class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("550x550+350+200")
        self.title("About Us")
        self.resizable(False, False)
        # --------------------------------------------------------------frames
        self.top = Frame(self, height=550, bg='#ffa550', width=550)
        self.top.pack(fill=BOTH)

        self.text=Label(self.top,text="Made with love and hard work by Keshav Bhalla"
                                      "\n U can see me on"
                                      "\n Codeforces link", font="sans 14 bold", bg='#ffa550')

        self.text.place(x=50, y=50)