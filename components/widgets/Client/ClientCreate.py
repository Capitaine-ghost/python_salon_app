import tkinter
from  customtkinter import *

class ClientCreateForm(CTkFrame) :
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.font_label=CTkFont(family="Helvetica", size=24,weight="bold", slant="italic")
        self.label=CTkLabel(self, text="Création d'un Nouveau Employé", font=self.font_label,text_color="#8bb6da")
        self.label.grid(row=0, column=0, padx=(20,0), pady=(20,10))
        
        self.input_name =CTkEntry(master=self,width=340, height=40,placeholder_text="Le Nom",border_width=0)
        self.input_name.grid(row=1,column=0, ipadx=5,pady=5, padx=(10,0))

        self.input_first_name =CTkEntry(master=self,width=340, height=40,placeholder_text="Le Prénom",border_width=0)
        self.input_first_name.grid(row=2,column=0, ipadx=5,pady=5, padx=(10,0))

        self.input_phone =CTkEntry(master=self,width=340, height=40,placeholder_text="Le Téléphone",border_width=0)
        self.input_phone.grid(row=3,column=0, ipadx=5,pady=5, padx=(10,0))

        self.input_adress =CTkEntry(master=self,width=340, height=40,placeholder_text="L'adresse",border_width=0)
        self.input_adress.grid(row=4,column=0, ipadx=5,pady=5, padx=(10,0))

        self.submit_btn = CTkButton(self,text="Enregistrer",command=self.submit)
        self.submit_btn.grid(row=5,column=0,pady=20)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        self.rowconfigure(5,weight=1)
        self.columnconfigure(0,weight=1)
    def submit(self) : 
        query="INSERT INTO client(nom,prenom,telephone,adresse) values(%s,%s,%s,%s)"
        params=[self.input_name.get(),self.input_first_name.get(),self.input_phone.get(),self.input_adress.get()]
        self.master.post(query,params)
    
