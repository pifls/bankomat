"""from tkinter import *
from tkinter import messagebox
import sqlite3


ARIAL = ("arial",10,"bold")

class Bank:
    def __init__(self,root):
        self.conn = sqlite3.connect("atm_databse.db", timeout=100)
        self.login = False
        self.root = root
        self.header = Label(self.root,text="R~R BANK",bg="#50A8B0",fg="white",font=("arial",20,"bold"))
        self.header.pack(fill=X)
        self.frame = Frame(self.root,bg="#728B8E",width=600,height=400)
        #Login Page Form Components
     #   self.userlabel =Label(self.frame,text="Account Number",bg="#728B8E",fg="white",font=ARIAL)
      #  self.uentry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",
          # highlightthickness=2,
         #   highlightbackground="white")
      #  self.plabel = Label(self.frame, text="Password",bg="#728B8E",fg="white",font=ARIAL)
      #  self.pentry = Entry(self.frame,bg="honeydew",show="*",highlightcolor="#50A8B0",
        #   highlightthickness=2,
        #    highlightbackground="white")
      #  self.button = Button(self.frame,text="LOGIN",bg="#50A8B0",fg="white",font=ARIAL)
        self.q = Button(self.frame,text="Quit",bg="#50A8B0",fg="white",font=ARIAL,command = self.root.destroy)
      #  self.userlabel.place(x=145,y=100,width=120,height=20)
      #  self.uentry.place(x=153,y=130,width=200,height=20)
    #    self.plabel.place(x=125,y=160,width=120,height=20)
      #  self.pentry.place(x=153,y=190,width=200,height=20)
    #    self.button.place(x=155,y=230,width=120,height=20)
        self.q.place(x=480,y=360,width=120,height=20)


      #  self.frame.pack()

        frame = Frame(self.root,bg="#728B8E",width=800,height=400)
        root.geometry("800x400")
        detail = Button(self.frame,text="Account Details",bg="#50A8B0",fg="white",font=ARIAL,command=self.account_detail)
        enquiry = Button(self.frame, text="Balance Enquiry",bg="#50A8B0",fg="white",font=ARIAL,command= self.Balance)
        deposit = Button(self.frame, text="Deposit Money",bg="#50A8B0",fg="white",font=ARIAL,command=self.deposit_money)
        withdrawl = Button(self.frame, text="Withdrawl Money",bg="#50A8B0",fg="white",font=ARIAL,command=self.withdrawl_money)
        q = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font=ARIAL, command=self.root.destroy)
        detail.place(x=0,y=0,width=200,height=50)
        enquiry.place(x=0, y=315, width=200, height=50)
        deposit.place(x=600, y=0, width=200, height=50)
        withdrawl.place(x=600, y=315, width=200, height=50)
        q.place(x=340, y=340, width=120, height=20)
        frame.pack()


        database_fetch()
        text = self.acc_list[0]+"\n"+self.acc_list[1]+"\n"+self.acc_list[2]
        label = Label(self.frame,text=text,font=ARIAL)
        label.place(x=200,y=100,width=300,height=100)


        database_fetch()
        label = Label(self.frame, text=self.acc_list[3],font=ARIAL)
        label.place(x=200, y=100, width=300, height=100)

    def deposit_money(self):
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",
           highlightthickness=2,
            highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL)

        self.money_box.place(x=200,y=100,width=200,height=20)
        self.submitButton.place(x=445,y=100,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.deposit_trans)

    def deposit_trans(self,flag):
        self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)
        self.conn.execute("update atm set bal = bal + ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()

    def withdrawl_money(self):
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",
           highlightthickness=2,
            highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL)

        self.money_box.place(x=200,y=100,width=200,height=20)
        self.submitButton.place(x=445,y=100,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.withdrawl_trans)

    def withdrawl_trans(self,flag):
        self.label = Label(self.frame, text="Money Withdrawl !", font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)
        self.conn.execute("update atm set bal = bal - ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()



root = Tk()
root.title("Sign In")
root.geometry("600x420")
#icon = PhotoImage(file="icon.png")
root.tk.call()
obj = Bank(root)
root.mainloop()
"""
"""
import tkinter  as tk
from tkinter import *

window = tk.Tk()
window.geometry("600x400")
window.title("Cash machine")


def account_detail():
  wyplata = Button(text="Wypłata", command = wyplataFunction)
  wplata = Button(text="Wpłata")
  stan = Button(text="Sprawdź stan konta")
  przelew = Button(text="Dokonaj przelewu")
  Frame.destroy(but1)
  Frame.destroy(textbox)
  Frame.destroy(confirmButton)
  wyplata.pack()
  wplata.pack()
  stan.pack()
  przelew.pack()

def wyplataFunction():
      # Frame.destroy(wyplata)
      #  Frame.destroy(wplata)
      # Frame.destroy(stan)
      # Frame.destroy(przelew)
  wplata = Button(text="Wpłata")
  wplata.config(state="disabled")
  ile = Entry(text="Wpisz ile chcesz wypłacic")
  ile.pack()

def quitFunction():
    Frame.destroy(wyplata)
    Frame.destroy(wplata)
    Frame.destroy(stan)
    Frame.destroy(przelew)



but1 = tk.Button(window, text="Proszę włożyć kartę i podać PIN", bg = "dark green", padx=100, pady=20, activebackground = "#ff0000")
but1.pack(side = tk.TOP)
textbox = tk.Entry() #window, width = 8, height = 2)
textbox.pack()
confirmButton = tk.Button(window, text="Zatwierdź", bg = "light blue", padx= 50, pady= 10,command = account_detail)
confirmButton.pack()

quitButton = tk.Button(window, text="Wstecz", command = quitFunction)
quitButton.pack()


window.mainloop()
"""
import tkinter as tk                # python 3
from tkinter import *
from tkinter import messagebox
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self,width=500, height=500)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Wyplata, PageTwo, Prepaid, Inna, Stan, Transfer, PINPage, Drukparagon, Koniec, Transfer2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PINPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,width=1000, height=500)
        self.controller = controller
        label = tk.Label(self, text="Bankomat", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Wypłata", relief = "solid",
                            command=lambda: controller.show_frame("Wyplata"))
        button2 = tk.Button(self, text="Zdeponowanie", relief = "solid",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Doładowanie pre-paid", relief = "solid",
                            command=lambda: controller.show_frame("Prepaid"))
        button4 = tk.Button(self, text="Stan karty", relief = "solid",
                            command=lambda: controller.show_frame("Stan"))
        button5 = tk.Button(self, text="Dokonaj przelewu", relief = "solid",
                            command=lambda: controller.show_frame("Transfer"))
        button6 = tk.Button(self, text="pin", relief = "solid",
                            command=lambda: controller.show_frame("PINPage"))

        button1.pack()#padx=5, pady=10, side=tk.LEFT)
        button1.place(x=10, y=60)
        button2.pack()
        button2.place(x=10,y=100)#padx=5, pady=20, side=tk.LEFT)
        button3.pack()
        button3.place(x=10,y=140)#padx=5, pady=30, side=tk.LEFT)
        button4.pack()
        button4.place(x=410,y=60)
        button5.pack()
        button5.place(x=410, y=100)
    #    button6.pack()
   #     button6.place(x=410, y=140)


class PINPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        a = 3
        def calld():
            a = entry.get()
            b = a
            if b != "1111":
                messagebox.showerror("error", "PIN jest niepoprawny")
            elif b == "1111":

                controller.show_frame("StartPage")

        label = tk.Label(self, text="Podaj PIN:")
        label.pack()
   #     var1 = StringVar()
        entry = tk.Entry(self)#, texvariable = var1)
        entry.pack()
        entryString = entry.get()
        a = "1111"
        label3 = tk.Label(text=entryString)
        label3.pack()
        if entryString == a:
            messagebox.showerror("error", "try again")
   #     tekst = "1111"
  #      if var1 == tekst:
   #         b = 6
        button8 = tk.Button(self, text="Przejdź dalej", command= calld)
        button8.pack()

class Wyplata(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Wybierz kwotę jaką chcesz wypłacić:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Wróć",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, relief = "solid", text="50 zł", command=lambda: controller.show_frame("Drukparagon"))
        button2 = tk.Button(self, relief = "solid", text="20 zł", command=lambda: controller.show_frame("Drukparagon"))
        button3 = tk.Button(self,relief = "solid", text="100 zł", command=lambda: controller.show_frame("Drukparagon"))
        button4 = tk.Button(self,relief = "solid", text="200 zł", command=lambda: controller.show_frame("Drukparagon"))
        button5 = tk.Button(self, relief = "solid",text="10 zł", command=lambda: controller.show_frame("Drukparagon"))
        button6 = tk.Button(self, relief = "solid", text="Inna kwota", command=lambda: controller.show_frame("Inna"))
        button.pack()
        button1.place(x=10, y=60)
        button2.pack()
        button2.place(x=10, y=100)  # padx=5, pady=20, side=tk.LEFT)
        button3.pack()
        button3.place(x=10, y=140)  # padx=5, pady=30, side=tk.LEFT)
        button4.pack()
        button4.place(x=410, y=60)
        button5.pack()
        button5.place(x=410, y=100)
        button6.pack()
        button6.place(x=410, y=140)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Dokonaj wpłaty", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Podaj kwotę, którą chcesz wpłacić:")
        label2.pack()
        entry = tk.Entry(self)
        entry.pack()
        buttonconf = tk.Button(self, text="Zatwierdź",command=lambda: controller.show_frame("Drukparagon"))
        buttonconf.pack()
        button = tk.Button(self, text="Wróć",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Prepaid(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Wybierz kwotę jaką chcesz doładować telefon:", font=15)#controller.title_font)
        label.pack(side="top", fill="x")
        entry = tk.Entry(self)
        entry.pack()
        button1 = tk.Button(self, text= "Zatwierdź",command=lambda: controller.show_frame("Drukparagon"))
        button1.pack()
        button = tk.Button(self, text="Wróć",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Inna(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Podaj kwotę:")
        label.pack()
        entry = tk.Entry(self)
        entry.pack()
        button1 = tk.Button(self, text="Zatwierdź", command=lambda: controller.show_frame("Drukparagon"))
        button1.pack()
        button = tk.Button(self, text="Wróć",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Drukparagon(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Czy wydrukować potwierdzenie?")
        buttonyes = tk.Button(self, text="Tak", command=lambda: controller.show_frame("Koniec"))
        buttonno = tk.Button(self, text="Nie", command=lambda: controller.show_frame("Koniec"))
        label.pack()
        buttonyes.pack()
        buttonno.pack()

class Koniec(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Odbierz paragon i wyjmij kartę")
        label.pack()
        button = tk.Button(self, text="Wróć",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Transfer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Podaj nr konta, na który chcesz dokonać przelewu:")
        label.pack()
        entry = tk.Entry(self)
        entry.pack()
        buttonconfirm = tk.Button(self,text="Zatwierdź", command=lambda: controller.show_frame("Transfer2"))
        buttonconfirm.pack()
        button = tk.Button(self, text="Wróć",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Transfer2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Podaj kwotę przelewu:")
        label.pack()
        entry = tk.Entry(self)
        entry.pack()
        buttonconfirm = tk.Button(self, text="Zatwierdź", command=lambda: controller.show_frame("Drukparagon"))
        buttonconfirm.pack()
        button = tk.Button(self, text="Wróć",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Stan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Stan konta wynosi:")
        label.pack()
        label2 = tk.Label(self, text="156 zł")
        label2.pack()
        button = tk.Button(self, text="Wróć",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()