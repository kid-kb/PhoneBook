from tkinter import *
import _sqlite3
from PIL import Image, ImageTk
from PhoneBook import addpeople
from PhoneBook import updateppl
from PhoneBook import displayppl
from tkinter import messagebox

con = _sqlite3.connect('database.db')
cur = con.cursor()


class Mypeople(Toplevel):
    def del_ppl(self):
        selected_itm = self.list.curselection()
        itm = self.list.get(selected_itm)
        index = itm.split(".")[0]
        q = "delete from 'addressbook' where person_id = {}".format(index)
        ans=messagebox.askquestion("Warning","Do you want to delete")
        if ans == "Yes":
            try:
                cur.execute(q)
                con.commit()
                messagebox.showinfo("Sucess","Contact Deleted")
                self.destroy()
            except EXCEPTION as e:
                print(e)


    def up_ppl(self):
        selected_itm = self.list.curselection()
        itm = self.list.get(selected_itm)
        index = itm.split(".")[0]
        updateppl.Updatepeople(index)
        self.destroy()

    def dis_ppl(self):
        selected_itm = self.list.curselection()
        itm = self.list.get(selected_itm)
        index = itm.split(".")[0]
        displayppl.Display(index)


    def add_ppl(self):
        addpeople.Addpeople()
        self.destroy()

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x480+350+200")
        self.title("My People")
        self.resizable(False, False)

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
        self.heading = Label(self.top, text="My People ", font="arial 20 bold", fg="#34baeb")
        self.heading.place(x=260, y=50)

        self.scroll =Scrollbar(self.bot,orient=VERTICAL)
        self.list= Listbox(self.bot,width=40,height=20,yscrollcommand=self.scroll.set)
        self.list.grid(row=0, column=0, padx=(40,0))

        self.scroll.config(command=self.list.yview)
        self.scroll.grid(row=0, column=1, sticky=N+S)

        persons = cur.execute("select * from 'addressbook'").fetchall()
        c = 0
        for p in persons:
            self.list.insert(c,str(p[0])+". "+str(p[1])+" "+str(p[2]))
            c += 1

        # -----------------------------------------------------------------buttons

        btnadd = Button(self.bot, text="Add", width=12, font="Sans 12 bold", command=self.add_ppl)
        btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btnup = Button(self.bot, text="Update", width=12, font="Sans 12 bold",command=self.up_ppl)
        btnup.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btndis = Button(self.bot, text="Display", width=12, font="Sans 12 bold",command=self.dis_ppl)
        btndis.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btndel = Button(self.bot, text="Delete", width=12, font="Sans 12 bold",command=self.del_ppl)
        btndel.grid(row=0, column=2, padx=20, pady=130, sticky=N)
