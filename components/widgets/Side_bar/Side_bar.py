from customtkinter import *
from customtkinter import CTk
from PIL import Image
class MySideBar(CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.label_font=CTkFont(family="Helevetica",weight="bold",size=16,slant="italic")
        self.label_title  = CTkLabel(self,text="Salon App", font=self.label_font)
        # adding a top label for the App name
        self.label_title.grid(row=0, column=0,pady=(20,0)) 
        #sidebar controler for changing Layouts 

        self.home_dark_icon=Image.open("assets/icons/chart_dark.png")
        self.home_light_icon=Image.open("assets/icons/chart_light.png")
        self.home_icon=CTkImage(light_image=self.home_dark_icon, dark_image=self.home_light_icon, size=(20, 20))
        
        self.service_dark_icon=Image.open("assets/icons/service_dark.png")
        self.service_light_icon=Image.open("assets/icons/service_light.png")
        self.service_icon=CTkImage(light_image=self.service_dark_icon, dark_image=self.service_light_icon, size=(20, 20))



        self.client_dark_icon=Image.open("assets/icons/client_dark.png")
        self.client_light_icon=Image.open("assets/icons/client_light.png")

        self.client_icon=CTkImage(light_image=self.client_dark_icon, dark_image=self.client_light_icon, size=(20, 20))
        self.employe_dark_icon=Image.open("assets/icons/employe_dark.png")
        self.employe_light_icon=Image.open("assets/icons/employe_light.png")    
        self.employe_icon=CTkImage(light_image=self.employe_dark_icon, dark_image=self.employe_light_icon, size=(20, 20))
        # implementation des boutons de la sidebar
        # Home
        self.home_btn = CTkButton(self,text="Home", fg_color="transparent",command=lambda:master.mountLayout("home"),
                                 image=self.home_icon, anchor="right", compound="right")
        self.home_btn.grid(row=1,column=0, pady=(20,0), padx=10)
        # Emplyes
        self.employe_btn = CTkButton(self,text="Employés", fg_color="transparent", anchor="right",command=lambda:master.mountLayout("employes"),
                                     image=self.employe_icon, compound="right")
        self.employe_btn.grid(row=2,column=0, pady=(20,0), padx=10)
        
        self.client_btn = CTkButton(self,text="Clients", fg_color="transparent", anchor="right",command=lambda:master.mountLayout("clients"),
                                    image=self.client_icon, compound="right")
        self.client_btn.grid(row=3,column=0, pady=(20,0), padx=10)

        self.prestatio_dark_icon=Image.open("assets/icons/watch_dark.png")
        self.prestatio_light_icon=Image.open("assets/icons/watch_light.png")
        
        self.type_service_dark_icon=Image.open("assets/icons/category_dark.png")
        self.type_service_light_icon=Image.open("assets/icons/category_light.png")
        self.type_service_icon=CTkImage(light_image=self.type_service_dark_icon, dark_image=self.type_service_light_icon, size=(20, 20))
        self.prestation_icon=CTkImage(light_image=self.prestatio_dark_icon,dark_image=self.prestatio_light_icon)

        self.produit_dark_icon=Image.open("assets/icons/produit_dark.png")
        self.produit_light_icon=Image.open("assets/icons/produit_light.png")
        self.produit_icon=CTkImage(light_image=self.produit_dark_icon, dark_image=self.produit_light_icon, size=(20, 20))
        self.produit_btn = CTkButton(self,text="Produits", fg_color="transparent", anchor="right",
                                     command=lambda:master.mountLayout("produits"),image=self.produit_icon, compound="right")
        self.produit_btn.grid(row=4,column=0, pady=(20,0), padx=10)

        self.type_service = CTkButton(self,text="Type Service", fg_color="transparent", anchor="right",
                                       command=lambda:master.mountLayout("type_service"),image=self.type_service_icon, compound="right")
        self.type_service.grid(row=5,column=0, pady=(20,0), padx=10)


        self.service_btn = CTkButton(self,text="Service", fg_color="transparent", anchor="right", 
                                     command=lambda:master.mountLayout("services"), image=self.service_icon, compound="right")
        self.service_btn.grid(row=6,column=0, pady=(20,0), padx=10)

        self.rende_vous_dark_icon=Image.open("assets/icons/calendar_dark.png")
        self.rende_vous_light_icon=Image.open("assets/icons/calendar_light.png")
        self.rende_vous_icon=CTkImage(light_image=self.rende_vous_dark_icon, dark_image=self.rende_vous_light_icon, size=(20, 20))

        self.Rende_vous_btn = CTkButton(self,text="Rendez-vous", fg_color="transparent", anchor="right",
                                        command=lambda:master.mountLayout("Rdv"), image=self.rende_vous_icon, compound="right")
        self.Rende_vous_btn.grid(row=7,column=0, pady=(20,0), padx=10)

        self.Prestation_btn = CTkButton(self,text="Prestation", fg_color="transparent", anchor="right",
                                        command=lambda:master.mountLayout("prestation"),image=self.prestation_icon, compound="right")
        self.Prestation_btn.grid(row=8,column=0, pady=(20,0), padx=10)

        # -------------------------------------
        self.setting_dark_icon=Image.open("assets/icons/setting_dark.png")
        self.setting_light_icon=Image.open("assets/icons/setting_light.png")
        self.setting_icon=CTkImage(light_image=self.setting_dark_icon, dark_image=self.setting_light_icon, size=(20, 20))
        self.settings_btn = CTkButton(self,text="Paramétre", fg_color="transparent", anchor="right", command=lambda:master.mountLayout("settings"),
                                      image=self.setting_icon, compound="right")
        self.settings_btn.grid(row=9,column=0, pady=(20,0), padx=10)

        self.profil_dark_icon=Image.open("assets/icons/account_dark.png")
        self.profil_light_icon=Image.open("assets/icons/account_light.png")
        self.profil_icon=CTkImage(light_image=self.profil_dark_icon, dark_image=self.profil_light_icon, size=(20, 20))

        self.profil_btn = CTkButton(self,text="Profil", fg_color="transparent", anchor="right", image=self.profil_icon, compound="right",
                                    command=lambda:master.mountLayout("profil"))
        self.profil_btn.grid(row=10,column=0, pady=(20,0), padx=10)
        self.logout_dark_icon=Image.open("assets/icons/logout_dark.png")
        self.logout_light_icon=Image.open("assets/icons/logout_light.png")
        self.logout_icon=CTkImage(light_image=self.logout_dark_icon, dark_image=self.logout_light_icon, size=(20, 20))
        self.log_out_btn = CTkButton(self,text="Déconnexion", fg_color="transparent", anchor="right",image=self.logout_icon, compound="right",
                                     command=lambda:master.mountLayout("logout"))
        self.log_out_btn.grid(row=11,column=0, pady=(20,0), padx=10)

        self.quit_btn = CTkButton(self,text="Quitter l'Application", fg_color="transparent", anchor="right", command=master.quit)
        self.quit_btn.grid(row=12,column=0, pady=(20,0), padx=10)
   
        