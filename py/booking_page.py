import tkinter as tk
from tkinter import messagebox

class BookingPage(tk.Frame):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)

        self.controller = controller
        self.trip_type = tk.StringVar(value=" ")
        self.route = tk.StringVar(value=" ")

        self.outbound_bunk_count = tk.IntVar(value=0)
        self.outbound_receiling_count = tk.IntVar(value=0)
        self.return_bunk_count = tk.IntVar(value=0)
        self.return_receiling_count = tk.IntVar(value=0)

        self.total_price = tk.DoubleVar(value=0.0)
        self.gst_price = tk.DoubleVar(value=0.0)

        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_padx = 12
        self.grid_pady = 6

        self.title_label = tk.Label(self, text="Online Ticket Booking System", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 8))

        self.trip_type_label = tk.Label(self, text="Trip Type:", font=("Arial", 12))
        self.trip_type_label.grid(row=1, column=0, sticky="w", padx=12)

        self.radio_one_way = tk.Radiobutton(self, text="One-way", value="one-way", variable=self.trip_type, font=("Arial", 11), command=self.update_seat_ui)
        self.radio_one_way.grid(row=2, column=0, sticky="w", padx=18)

        self.radio_return = tk.Radiobutton(self, text="Return", value="return", variable=self.trip_type, font=("Arial", 11), command=self.update_seat_ui)
        self.radio_return.grid(row=3, column=0, sticky="w", padx=18)

        self.route_label = tk.Label(self, text="Route:", font=("Arial", 12))
        self.route_label.grid(row=4, column=0, sticky="w", padx=12, pady=(8, 0))

        self.route1 = tk.Radiobutton(self, text="Route 1", value="outbound", variable=self.route, font=("Arial", 11), command=self.update_seat_ui)
        self.route1.grid(row=5, column=0, sticky="w", padx=18)

        self.route2 = tk.Radiobutton(self, text="Route 2", value="return", variable=self.route, font=("Arial", 11), command=self.update_seat_ui)
        self.route2.grid(row=6, column=0, sticky="w", padx=18)

        self.seat_type_label = tk.Label(self, text="Seat Type:", font=("Arial", 12))
        self.seat_type_label.grid(row=7, column=0, sticky="w", padx=12, pady=(8, 0))

        #Outbound section
        self.outbound_section = tk.Frame(self, bd=1, relief="solid")
        self.outbound_section.grid(row=8, column=0, sticky="ew", padx=12, pady=(4, 8))
        self.outbound_section.grid_columnconfigure(0, weight=1)
        self.outbound_section.grid_columnconfigure(1, weight=1)

        self.bunk_label = tk.Label(self.outbound_section, text="Bunk Seats:", font=("Arial", 12))
        self.bunk_label.grid(row=0, column=0, sticky="w", padx=(8, 6), pady=4)
        self.bunk_spinbox = tk.Spinbox(self.outbound_section, from_=0, to=20, textvariable=self.outbound_bunk_count, font=("Arial", 11), command=self.update_total_price, width=8)
        self.bunk_spinbox.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=4)

        self.receiling_label = tk.Label(self.outbound_section, text="Receiling Seats:", font=("Arial", 12))
        self.receiling_label.grid(row=1, column=0, sticky="w", padx=(8, 6), pady=4)
        self.receiling_spinbox = tk.Spinbox(self.outbound_section, from_=0, to=20, textvariable=self.outbound_receiling_count, font=("Arial", 11), command=self.update_total_price, width=8)
        self.receiling_spinbox.grid(row=1, column=1, sticky="ew", padx=(0, 8), pady=4)

        #Return section
        self.return_section = tk.Frame(self, bd=1, relief="solid")
        self.return_section.grid(row=9, column=0, sticky="ew", padx=12, pady=(0, 8))
        self.return_section.grid_columnconfigure(0, weight=1)
        self.return_section.grid_columnconfigure(1, weight=1)
        self.return_section.grid_remove()

        self.bunk_label_return = tk.Label(self.return_section, text="Bunk Seats:", font=("Arial", 12))
        self.bunk_label_return.grid(row=0, column=0, sticky="w", padx=(8, 6), pady=4)
        self.return_bunk_spinbox = tk.Spinbox(self.return_section, from_=0, to=20, textvariable=self.return_bunk_count, font=("Arial", 11), command=self.update_total_price, width=8)
        self.return_bunk_spinbox.grid(row=0, column=1, sticky="ew", padx=(0, 8), pady=4)

        self.receiling_label_return = tk.Label(self.return_section, text="Receiling Seats:", font=("Arial", 12))
        self.receiling_label_return.grid(row=1, column=0, sticky="w", padx=(8, 6), pady=4)
        self.return_receiling_spinbox = tk.Spinbox(self.return_section, from_=0, to=20, textvariable=self.return_receiling_count, font=("Arial", 11), command=self.update_total_price, width=8)
        self.return_receiling_spinbox.grid(row=1, column=1, sticky="ew", padx=(0, 8), pady=4)

        self.total_price_label = tk.Label(self, text="Total Price:", font=("Arial", 12))
        self.total_price_label.grid(row=10, column=0, sticky="w", padx=12)
        self.price_label = tk.Label(self, textvariable=self.total_price, font=("Arial", 12))
        self.price_label.grid(row=11, column=0, sticky="w", padx=12)

        self.gst_label = tk.Label(self, text="GST:", font=("Arial", 12))
        self.gst_label.grid(row=12, column=0, sticky="w", padx=12)
        self.gst_value_label = tk.Label(self, textvariable=self.gst_price, font=("Arial", 10))
        self.gst_value_label.grid(row=13, column=0, sticky="w", padx=12)

        self.button_book = tk.Button(self, text="Book", font=("Arial", 12), command=self.book_onclick)
        self.button_book.grid(row=14, column=0, sticky="ew", padx=12, pady=(10, 12))



    def update_seat_ui(self):
        if self.trip_type.get() == "return":
            if self.route.get() == "outbound":
                self.return_section.grid_remove()
            else:
                self.return_section.grid(row=9, column=0, sticky="ew", padx=12, pady=(0, 8))
        elif self.trip_type.get() == "one-way":
            self.return_section.grid_remove()

    def update_total_price(self):
        total_price = 0.0

        if self.trip_type.get() == "return":
            total_price = (self.outbound_bunk_count.get() * 20 + self.outbound_receiling_count.get() * 15) + (self.return_bunk_count.get() * 20 + self.return_receiling_count.get() * 15)
        else:
            if self.route.get() == "outbound":
                total_price = self.outbound_bunk_count.get() * 20 + self.outbound_receiling_count.get() * 15
            elif self.route.get() == "return":
                total_price = self.return_bunk_count.get() * 20 + self.return_receiling_count.get() * 15
            else:
                total_price = 0.0

        self.total_price.set(total_price)
        self.gst_price.set(total_price / 1.15)

    def book_onclick(self):

        if self.trip_type.get().strip() == "":
            messagebox.showerror("Error", "Please select a trip type")
            return

        if self.route.get().strip() =="":
            messagebox.showerror("Error", "Please select a route")
            return

        if self.outbound_bunk_count.get() == 0 and self.outbound_receiling_count.get() == 0 and self.return_bunk_count.get() == 0 and self.return_receiling_count.get() == 0:
            messagebox.showerror("Error", "Please select at least one seat")
            return
        confirm = messagebox.askyesno("Confirm Booking", 
                                      f"Are you sure you want to book the following:\nTrip Type: {self.trip_type.get()}\nRoute: {self.route.get()}\nBunk Seats: {self.outbound_bunk_count.get()}\nReceiling Seats: {self.outbound_receiling_count.get()}\nTotal Price: ${self.total_price.get():.2f}")

        if confirm:
            messagebox.showinfo("Success", f"Booking successful!\nTrip Type: {self.trip_type.get()}\nRoute: {self.route.get()}\nBunk Seats: {self.outbound_bunk_count.get()}\nReceiling Seats: {self.outbound_receiling_count.get()}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Booking Page")
    root.geometry("400x300")
    app = BookingPage(master=root)
    app.mainloop()