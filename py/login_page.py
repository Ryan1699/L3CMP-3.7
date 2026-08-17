import tkinter as tk
from tkinter import messagebox

from function import Valuechecker, Errorlabel

class LoginPage(tk.Frame):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # title label   
        self.lable = tk.Label(self, text="Online Ticket Booking System", font=("Arial", 16))
        self.lable.pack(side="top")

            #First Name label
        self.label_firstname = tk.Label(self, text="First Name:", font=("Arial", 12))
        self.label_firstname.pack(side="top")
        self.input_firstname = tk.Entry(self, font=("Arial", 11))
        self.input_firstname.pack(side="top")
        self.error_firstname = Errorlabel(self)


            #Last Name label
        self.label_lastname = tk.Label(self, text="Last Name:", font=("Arial", 12))
        self.label_lastname.pack(side="top")
        self.input_lastname = tk.Entry(self, font=("Arial", 11))
        self.input_lastname.pack(side="top")
        self.error_lastname = Errorlabel(self)
            #Phone Number label
        self.label_number = tk.Label(self, text="Phone Number:", font=("Arial", 12))
        self.label_number.pack(side="top")
        self.input_number = tk.Entry(self, font=("Arial", 11))
        self.input_number.pack(side="top")
        self.error_number = Errorlabel(self)
        
            #Email Address label
        self.label_email = tk.Label(self, text="Email Address:", font=("Arial", 12))
        self.label_email.pack(side="top")
        self.input_email = tk.Entry(self, font=("Arial", 11))
        self.input_email.pack(side="top")
        self.error_email = Errorlabel(self)

            #Login button
        self.button_login = tk.Button(self, text="Log in", font=("Arial", 12), command=self.login_onclick)
        self.button_login.pack(side="top")

    def login_onclick(self):
        firstname = self.input_firstname.get()
        lastname = self.input_lastname.get()
        number = self.input_number.get()
        email = self.input_email.get()

        '''is_valid_firstname, firstname_error = Valuechecker.name_check(firstname)
        if not is_valid_firstname:
            self.error_firstname.show_error(firstname_error)
            return
        else:
            self.error_firstname.hide_error()

        is_valid_lastname, lastname_error = Valuechecker.name_check(lastname)
        if not is_valid_lastname:
            self.error_lastname.show_error(lastname_error)
            return
        else:
            self.error_lastname.hide_error()

        is_valid_number, number_error = Valuechecker.number_check(number)
        if not is_valid_number:
            self.error_number.show_error(number_error)
            return
        else:
            self.error_number.hide_error()

        is_valid_email, email_error = Valuechecker.email_check(email)
        if not is_valid_email:
            self.error_email.show_error(email_error)
            return
        else:
            self.error_email.hide_error()'''


        messagebox.showinfo("Success", "Login successful")
        self.controller.show_frame("BookingPage")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("test")
    root.geometry("400x300")
    app = LoginPage(parent=root)
    app.mainloop()