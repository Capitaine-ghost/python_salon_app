import tkinter
from customtkinter import *
from PIL import Image,ImageTk
class RendezVousFrameContainer(CTkFrame) : 
    def __init__(self,master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.rende_vous_dark_icon=Image.open("assets/icons/calendar_dark.png")
        self.rende_vous_light_icon=Image.open("assets/icons/calendar_light.png")
        self.rende_vous_icon=CTkImage(light_image=self.rende_vous_dark_icon, dark_image=self.rende_vous_light_icon, size=(20, 20))

        self.label_title = CTkLabel(self, text="Rendez-vous",image=self.rende_vous_icon,compound="left")
        self.label_title.grid(row=0,column=0, padx=10)
