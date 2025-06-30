import tkinter 
from PIL import Image,ImageTk
from customtkinter import *
from components.widgets.DataTable.DataTable import TableFrame
from components.widgets.Client.ClientCreate import ClientCreateForm

class ClientContainer(CTkFrame) : 
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.client_dark_icon=Image.open("assets/icons/client_dark.png")
        self.client_light_icon=Image.open("assets/icons/client_light.png")
        self.client_icon=CTkImage(light_image=self.client_dark_icon, dark_image=self.client_light_icon, size=(20, 20))

        self.label_title=CTkLabel(self,text="Clients",image=self.client_icon,compound="left")
        self.label_title.pack(anchor="w",pady=(10,0),padx=(10,0))

        self.frame_actions =CTkFrame(self,bg_color="transparent", fg_color="transparent")
        self.frame_actions.pack(side="top",ipady=10)

        self.catalogue_btn = CTkButton(self.frame_actions,text="Catalogue", command=self.show_catalogue)
        self.catalogue_btn.grid(row=0,column=0,padx=10, pady=10)

        self.create_btn = CTkButton(self.frame_actions,text="Nouveau",command=self.show_new)
        self.create_btn.grid(column=1, row=0, padx=10,pady=10)
        self.client_catalogue =CTkFrame(self)
        
        self.table_clients = TableFrame(self.client_catalogue,columns=['ID',"Nom","Prénom","téléphone","Adress"])
        self.table_clients.pack(expand=True, fill="both", padx=10, pady=(0, 10))

        self.new_client_form = ClientCreateForm(self)
        self.client_catalogue.pack(side="top", fill="x",padx=10, pady=(0, 10), ipadx=10, ipady=10)
        self.get()
    def show_catalogue(self) :
        self.new_client_form.pack_forget() 
        self.client_catalogue.pack(side="top", fill="x", padx=10, pady=(0, 10), ipadx=10, ipady=10)

    def show_new(self): 
          self.client_catalogue.pack_forget()
          self.new_client_form.pack(side="top", fill="x", padx=10, pady=(0, 10), ipadx=10, ipady=10)
    def post(self,query,params=None):
        self.master.master.post(query,params)
        
    def get(self): 
            query="SELECT * from client_list"
            result,status= self.master.master.get(query)
            if status==200:
                self.table_clients.set_data(result)


