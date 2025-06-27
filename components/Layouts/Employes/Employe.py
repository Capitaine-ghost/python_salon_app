import tkinter
from customtkinter import * 
from components.widgets.EmployeForm.EmployeForm import EmployeForm
from components.widgets.DataTable.DataTable import TableFrame
from PIL import ImageTk,Image
class EmployeFrameContainer(CTkFrame) : 
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.employe_dark_icon=Image.open("assets/icons/employe_dark.png")
        self.employe_light_icon=Image.open("assets/icons/employe_light.png")    
        self.employe_icon=CTkImage(light_image=self.employe_dark_icon, dark_image=self.employe_light_icon, size=(20, 20))
        
        self.label_title=CTkLabel(self,text="Employes",image=self.employe_icon,compound="left")
        self.label_title.pack(anchor="w",pady=(10,0),padx=(10,0))

        self.frame_actions =CTkFrame(self,bg_color="transparent", fg_color="transparent")
        self.frame_actions.pack(side="top",ipady=10)

        self.button_catalogue =CTkButton(self.frame_actions,text="Catalogue",command=self.show_catalogue_employe, width=100, height=30, text_color="white")
        self.button_catalogue.grid(row=0,column=0, padx=(10,0), pady=(10,0))

        self.button_new =CTkButton(self.frame_actions,text="Nouveau",command=self.show_new_employe, width=100, height=30, text_color="white")
        self.button_new.grid(row=0,column=1, padx=(10,0), pady=(10,0))

        self.employe_new_form =EmployeForm(self)
  
        self.catalogue_employe =TableFrame(self,columns=["ID","Noms","Prénoms","Téléphone","Salaire"])
        self.catalogue_employe.pack(side="top", fill="x", padx=10, pady=(0, 10), ipadx=10, ipady=10)
        
        self.get()
    def post(self): 
        pass
    def get(self) : 
        query="SELECT * FROM employe"
        result = self.master.master.get(query)
        if result is not None :
         self.catalogue_employe.set_data(result)
    def put(self): 
        pass
    def delete(self):
        pass
    def show_catalogue_employe(self): 
        self.employe_new_form.pack_forget()
        self.catalogue_employe.pack(side="top",fill="x",padx=10,pady=(5,10),ipady=10,ipadx=10)
        
    def show_new_employe(self) :
        self.catalogue_employe.pack_forget()
        self.employe_new_form.pack(side="top", fill="x", padx=10, pady=(0, 10), ipadx=10, ipady=10)
        