import tkinter 
from customtkinter import *
from components.widgets.FormNewProduct.ProductForm import ProductForm
from components.widgets.DataTable.DataTable import TableFrame
from PIL import Image, ImageTk

class ProduitsContainer (CTkFrame) : 
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.produit_dark_icon=Image.open("assets/icons/produit_dark.png")
        self.produit_light_icon=Image.open("assets/icons/produit_light.png")
        self.produit_icon=CTkImage(light_image=self.produit_dark_icon, dark_image=self.produit_light_icon, size=(20, 20))

        self.label_title = CTkLabel(self,text="Produits", image=self.produit_icon, compound="left")
        self.label_title.pack(anchor="w",pady=(10,0),padx=(10,0)
                              )
        # self.show_new=False
        # self.show_catalogue=False
        self.frame_actions =CTkFrame(self,bg_color="transparent", fg_color="transparent")
        self.frame_actions.pack(side="top",ipady=10)

        # self.create_product_form=CTkFrame(self)
        # self.create_product_form.pack(side="top", fill="x", padx=10, pady=(0, 10))
        self.product_new_form=ProductForm(self)
        #self.product_new_form.pack(side="top", fill="x", padx=10, pady=(0, 10), ipadx=10, ipady=10)
        self.product_catalogue=CTkFrame(self)
        self.product_catalogue.pack(side="top", fill="x", padx=10, pady=(0, 10), ipadx=10, ipady=10)
        
        self.table_produits = TableFrame(self.product_catalogue, columns=["ID", "Libellé", "Prix Unitaire", "Quantité", "Unité de Mesure"],
         headings=["ID", "Libellé", "Prix Unitaire", "Quantité", "Unité de Mesure"])
        
        self.table_produits.pack(expand=True, fill="both", padx=10, pady=(0, 10))


        # self.label_title.grid(row=0,column=0, padx=10)
        self.button_catalogue =CTkButton(self.frame_actions,text="Catalogue",command=self.show_catalogue_produit, width=100, height=30, text_color="white")
        self.button_catalogue.grid(row=0,column=0, padx=(10,0), pady=(10,0))

        self.button_new =CTkButton(self.frame_actions,text="Nouveau",command=self.show_new_produit, width=100, height=30, text_color="white")
        self.button_new.grid(row=0,column=1, padx=(10,0), pady=(10,0))
        self.get()


    def post(self,query,params) : 
         self.master.master.post(query,params)
    def get(self) :
         query="SELECT id,libelle,prix_unitaire,quantite,unite_mesure FROM produit"
         result,status = self.master.master.get(query)
         if status==200:
            self.table_produits.set_data(result)
    
    def refresh_catalogue(self):
        self.get()
        self.show_catalogue_produit()
        
    def show_new_produit(self):
         self.product_new_form.pack(side="top", fill="x", padx=10, pady=(0, 10), ipadx=10, ipady=10)
         self.product_catalogue.pack_forget()

    def show_catalogue_produit(self):
        self.product_new_form.pack_forget()
        self.product_catalogue.pack(side="top", fill="x", padx=10, pady=(0, 10), ipadx=10, ipady=10)


        