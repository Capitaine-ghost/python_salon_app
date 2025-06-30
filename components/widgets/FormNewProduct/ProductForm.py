import tkinter
from tkinter import filedialog
import customtkinter
from customtkinter import *
from PIL import Image,ImageTk

class ProductForm(CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.font_label=CTkFont(family="Helvetica", size=24,weight="bold", slant="italic")
        self.label=CTkLabel(self, text="Création d'un Nouveau Produit", font=self.font_label,text_color="#8bb6da")
        self.label.grid(row=0, column=0, padx=(20,0), pady=(20,0))
        
        self.input_libelle =CTkEntry(master=self,width=340, height=40,placeholder_text="Le nom du Produit",border_width=0)
        self.input_libelle.grid(row=1,column=0, ipadx=5,pady=5, padx=(10,0))

        self.file_path_image_product =""

        self.input_prix =CTkEntry(master=self,width=340, height=40,placeholder_text="Le Prix unitaire",border_width=0)
        self.input_prix.grid(row=2,column=0, ipadx=5,pady=5, padx=(10,0))

        self.input_quantite =CTkEntry(master=self,width=340, height=40,placeholder_text="La Quantité disponible",border_width=0)
        self.input_quantite.grid(row=3,column=0, ipadx=5,pady=5, padx=(10,0))

        self.input_unite = CTkComboBox(self,values=["tubes","bouteille","flacon","paquet","Entrez une unité personalisée"],width=340, height=40,border_width=0,state="readonly", command=self.personalise_choix)
        self.input_unite.set("selection l'unité de mesure")
        self.input_unite.grid(row=4,column=0,ipadx=5,pady=5, padx=(10,0))

        self.preview_image_prod = CTkLabel(self, text="L'image du produit s'affiche ici")
        self.preview_image_prod.grid(row=1,column=1,ipadx=5,pady=5, padx=(10,0))

        self.imagePicker = CTkButton(self,text="Choisir une Image",command=self.pickImage)
        self.imagePicker.grid(row=2,column=1,ipadx=5,pady=5, padx=(10,0))
        self.image_link =""
        self.image=""
        self.submit_button = CTkButton(self,text="Enregistrer",command=self.submit_form)
        self.submit_button.grid(row=5,columnspan=4, pady=20)
        self.image_data=""

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

    def personalise_choix(self,choix):
        if choix=="Entrez une unité personalisée" : 
            self.input_unite.configure(state="normal")
            self.input_unite.set("")
            self.input_unite.focus()
        else : 
            self.input_unite.configure(state="readonly")

    def pickImage(self) : 
        self.file_path_image_product = filedialog.askopenfilename(title="Séléctionner une Image pour le Produit",filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        self.image_link = Image.open(self.file_path_image_product)
        self.image =CTkImage(self.image_link, size=(150,100))
        self.preview_image_prod.configure(image=self.image)
        self.preview_image_prod.configure(text="")
        with open(self.file_path_image_product,"rb") as file : 
            self.image_data=file.read();
            print(f'path : ${self.file_path_image_product}')
    def reset(self) : 
        self.input_libelle.delete(0, 'end')
        self.input_prix.delete(0, 'end')
        self.input_quantite.delete(0, 'end')
        self.input_unite.set("selection l'unité de mesure")
        self.preview_image_prod.configure(image=None, text="L'image du produit s'affiche ici")
        self.image_data = ""
        self.file_path_image_product = ""
        
    def submit_form(self): 
         print(f"um :${self.input_unite.get()} ")
         query="INSERT INTO produit(libelle,prix_unitaire,unite_mesure,quantite,image_prod) VALUES(%s,%s,%s,%s,%s)"
         params = [self.input_libelle.get(),self.input_prix.get(), self.input_unite.get(),self.input_quantite.get(),self.image_data]
         self.master.post(query,params)
         self.reset()
         self.master.refresh_catalogue()
    

        