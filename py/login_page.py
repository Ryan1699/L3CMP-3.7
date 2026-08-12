import tkinter as tk
from tkinter import messagebox

from value_checker import Valuechecker

class LoginPage(tk.Frame):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # title label   
        self.lable = tk.Label(self, text="Online Ticket Booking System", font=("Arial", 16))
        self.lable.pack(side="top")

        self.label_firstname = tk.Label(self, text="First Name:", font=("Arial", 12))
        self.label_firstname.pack(side="top")
        self.input_firstname = tk.Entry(self, font=("Arial", 11))
        self.input_firstname.pack(side="top")

        self.label_lastname = tk.Label(self, text="Last Name:", font=("Arial", 12))
        self.label_lastname.pack(side="top")
        self.input_lastname = tk.Entry(self, font=("Arial", 11))
        self.input_lastname.pack(side="top")

        self.label_number = tk.Label(self, text="Phone Number:", font=("Arial", 12))
        self.label_number.pack(side="top")
        self.input_number = tk.Entry(self, font=("Arial", 11))
        self.input_number.pack(side="top")

        self.label_email = tk.Label(self, text="Email Address:", font=("Arial", 12))
        self.label_email.pack(side="top")
        self.input_email = tk.Entry(self, font=("Arial", 11))
        self.input_email.pack(side="top")

        self.button_login = tk.Button(self, text="Log in", font=("Arial", 12), command=self.login_onclick)
        self.button_login.pack(side="top")

    def login_onclick(self):
        firstname = self.input_firstname.get()
        lastname = self.input_lastname.get()
        number = self.input_number.get()
        email = self.input_email.get()

        '''if not Valuechecker.name_check(firstname):
            messagebox.showerror("Error", "Invalid first name")
            return

        if not Valuechecker.name_check(lastname):
            messagebox.showerror("Error", "Invalid last name")
            return

        if not Valuechecker.number_check(number):
            messagebox.showerror("Error", "Invalid phone number")
            return

        if not Valuechecker.email_check(email):
            messagebox.showerror("Error", "Invalid email address")
            return'''

        messagebox.showinfo("Success", "Login successful")
        self.controller.show_frame("BookingPage")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("test")
    root.geometry("400x300")
    app = LoginPage(master=root)
    app.mainloop()