import tkinter as tk
from tkinter import messagebox

class login_page(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
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

        self.button_login = tk.Button(self, text="Log in", font=("Arial", 12))
        self.button_login.pack(side="top")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("test")
    root.geometry("400x300")
    app = login_page(master=root)
    app.mainloop()