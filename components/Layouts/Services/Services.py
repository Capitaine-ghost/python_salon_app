import tkinter
from customtkinter import *
from PIL import ImageTk,Image
from components.widgets.service.service_form_new import ServiceNewForm
from components.widgets.DataTable.DataTable import TableFrame
class ServiceFrameContainer(CTkFrame) : 
    def __init__(self, master,width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.service_dark_icon=Image.open("assets/icons/service_dark.png")
        self.service_light_icon=Image.open("assets/icons/service_light.png")
        self.service_icon=CTkImage(light_image=self.service_dark_icon, dark_image=self.service_light_icon, size=(20, 20))

        self.label_title = CTkLabel(self,text="Services",image=self.service_icon,compound="left")
        self.label_title.pack(anchor="w",pady=(10,0),padx=(10,0))
        self.frame_actions =CTkFrame(self,bg_color="transparent", fg_color="transparent")
        self.frame_actions.pack(side="top",ipady=10)

        # self.label_title.grid(row=0,column=0, padx=10)
        self.button_catalogue=CTkButton(self.frame_actions,text="Catalogue", command=self.show_catalogue)
        self.button_catalogue.grid(row=0,column=0)

        self.button_new =CTkButton(self.frame_actions,text="Nouveau",command=self.show_new)
        self.button_new.grid(row=0,column=1,padx=10)

        self.service_form=ServiceNewForm(self)
        

        self.catalogue =CTkFrame(self)
        

        self.service_table =TableFrame(self.catalogue,columns=["ID","Libelle","Description","Prix","Type"])
        self.service_table.pack(side="top",fill="both",padx=10,ipady=10)
        self.get()
        self.catalogue.pack(side="top",fill="both",ipady=10, ipadx=10, padx=10,pady=10)

    def get(self): 
        query="SELECT * FROM service_list";
        result,status = self.master.master.get(query)
        if status ==200 : 
            self.service_table.set_data(result)

    def show_new(self) : 
       self.catalogue.pack_forget()
       self.service_form.pack(side="top", fill="x", ipady=10, ipadx=10, padx=10,pady=10)
    def show_catalogue(self): 
        self.service_form.pack_forget()
        self.catalogue.pack(side="top",fill="both",ipady=10, ipadx=10, padx=10,pady=10)

