from tkinter import *
import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class loginWindow:
    def __init__(self, ventanita):
        self.ventana = ventanita
        self.vc = Canvas(self.ventana, width=1366, height=768, background="black")
        self.logo = PhotoImage(file="imagenes/LOGO.png")
        self.widges()

    def widges(self):
        self.ventana.geometry('1366x768')
        self.vc.place(x=0, y=0)
        self.vc.create_image(1366, 768, image=self.logo, anchor="nw")
        self.vc.update()
        self.vc.update()