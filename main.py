import customtkinter
from customtkinter import CTk

customtkinter.set_appearance_mode("system")

class App(CTk) : 
    def __init__(self):
        super().__init__()
        self.title("Salon App")
        self.geometry("720x500")


App =App()


App.mainloop()
        