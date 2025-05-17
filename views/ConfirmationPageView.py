import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class ConfirmationPageView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.controller = controller

        # Title
        title = ttk.Label(self, text="Thanks!",
                          font=controller.title_font)
        title.pack(pady=30)

        # Message
        message = ttk.Label(
            self,
            text="We've recorded your contact info. We'll reach out to you soon!",
            font=controller.field_font)
        message.pack(pady=30)

        # Return Button
        return_button = ttk.Button(
            self, text="Register Another", command=self.controller.return_to_form)
        return_button.pack(pady=50)
