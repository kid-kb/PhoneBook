from tkinter import *
from PIL import Image, ImageTk
import _sqlite3


con = _sqlite3.connect('database.db')
cur = con.cursor()


class Display(Toplevel):
    def __init__(self, index):
        Toplevel.__init__(self)
        self.geometry("650x480+350+200")
        self.title("Display Person")
        self.resizable(False, False)
        self.index = index
        # --------------------------------------------------------------frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bot = Frame(self, height=500, bg='#ebb134')
        self.bot.pack(fill=X)

        # ----------------------------------------------------------------image
        image = Image.open("icons/peopleimg.jpg")
        image = image.resize((70, 70), Image.ANTIALIAS)
        self.top_image = ImageTk.PhotoImage(image)
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=135, y=30)

        # ----------------------------------------------------------------heading
        self.heading = Label(self.top, text="Person Details", font="arial 20 bold", fg="#34baeb")
        self.heading.place(x=260, y=50)

        q = "select * from 'addressbook' where person_id = '{}'".format(index)
        result = cur.execute(q).fetchone()
        p_nm = result[1]
        p_snm = result[2]
        p_em = result[3]
        p_ph = result[4]
        p_add = result[5]

        # ------------------------------------------------------------------name
        self.label_name = Label(self.bot, text="First Name", font="arial 15 bold", fg="white", bg="#fcc324")
        self.label_name.place(x=40, y=40)

        self.e_n = Entry(self.bot, width=30, bd=4)
        self.e_n.insert(0, p_nm)
        self.e_n.config(state="disabled")
        self.e_n.place(x=150, y=40)

        # ------------------------------------------------------------------surname
        self.label_sname = Label(self.bot, text="Surname", font="arial 15 bold", fg="white", bg="#fcc324")
        self.label_sname.place(x=40, y=80)

        self.e_sn = Entry(self.bot, width=30, bd=4)
        self.e_sn.insert(0, p_snm)
        self.e_sn.config(state="disabled")
        self.e_sn.place(x=150, y=80)

        # ------------------------------------------------------------------email
        self.label_email = Label(self.bot, text="Email", font="arial 15 bold", fg="white", bg="#fcc324")
        self.label_email.place(x=40, y=120)

        self.e_e = Entry(self.bot, width=30, bd=4)
        self.e_e.insert(0, p_em)
        self.e_e.config(state="disabled")
        self.e_e.place(x=150, y=120)

        # ------------------------------------------------------------------phn no
        self.label_phn = Label(self.bot, text="Phone Number", font="arial 15 bold", fg="white", bg="#fcc324")
        self.label_phn.place(x=40, y=160)

        self.e_ph = Entry(self.bot, width=30, bd=4)
        self.e_ph.insert(0, p_ph)
        self.e_ph.config(state="disabled")
        self.e_ph.place(x=150, y=160)

        # ------------------------------------------------------------------address
        self.label_add = Label(self.bot, text="Address", font="arial 15 bold", fg="white", bg="#fcc324")
        self.label_add.place(x=40, y=200)

        self.e_add = Text(self.bot, width=40, height=4)
        self.e_add.insert(1.0, p_add)
        self.e_add.config(state="disabled")
        self.e_add.place(x=150, y=200)

