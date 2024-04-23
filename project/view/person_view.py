from tkinter import *
import tkinter.messagebox as msg
from project.controller.person_controller import PersonController

class PersonView:
    def save_click(self):
        status, message = PersonController.save(self.name.get(), self.family.get())
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error",message)

    def edit_click(self):
        status, message = PersonController.edit(self.name.get(), self.family.get())
        if status:
            msg.showinfo("Edit", message)
        else:
            msg.showerror("Edit Error",message)

    def remove_click(self):
        status, message = PersonController.remove(self.name.get(), self.family.get())
        if status:
            msg.showinfo("Remove", message)
        else:
            msg.showerror("Remove Error", message)

    def __init__(self):
        win = Tk()
        win.title("Person Information")
        win.geometry("250x250")
        Label(win, text="Name: ").place(x=20,y=20)
        self.name = StringVar()
        Entry(win, textvariable=self.name).place(x=80,y=20)

        Label(win, text="Family: ").place(x=20,y=60)
        self.family = StringVar()
        Entry(win, textvariable=self.family).place(x=80,y=60)

        Button(win, text="Save",width=6, command=self.save_click).place(x=20,y=150)
        Button(win, text="Edit",width=6, command=self.edit_click).place(x=85,y=150)
        Button(win, text="Remove",width=6, command=self.remove_click).place(x=150,y=150)

        win.mainloop()