import tkinter as tk


BG_COLOR = "#022F69"
class Valuechecker:


    @staticmethod
    def name_check(value):
        
        if not value.isalpha():
            return False, "Please enter a valid name (only letters are allowed)."
        return True, ""

    @staticmethod
    def number_check(value):
        if not value or not value.strip():
            return False, "Please enter a valid phone number."

        if len(value) < 9 or len(value) > 12:
            return False, "Please enter a valid phone number (9-12 digits)."

        try:
            int(value)
            return True, ""
        except ValueError:
            return False, "Please enter a valid phone number."

    @staticmethod
    def email_check(value):
        if not value or not value.strip():
            return False, "Please enter a valid email address."
        if "@" not in value or "." not in value:
            return False, "Email address must contain '@' and '.'"
        return True, ""
    

class Errorlabel(tk.Label):
    def __init__(self, master=None, text="", **kwargs):

        default_config = {
            "fg": "red",
            "font": ("Arial", 10),
            "bg": BG_COLOR
        }
        super().__init__(master, text=text, **{**default_config, **kwargs})

    def show_error(self, message):
        self.config(text=message)
        self.grid()

    def hide_error(self):
        self.config(text="")
        self.grid_forget()



