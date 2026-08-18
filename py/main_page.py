import tkinter as tk
from tkinter import messagebox
from login_page import LoginPage
from booking_page import BookingPage


class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for page in (LoginPage, BookingPage):
            page_name = page.__name__
            frame = page(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Booking System")
    root.geometry("500x700")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app = MainPage(master=root)
    app.mainloop()