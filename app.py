import csv
from pathlib import Path
import tkinter.font as font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from views.FormPageView import FormPageView
from views.ConfirmationPageView import ConfirmationPageView
import tkinter.messagebox as messagebox


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="journal")

        # Fullscreen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        # Fonts/Styles
        self.title_font = font.Font(size=30, weight="bold")
        self.field_font = font.Font(size=18)
        style = Style()
        style.configure("TButton", font=("Helvetica", 16))

        # Title
        self.title("D&M Imaging")

        # CSV File Path
        desktop = Path.home() / "Desktop"
        filename = "visitor_data.csv"
        self.filepath = desktop / filename

        # Frames
        self.frames = {}
        for Page in (FormPageView, ConfirmationPageView):
            page_name = Page.__name__
            frame = Page(parent=self, controller=self)
            self.frames[page_name] = frame

        self.show_frame("FormPageView")

    def submit_form_data(self, data):
        with open(self.filepath, 'a', newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

        # ADD A CHECK HERE THAT THE DATA WAS WRITTEN
        with open(self.filepath, 'r', newline="") as csvfile:
            lines = list(csv.reader(csvfile))
            if lines and lines[-1] == data:
                self.show_frame("ConfirmationPageView")
            else:
                self.show_error_message(
                    "Failed to save data. Please try again.")

    def return_to_form(self):
        form_page = self.frames["FormPageView"]
        form_page.clear_fields()
        self.show_frame("FormPageView")

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.pack_forget()  # hide all frames
        frame = self.frames[page_name]
        frame.pack(fill="both", expand=True)

    def show_error_message(self, message):
        messagebox.showerror("Error", message)


if __name__ == "__main__":
    app = App()
    app.mainloop()
