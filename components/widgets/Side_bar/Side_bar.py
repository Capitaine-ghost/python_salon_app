from customtkinter import *
from customtkinter import CTk

class MySideBar(CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.label_font=CTkFont(family="Helevetica",weight="bold",size=16,slant="italic")
        self.label_title  = CTkLabel(self,text="Salon App", font=self.label_font)
        # adding a top label for the App name
        self.label_title.grid(row=0, column=0,pady=(20,0)) 
        #sidebar controler for changing Layouts 
        self.home_btn = CTkButton(self,text="Home", fg_color="transparent",command=lambda:master.mountLayout("home"))
        self.home_btn.grid(row=1,column=0, pady=(20,0), padx=10)
        # Emplyes
        self.employe_btn = CTkButton(self,text="Employés", fg_color="transparent", anchor="right",command=lambda:master.mountLayout("employes"))
        self.employe_btn.grid(row=2,column=0, pady=(20,0), padx=10)

        self.type_service = CTkButton(self,text="Type Service", fg_color="transparent", anchor="right", command=lambda:master.mountLayout("type_service"))
        self.type_service.grid(row=3,column=0, pady=(20,0), padx=10)

        self.service_btn = CTkButton(self,text="Service", fg_color="transparent", anchor="right", command=lambda:master.mountLayout("services"))
        self.service_btn.grid(row=4,column=0, pady=(20,0), padx=10)

        self.Rende_vous_btn = CTkButton(self,text="Rendez-vous", fg_color="transparent", anchor="right",command=lambda:master.mountLayout("Rdv"))
        self.Rende_vous_btn.grid(row=5,column=0, pady=(20,0), padx=10)

        self.Prestation_btn = CTkButton(self,text="Prestation", fg_color="transparent", anchor="right",command=lambda:master.mountLayout("prestation"))
        self.Prestation_btn.grid(row=6,column=0, pady=(20,0), padx=10)

        # -------------------------------------
        self.settings_btn = CTkButton(self,text="Paramétre", fg_color="transparent", anchor="right")
        self.settings_btn.grid(row=7,column=0, pady=(20,0), padx=10)

        self.profil_btn = CTkButton(self,text="Profil", fg_color="transparent", anchor="right")
        self.profil_btn.grid(row=8,column=0, pady=(20,0), padx=10)

        self.log_out_btn = CTkButton(self,text="Déconnexion", fg_color="transparent", anchor="right")
        self.log_out_btn.grid(row=9,column=0, pady=(20,0), padx=10)

        self.quit_btn = CTkButton(self,text="Quitter l'Application", fg_color="transparent", anchor="right", command=master.quit)
        self.quit_btn.grid(row=10,column=0, pady=(20,0), padx=10)
   
        