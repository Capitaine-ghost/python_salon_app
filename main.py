import customtkinter 
import tkinter
from customtkinter import CTk
from components.widgets.Side_bar.Side_bar import MySideBar
from components.Layouts.type_service.type_service import TypeFrameContainer
from components.Layouts.Dashboad.Dash_board import Dashboard
from components.Layouts.Employes.Employe import EmployeFrameContainer
from components.Layouts.Prestation.Prestation import PrestationFrameContainer
from components.Layouts.Rendez_vous.Rendez_vous import RendezVousFrameContainer
from components.Layouts.Services.Services import ServiceFrameContainer
from components.Layouts.Clients.Clients import ClientContainer
from components.Layouts.Produits.Produits import ProduitsContainer
from db.connector import DbConnection
from db.config import CONFIG
from components.widgets.DialogBox.DialogBox import DialogBox
# setting the appearance mode to dark
customtkinter.set_appearance_mode("dark")

class App(CTk) : 
    def __init__(self):
        super().__init__()
        # creating a generl font layouts title
        self.font_title_label = customtkinter.CTkFont(family="Helvetica",weight="bold", slant="italic",size=18)
        self.DbConnector = DbConnection(**CONFIG)
        self.title("Salon App")
        self.geometry("1023x650")
        # Creating app sidebar 
        self.side_Bar = MySideBar(self)
        self.side_Bar.pack(anchor="nw", fill="y", side="left")
      
        # initializing the main container for layouts
        self.main_content =CTkFrame = customtkinter.CTkFrame(self)
        self.main_content.pack(fill="both",expand="true", padx=(10,0),pady=(5,0))

        # implementing different layouts class without mounting
        self.type_service_layout= TypeFrameContainer(self.main_content)
        self.service_layout =ServiceFrameContainer(self.main_content)
        self.rendezvous_layout = RendezVousFrameContainer(self.main_content)
        self.prestation_layout = PrestationFrameContainer(self.main_content)
        self.dashboard_layout =Dashboard(self.main_content)
        self.employe_layout = EmployeFrameContainer(self.main_content)
        self.clients_layout=ClientContainer(self.main_content)
        self.produits_layout=ProduitsContainer(self.main_content, width=700,height=450)

    # function to mount the exact layout selected from the sidebar
    def mountLayout(self,page):
        # 
        if   page =="type_service" : 
            # unmount all others layouts and mount type_service
            self.service_layout.pack_forget()
            self.rendezvous_layout.pack_forget()
            self.prestation_layout.pack_forget()
            self.dashboard_layout.pack_forget()
            self.employe_layout.pack_forget()
            self.clients_layout.pack_forget()
            self.produits_layout.pack_forget()
            # mounting type service layout
            self.type_service_layout.pack(expand="true",fill="both")
        elif page=="home" : 
             # unmount all others layouts and mount dashboard
            self.service_layout.pack_forget()
            self.rendezvous_layout.pack_forget()
            self.prestation_layout.pack_forget()
            self.type_service_layout.pack_forget()
            self.employe_layout.pack_forget()
            self.clients_layout.pack_forget()
            self.produits_layout.pack_forget()
            # mounting type service layout
            self.dashboard_layout.pack(expand="true",fill="both")
        elif page=="prestation" : 
             # unmount all others layouts and mount prestation
            self.service_layout.pack_forget()
            self.rendezvous_layout.pack_forget()
            self.type_service_layout.pack_forget()
            self.dashboard_layout.pack_forget()
            self.employe_layout.pack_forget()
            self.clients_layout.pack_forget()
            self.produits_layout.pack_forget()
            # mounting type service layout
            self.prestation_layout.pack(expand="true",fill="both")
        elif page=="Rdv" : 
             # unmount all others layouts and mount type_service
            self.service_layout.pack_forget()
            self.type_service_layout.pack_forget()
            self.prestation_layout.pack_forget()
            self.dashboard_layout.pack_forget()
            self.employe_layout.pack_forget()
            self.clients_layout.pack_forget()
            # mounting type service layout
            self.rendezvous_layout.pack(expand="true",fill="both")
        elif page=="employes" : 
             # unmount all others layouts and mount type_service
            self.service_layout.pack_forget()
            self.rendezvous_layout.pack_forget()
            self.prestation_layout.pack_forget()
            self.dashboard_layout.pack_forget()
            self.type_service_layout.pack_forget()
            self.clients_layout.pack_forget()
            self.produits_layout.pack_forget()
            # mounting type service layout
            self.employe_layout.pack(expand="true",fill="both")
        elif page=="services":
             # unmount all others layouts and mount type_service
            self.type_service_layout.pack_forget()
            self.rendezvous_layout.pack_forget()
            self.prestation_layout.pack_forget()
            self.dashboard_layout.pack_forget()
            self.employe_layout.pack_forget()
            self.clients_layout.pack_forget()
            self.produits_layout.pack_forget()
            # mounting type service layout
            # self.service_layout.grid(row=0,column=0)
            self.service_layout.pack(expand="true",fill="both")
        elif page=="clients" : 
             # unmount all others layouts and mount type_service
            self.type_service_layout.pack_forget()
            self.rendezvous_layout.pack_forget()
            self.prestation_layout.pack_forget()
            self.dashboard_layout.pack_forget()
            self.employe_layout.pack_forget()
            self.service_layout.pack_forget()
            self.produits_layout.pack_forget()
            # mounting type service layout
            self.clients_layout.pack(expand="true",fill="both")
        elif page=="produits": 
             # unmount all others layouts and mount type_service
            self.type_service_layout.pack_forget()
            self.rendezvous_layout.pack_forget()
            self.prestation_layout.pack_forget()
            self.dashboard_layout.pack_forget()
            self.employe_layout.pack_forget()
            self.clients_layout.pack_forget()
            self.service_layout.pack_forget()
            # mounting type service layout
            self.produits_layout.pack(expand="true",fill="both")

        self.main_content.update()

    def post(self,query,params): 
        self.DbConnector.connect()
        self.DbConnector.execute_query(query,params)
        if self.DbConnector.status==201 or self.DbConnector.status==200:
            dialog = DialogBox(self, title="Success", message="Opération Effectué avec success !", type="success")
            dialog.grab_set()
        else :
            dialog = DialogBox(self, title="Error", message="Une erreur s'est produite lors de l'opération.", type="error")
            dialog.grab_set()
        # self.DbConnector.close()
        
    def get(self,query,params=None):
        self.DbConnector.connect()
        results, status = self.DbConnector.fetch_all(query, params)
        if status==200:
            if results.__len__()==0:
                dialog = DialogBox(self, title="Info", message="Aucune donnée trouvée.", type="info")
                dialog.grab_set()
                return []
            return results,200
        else :
            dialog = DialogBox(self, title="Error", message="Une erreur s'est produite lors de la récupération des données.", type="error")
            dialog.grab_set()
            return None,500
        # self.DbConnector.close()
App =App()
App.mountLayout("home");
App.mainloop()
        