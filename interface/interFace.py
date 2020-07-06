from tkinter import *
import time
import threading
def login():
    user = StringVar()
    password = StringVar()

    lflogin = LabelFrame(venta, text='User', padx=10, pady=10)
    lflogin.grid(row=2, column=0)

    Label(lflogin, text='usernam:').grid(row=3, column=1)
    luser = Entry(lflogin, textvariable=user, width=15).grid(row=3, column=3)

    Label(lflogin, text='passwor:').grid(row=4, column=1)
    lpassword = Entry(lflogin, textvariable=password, width=15).grid(row=4, column=3)

    btnAgregar = Button(lflogin, text=" Agregar ")
    btnAgregar.grid(row=7, column=1)

venta = Tk()
venta.geometry('1366x768')
venta.config(cursor="pirate",bg="beige",bd=10,relief="ridge")
vc = Canvas(venta, width=1366, height=768)
vc.place(x=0, y=0)
logo = PhotoImage(file="imagenes/LOGO.png")
vc.create_image(0, 0, image=logo, anchor="nw")
vc.update()
#t = threading.Thread(target=star)
frame = Frame(venta, width=200, height=200) #Creando el marco
frame.config(cursor="spider",bg="lightblue") #Configuración del marco
frame.pack(side="top", anchor="w")
venta.mainloop()

