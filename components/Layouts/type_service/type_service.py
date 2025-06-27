import tkinter
from customtkinter import *
from PIL import Image,ImageTk
from components.widgets.service.type_service_new import TypeServiceNewForm
from components.widgets.DataTable.DataTable import TableFrame
class TypeFrameContainer(CTkFrame) : 
    def __init__(self,master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.type_service_dark_icon=Image.open("assets/icons/category_dark.png")
        self.type_service_light_icon=Image.open("assets/icons/category_light.png")
        self.type_service_icon=CTkImage(light_image=self.type_service_dark_icon, dark_image=self.type_service_light_icon, size=(20, 20))

        self.Label_title = CTkLabel(self, text="Type Service",image=self.type_service_icon,compound="left")
        self.Label_title.pack(anchor="w",side="top",pady=10,padx=10)
        self.actions_container = CTkFrame(self,bg_color="transparent",fg_color="transparent")
        self.actions_container.pack(side="top",ipady=10)

        self.catalogue = TableFrame(self,columns=["id","libelle"])
       

        self.btn_show_new=CTkButton(self.actions_container,text="Nouveau",command=self.show_new)
        self.btn_show_catalogue=CTkButton(self.actions_container,text="Catalogue", command=self.show_catalogue)

        self.btn_show_catalogue.grid(row=0,column=0, pady=10,padx=10)
        self.btn_show_new.grid(row=0,column=1,padx=10,pady=10)

        self.new_type=TypeServiceNewForm(self);
        self.catalogue.pack(side="top", fill="x",padx=20,ipady=10)
        self.get()
      
    
    def post(self,query,params): 
        self.master.master.post(query,params)

    def get(self) : 
        query = "SELECT * from type_service"
        result,status = self.master.master.get(query)
        if status==200: 
            self.catalogue.set_data(result)

    def show_catalogue(self):
         self.new_type.pack_forget()
         self.catalogue.pack(side="top", fill="x",padx=20,ipady=10)
    def show_new(self):
         self.catalogue.pack_forget()
         self.new_type.pack(side="top",fill="x");


