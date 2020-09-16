from tkinter import *
from PIL import Image, ImageTk
from PhoneBook import people
from PhoneBook import addpeople
from PhoneBook import aboutus
import datetime


dt = datetime.datetime.now().date()
dt = str(dt)


class Application(object):
    def about(self):
        aboutus.About()

    def addpplfn(self):
        addpeople.Addpeople()

    def my_ppl(self):
        people.Mypeople()

    def __init__(self, master):
        self.master = master

        # --------------------------------------------------------------frames
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bot = Frame(master, height=500, bg='#34baeb')
        self.bot.pack(fill=X)

        # ----------------------------------------------------------------image
        image = Image.open("icons/image.png")
        image = image.resize((70, 70), Image.ANTIALIAS)
        self.top_image = ImageTk.PhotoImage(image)
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=135, y=30)

        # ----------------------------------------------------------------heading
        self.heading = Label(self.top, text="My Phonebook App", font="arial 20 bold", fg="#ebb434")
        self.heading.place(x=260, y=50)

        # ------------------------------------------------------------------date
        self.date_lb = Label(self.top, text=dt, font="arial 12 bold", fg="#ebb434")
        self.date_lb.place(x=500, y=110)

        # -------------------------------------------------------------------view people
        self.view_ppl = Button(self.bot, text="  My People  ", font="arial 20 bold", bd=6, bg="white", fg="#ebb434",
                               command=self.my_ppl)
        self.view_ppl.place(x=270, y=70)

        # -------------------------------------------------------------------add people
        self.add_ppl = Button(self.bot, text=" Add People ", font="arial 20 bold", bd=6, bg="white", fg="#ebb434",
                              command=self.addpplfn)
        self.add_ppl.place(x=270, y=130)

        # -------------------------------------------------------------------about us
        self.about_us = Button(self.bot, text="   About Us   ", font="arial 20 bold", bd=6, bg="white", fg="#ebb434",
                               command=self.about)
        self.about_us.place(x=270, y=190)


def main():
    root = Tk()
    root.title("Phonebook")
    root.geometry("650x480+350+200")
    root.resizable(False, False)
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
