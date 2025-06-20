import customtkinter
from customtkinter import CTk
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark_blue")
class App(CTk) : 
    def __init__(self):
        super().__init__()
        self.title("Salon App")
        self.geometry(720,500)


App =App()


App.mainloop()
        