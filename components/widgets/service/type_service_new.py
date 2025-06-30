import tkinter
from customtkinter import *

class TypeServiceNewForm(CTkFrame) : 
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.font =CTkFont(family="Helvetica",weight="bold", size=20)
        self.label = CTkLabel(self,text="Creation d'un type d'un Service", font=self.font, text_color="#d2d9da")
        self.label.grid(row=0,column=0, pady=(20,0), padx=10)

        self.input_libelle =CTkEntry(master=self,width=340, height=40,placeholder_text="Le Nom",border_width=0)
        self.input_libelle.grid(row=1,column=0)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)

        self.submit_btn = CTkButton(self,text="Enregistrer",command=self.submit)
        self.submit_btn.grid(row=2,column=0, pady=20)

    def submit(self): 
        query = "INSERT INTO type_service(libelle_type) values(%s)";
        params =[self.input_libelle.get()]
        self.master.post(query,params)