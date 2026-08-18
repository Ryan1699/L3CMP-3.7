import tkinter as tk
from tkinter import messagebox

from function import Valuechecker, Errorlabel


BG_COLOR = "#022F69"
TXT_COLOR = "#BDB100"

class LoginPage(tk.Frame):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.config(padx=25, pady=20, bg=BG_COLOR)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, pad=20)
        
        # title label   
        self.title_frame = tk.Label(self, text="Online Ticket Booking System", font=("Arial", 16), bg=BG_COLOR, fg=TXT_COLOR)
        self.title_frame.grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 20))

        # First Name label
        self.label_firstname = tk.Label(self, text="First Name:", font=("Arial", 12), bg=BG_COLOR, fg=TXT_COLOR)
        self.label_firstname.grid(row=1, column=0, sticky="w", padx=12, pady=(0, 4))
        self.input_firstname = tk.Entry(self, font=("Arial", 11))
        self.input_firstname.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 2))
        self.error_firstname = Errorlabel(self)
        self.error_firstname.grid(row=3, column=0, sticky="w", padx=12)

        # Last Name label
        self.label_lastname = tk.Label(self, text="Last Name:", font=("Arial", 12), bg=BG_COLOR, fg=TXT_COLOR)
        self.label_lastname.grid(row=4, column=0, sticky="w", padx=12, pady=(12, 4))
        self.input_lastname = tk.Entry(self, font=("Arial", 11))
        self.input_lastname.grid(row=5, column=0, sticky="ew", padx=12, pady=(0, 2))
        self.error_lastname = Errorlabel(self)
        self.error_lastname.grid(row=6, column=0, sticky="w", padx=12)
        
        # Phone Number label
        self.label_number = tk.Label(self, text="Phone Number:", font=("Arial", 12), bg=BG_COLOR, fg=TXT_COLOR)
        self.label_number.grid(row=7, column=0, sticky="w", padx=12, pady=(12, 4))
        self.input_number = tk.Entry(self, font=("Arial", 11))
        self.input_number.grid(row=8, column=0, sticky="ew", padx=12, pady=(0, 2))
        self.error_number = Errorlabel(self)
        self.error_number.grid(row=9, column=0, sticky="w", padx=12)
        
        # Email Address label
        self.label_email = tk.Label(self, text="Email Address:", font=("Arial", 12), bg=BG_COLOR, fg=TXT_COLOR)
        self.label_email.grid(row=10, column=0, sticky="w", padx=12, pady=(12, 4))
        self.input_email = tk.Entry(self, font=("Arial", 11))
        self.input_email.grid(row=11, column=0, sticky="ew", padx=12, pady=(0, 2))
        self.error_email = Errorlabel(self)
        self.error_email.grid(row=12, column=0, sticky="w", padx=12)

        # Login button
        self.button_login = tk.Button(self, text="Log in", font=("Arial", 12), command=self.login_onclick)
        self.button_login.grid(row=13, column=0, sticky="ew", padx=12, pady=(20, 12))

    def login_onclick(self):
        firstname = self.input_firstname.get()
        lastname = self.input_lastname.get()
        number = self.input_number.get()
        email = self.input_email.get()
        can_proceed = []

        is_valid_firstname, firstname_error = Valuechecker.name_check(firstname)
        if not is_valid_firstname:
            self.error_firstname.show_error(firstname_error)
        else:
            self.error_firstname.hide_error()
            can_proceed.append(True)

        is_valid_lastname, lastname_error = Valuechecker.name_check(lastname)
        if not is_valid_lastname:
            self.error_lastname.show_error(lastname_error)
            
        else:
            self.error_lastname.hide_error()
            can_proceed.append(True)

        is_valid_number, number_error = Valuechecker.number_check(number)
        if not is_valid_number:
            self.error_number.show_error(number_error)
            
        else:
            self.error_number.hide_error()
            can_proceed.append(True)

        is_valid_email, email_error = Valuechecker.email_check(email)
        if not is_valid_email:
            self.error_email.show_error(email_error)
            
        else:
            self.error_email.hide_error()
            can_proceed.append(True)

        if len(can_proceed) == 4:
            messagebox.showinfo("Success", "Login successful")
            self.controller.show_frame("BookingPage")


