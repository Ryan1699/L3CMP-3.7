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
        self.outbound_bunk_count = tk.IntVar(value=0)
        self.outbound_receiling_count = tk.IntVar(value=0)
        self.return_bunk_count = tk.IntVar(value=0)
        self.return_receiling_count = tk.IntVar(value=0)
        self.total_price = tk.DoubleVar(value=0.0)
        self.gst_price = tk.DoubleVar(value=0.0)
        self.seat_selection = self.build_seat_selection()

        self.create_widgets()
        self.update_trip_ui()
        self.update_total_price()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Online Ticket Booking System", font=("Arial", 16))
        self.title_label.pack(side="top")

        self.trip_type_label = tk.Label(self, text="Trip Type:", font=("Arial", 12))
        self.trip_type_label.pack(side="top")

        self.radio_one_way = tk.Radiobutton(
            self,
            text="One-way",
            value="one-way",
            variable=self.trip_type,
            font=("Arial", 11),
            command=self.trip_type_change,
        )
        self.radio_one_way.pack(side="top")

        self.radio_return = tk.Radiobutton(
            self,
            text="Return",
            value="return",
            variable=self.trip_type,
            font=("Arial", 11),
            command=self.trip_type_change,
        )
        self.radio_return.pack(side="top")

        self.route_label = tk.Label(self, text="Route:", font=("Arial", 12))
        self.route_label.pack(side="top")

        self.route1 = tk.Radiobutton(self, text="Route 1", value="route1", variable=self.route, font=("Arial", 11))
        self.route1.pack(side="top")

        self.route2 = tk.Radiobutton(self, text="Route 2", value="route2", variable=self.route, font=("Arial", 11))
        self.route2.pack(side="top")

        self.seat_type_label = tk.Label(self, text="Seat Type:", font=("Arial", 12))
        self.seat_type_label.pack(side="top")

            #Oneway frame
        self.one_way_frame = tk.Frame(self)
        self.one_way_frame.pack(side="top")
        self.one_way_label = tk.Label(self.one_way_frame, text=f'Outbound Seats ({self.trip_type.get()}):', font=("Arial", 12))
        self.one_way_label.pack(side="top")

        self.bunk_label = tk.Label(self.one_way_frame, text="Bunk Seats:", font=("Arial", 12))
        self.bunk_label.pack(side="top")
        self.bunk_spinbox = tk.Spinbox(
            self.one_way_frame,
            from_=0,
            to=20,
            textvariable=self.bunk_count,
            font=("Arial", 11),
            command=self.update_total_price,
        )
        self.bunk_spinbox.pack(side="top")

        self.receiling_label = tk.Label(self.one_way_frame, text="Receiling Seats:", font=("Arial", 12))
        self.receiling_label.pack(side="top")
        self.receiling_spinbox = tk.Spinbox(
            self.one_way_frame,
            from_=0,
            to=20,
            textvariable=self.receiling_count,
            font=("Arial", 11),
            command=self.update_total_price,
        )
        self.receiling_spinbox.pack(side="top")
        ######

            #Return frame
        self.return_frame = tk.Frame(self)
        self.return_frame.pack(side="top")
        self.return_label = tk.Label(self.return_frame, text="Return Trip Seats:", font=("Arial", 12))
        self.return_label.pack(side="top")

        self.outbound_section_label = tk.Label(self.return_frame, text="Outbound Seats:", font=("Arial", 11))
        self.outbound_section_label.pack(side="top")

        self.outbound_bunk_label = tk.Label(self.return_frame, text="Bunk Seats:", font=("Arial", 11))
        self.outbound_bunk_label.pack(side="top")
        self.outbound_bunk_spinbox = tk.Spinbox(
            self.return_frame,
            from_=0,
            to=20,
            textvariable=self.outbound_bunk_count,
            font=("Arial", 11),
            command=self.update_total_price,
        )
        self.outbound_bunk_spinbox.pack(side="top")


        self.outbound_receiling_label = tk.Label(self.return_frame, text="Receiling Seats:", font=("Arial", 11))
        self.outbound_receiling_label.pack(side="top")
        self.outbound_receiling_spinbox = tk.Spinbox(
            self.return_frame,
            from_=0,
            to=20,
            textvariable=self.outbound_receiling_count,
            font=("Arial", 11),
            command=self.update_total_price,
        )
        self.outbound_receiling_spinbox.pack(side="top")

        self.return_section_label = tk.Label(self.return_frame, text="Return Seats:", font=("Arial", 11))
        self.return_section_label.pack(side="top")
        self.return_bunk_label = tk.Label(self.return_frame, text="Bunk Seats:", font=("Arial", 11))
        self.return_bunk_label.pack(side="top")
        self.return_bunk_spinbox = tk.Spinbox(
            self.return_frame,
            from_=0,
            to=20,
            textvariable=self.return_bunk_count,
            font=("Arial", 11),
            command=self.update_total_price,
        )
        self.return_bunk_spinbox.pack(side="top")

        self.return_receiling_label = tk.Label(self.return_frame, text="Receiling Seats:", font=("Arial", 11))
        self.return_receiling_label.pack(side="top")
        self.return_receiling_spinbox = tk.Spinbox(
            self.return_frame,
            from_=0,
            to=20,
            textvariable=self.return_receiling_count,
            font=("Arial", 11),
            command=self.update_total_price,
        )
        self.return_receiling_spinbox.pack(side="top")

        self.total_price_label = tk.Label(self, text="Total Price:", font=("Arial", 12))
        self.total_price_label.pack(side="top")
        self.price_label = tk.Label(self, textvariable=self.total_price, font=("Arial", 12))
        self.price_label.pack(side="top")

        self.gst_label = tk.Label(self, text="GST:", font=("Arial", 12))
        self.gst_label.pack(side="top")
        self.gst_value_label = tk.Label(self, textvariable=self.gst_price, font=("Arial", 10))
        self.gst_value_label.pack(side="top")

        self.button_book = tk.Button(self, text="Book", font=("Arial", 12), command=self.book_onclick)
        self.button_book.pack(side="bottom")

    def trip_type_change(self):
        self.update_trip_ui()
        self.update_total_price()

    def build_seat_selection(self):
        return {
            "outbound": {
                "bunk": self.outbound_bunk_count.get(),
                "receiling": self.outbound_receiling_count.get(),
            },
            "return": {
                "bunk": self.return_bunk_count.get(),
                "receiling": self.return_receiling_count.get(),
            },
        }

    def sync_selection_to_dict(self):
        self.seat_selection = self.build_seat_selection()

    def update_trip_ui(self):
        trip_type = self.trip_type.get()
        if trip_type == "return":
            self.one_way_frame.pack_forget()
            self.return_frame.pack(side="top")
        else:
            self.return_frame.pack_forget()
            self.one_way_frame.pack(side="top")

    def get_selected_seats(self):
        trip_type = self.trip_type.get()
        outbound = {
            "bunk": self.outbound_bunk_count.get(),
            "receiling": self.outbound_receiling_count.get(),
        }
        outbound_total = outbound["bunk"] * 20 + outbound["receiling"] * 15

        if trip_type == "return":
            return_seat = {
                "bunk": self.return_bunk_count.get(),
                "receiling": self.return_receiling_count.get(),
            }
            return_total = return_seat["bunk"] * 20 + return_seat["receiling"] * 15
            total = outbound_total + return_total
            return {
                "trip_type": trip_type,
                "seat_selection": {"outbound": outbound, "return": return_seat},
                "total": total,
            }

        return {
            "trip_type": trip_type,
            "seat_selection": {"outbound": outbound},
            "total": outbound_total,
        }

    def update_total_price(self):
        selection = self.get_selected_seats()
        total_price = selection["total"]
        self.total_price.set(total_price)
        self.gst_price.set(total_price * 0.07)

    def book_onclick(self):
        self.sync_selection_to_dict()

        if self.trip_type.get().strip() == "":
            messagebox.showerror("Error", "Please select a trip type")
            return

        if self.route.get().strip() == "":
            messagebox.showerror("Error", "Please select a route")
            return

        if self.trip_type.get() == "one-way":
            outbound_total = self.outbound_bunk_count.get() + self.outbound_receiling_count.get()
            if outbound_total == 0:
                messagebox.showerror("Error", "Please select at least one outbound seat")
                return
        else:
            outbound_total = self.outbound_bunk_count.get() + self.outbound_receiling_count.get()
            return_total = self.return_bunk_count.get() + self.return_receiling_count.get()
            if outbound_total == 0 or return_total == 0:
                messagebox.showerror("Error", "Please select at least one seat for both outbound and return trips")
                return

        confirm = messagebox.askyesno(
            "Confirm Booking",
            f"Are you sure you want to book the following:\n"
            f"Trip Type: {self.trip_type.get()}\n"
            f"Route: {self.route.get()}\n"
            f"Seat Selection: {self.seat_selection}\n"
            f"Total Price: ${self.total_price.get():.2f}",
        )

        if confirm:
            messagebox.showinfo(
                "Success",
                f"Booking successful!\nTrip Type: {self.trip_type.get()}\n"
                f"Route: {self.route.get()}\nSeat Selection: {self.seat_selection}",
            )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Booking Page")
    root.geometry("400x350")
    app = BookingPage(master=root)
    app.mainloop()