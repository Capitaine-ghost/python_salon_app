import tkinter
from customtkinter import *

class EmployeForm (CTkFrame) :
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
   
        self.font_label=CTkFont(family="Helvetica", size=24,weight="bold", slant="italic")
        self.label=CTkLabel(self, text="Création d'un Nouveau Employé", font=self.font_label,text_color="#8bb6da")
        self.label.grid(row=0, column=0, padx=(20,0), pady=(20,0))
        
        self.input_name =CTkEntry(master=self,width=340, height=40,placeholder_text="Le Nom",border_width=0)
        self.input_name.grid(row=2,column=0, ipadx=5,pady=5, padx=(10,0))

        self.input_prenom =CTkEntry(master=self,width=340, height=40,placeholder_text="Le Prenom",border_width=0)
        self.input_prenom.grid(row=3,column=0, ipadx=5,pady=5, padx=(10,0))

        self.input_tel =CTkEntry(master=self,width=340, height=40,placeholder_text="+242",border_width=0)
        self.input_tel.grid(row=4,column=0, ipadx=5,pady=5, padx=(10,0))

        self.input_tel =CTkEntry(master=self,width=340, height=40,placeholder_text="Le salaire estimé",border_width=0)
        self.input_tel.grid(row=5,column=0, ipadx=5,pady=5, padx=(10,0))

        self.submit_button = CTkButton(self,text="Enregistrer", command=self.submitForm)
        self.submit_button.grid(row=6,column=0,pady=20)
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_rowconfigure(5,weight=1)
        self.grid_rowconfigure(6,weight=1)

    def submitForm(self) : 
        pass
        # query ="INSERT INTO employes(nom,prenom,telephone,salaire)"
    

