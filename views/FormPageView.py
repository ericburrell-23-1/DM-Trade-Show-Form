import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

IMAGE_SCALE_FACTOR = 0.1


class FormPageView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.controller = controller

        # Title
        title = ttk.Label(self, text="Looking for a new lab? We'll reach out.",
                          font=controller.title_font)
        title.pack(pady=30)

        # Entry field width
        self.entry_width = 40

        # Input fields
        self.first_name_entry = self.create_input_row("First Name")
        self.last_name_entry = self.create_input_row("Last Name")
        self.phone_number_entry = self.create_input_row("Phone Number")
        self.email_entry = self.create_input_row("Email")

        # Submit Button
        submit_button = ttk.Button(
            self, text="Submit", width=20, command=self.submit_form_data)
        submit_button.pack(pady=30)

        # Logo
        logo_img = Image.open("assets/dm-logo2.png")
        orig_width, orig_height = logo_img.size
        logo_img = logo_img.resize(
            (round(orig_width * IMAGE_SCALE_FACTOR), round(orig_height * IMAGE_SCALE_FACTOR)))
        self.logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = ttk.Label(self, image=self.logo_photo)
        logo_label.pack(side="bottom", pady=(0, 20))

    def create_input_row(self, label_text):
        frame = ttk.Frame(self)
        frame.pack(pady=10)

        inner_frame = ttk.Frame(frame)
        inner_frame.pack(fill="x", expand=True, pady=(0, 10))

        label = ttk.Label(inner_frame, text=label_text,
                          font=self.controller.field_font)
        label.pack(anchor="w")  # left-align

        entry = ttk.Entry(inner_frame, width=self.entry_width,
                          font=self.controller.field_font)
        entry.pack(pady=5, fill="x")

        return entry

    def submit_form_data(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        data = [first_name, last_name, phone_number, email]

        self.controller.submit_form_data(data)

    def clear_fields(self):
        self.first_name_entry.delete(0, "end")
        self.last_name_entry.delete(0, "end")
        self.phone_number_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
