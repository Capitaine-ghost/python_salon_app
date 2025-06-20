import customtkinter
import tkinter
from customtkinter import CTk
from components.widgets.Side_bar.Side_bar import MySideBar
customtkinter.set_appearance_mode("dark")

class App(CTk) : 
    def __init__(self):
        super().__init__()
        self.title("Salon App")
        self.geometry("1023x650")
        # Creating app sidebar 
        self.side_Bar = MySideBar(App)
        self.side_Bar.pack(anchor="nw", fill="y", side="left")

        # initializing the main container for layouts
        self.main_content =CTkFrame = customtkinter.CTkFrame(App)
        self.main_content.pack(fill="both",expand="true", padx=(10,0),pady=(5,0))
        


App =App()
App.mainloop()
        