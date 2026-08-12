import tkinter as tk
from tkinter import messagebox

class BookingPage(tk.Frame):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.trip_type = tk.StringVar(value=" ")
        self.route = tk.StringVar(value=" ")
        self.bunk_count = tk.IntVar(value=0)
        self.receiling_count = tk.IntVar(value=0)

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Online Ticket Booking System", font=("Arial", 16))
        self.title_label.pack(side="top")

        self.trip_type_label = tk.Label(self, text="Trip Type:", font=("Arial", 12))
        self.trip_type_label.pack(side="top")

        self.radio_one_way = tk.Radiobutton(self, text="One-way", value="one-way", variable=self.trip_type, font=("Arial", 11))
        self.radio_one_way.pack(side="top")

        self.radio_return = tk.Radiobutton(self, text="Return", value="return", variable=self.trip_type, font=("Arial", 11))
        self.radio_return.pack(side="top")




        self.route_label = tk.Label(self, text="Route:", font=("Arial", 12))
        self.route_label.pack(side="top")

        self.route1 = tk.Radiobutton(self, text="Route 1", value="route1", variable=self.route, font=("Arial", 11))
        self.route1.pack(side="top")

        self.route2 = tk.Radiobutton(self, text="Route 2", value="route2", variable=self.route, font=("Arial", 11))
        self.route2.pack(side="top")

        self.seat_type_label = tk.Label(self, text="Seat Type:", font=("Arial", 12))
        self.seat_type_label.pack(side="top")

        self.bunk_label = tk.Label(self, text="Bunk Seats:", font=("Arial", 12))
        self.bunk_label.pack(side="top")
        self.bunk_spinbox= tk.Spinbox(self, from_=0, to=20, textvariable=self.bunk_count, font=("Arial", 11))
        self.bunk_spinbox.pack(side="top")

        self.receiling_label = tk.Label(self, text="Receiling Seats:", font=("Arial", 12))
        self.receiling_label.pack(side="top")
        self.receiling_spinbox= tk.Spinbox(self, from_=0, to=20, textvariable=self.receiling_count, font=("Arial", 11))
        self.receiling_spinbox.pack(side="top")

        self.button_book = tk.Button(self, text="Book", font=("Arial", 12), command=self.book_onclick)
        self.button_book.pack(side="bottom")

    def book_onclick(self):


        if self.trip_type.get().strip() == "":
            messagebox.showerror("Error", "Please select a trip type")
            return

        if self.route.get().strip() == "":
            messagebox.showerror("Error", "Please select a route")
            return

        if self.bunk_count.get() == 0 and self.receiling_count.get() == 0:
            messagebox.showerror("Error", "Please select at least one seat")
            return

        messagebox.showinfo("Success", f"Booking successful!\nTrip Type: {self.trip_type.get()}\nRoute: {self.route.get()}\nBunk Seats: {self.bunk_count.get()}\nReceiling Seats: {self.receiling_count.get()}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Booking Page")
    root.geometry("400x300")
    app = BookingPage(master=root)
    app.mainloop()