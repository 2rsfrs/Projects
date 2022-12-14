from logging import root
import string
import secrets
from textwrap import wrap
import pyperclip
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

password_length = 8

def changeSize():

    def change():
        global password_length
        password_length = int(e.get())
        root.destroy()

    root = Tk()
    e = Entry(root, bg = "gray")
    label = Label(root, text = "Enter desired length of password")
    b = Button(root, text = "Change", command = change)
    #exit_button = Button(root, text = "Exit", command = root.destroy)
    
    label.grid(column = 1, row = 1)
    e.grid(column = 1, row = 2)
    b.grid(column = 1, row = 3)
    #exit_button.grid(column = 1, row = 4)

def makePassword():

    global password_length
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    pyperclip.copy(password)
    messagebox.showinfo("Password Generator", "Password has been copied to your clipboard")

def makePasswordWithChars():

    global password_length

    alphabet = string.ascii_letters + string.digits + "!" + "@" + "#" + "$" + "%" + "^" + "\&"
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    pyperclip.copy(password)
    messagebox.showinfo("Password Generator", "Password has been copied to your clipboard")

window = Tk()

window.title('Password Generator')
window.geometry("404x75")
window.config(background = "white")

button_changeNumber = Button(window, text = "Change Password Size", fg = "black", command = changeSize)
button_makePassword = Button(window, text = "Make Password", fg = "black", command = makePassword)
button_makePasswordWChars = Button(window, text = "Make Password w/ Special Chars", fg = "black", command = makePasswordWithChars)
button_exit = Button(window, text = "Exit", fg = "red", command = window.destroy)

button_changeNumber.grid(column = 3, row = 1)
button_makePassword.grid(column = 1, row = 1)
button_makePasswordWChars.grid(column = 2, row = 1)
button_exit.grid(column = 2, row = 2)

window.mainloop()
