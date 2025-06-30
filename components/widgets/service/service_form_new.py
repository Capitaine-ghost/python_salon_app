from tkinter import filedialog
from customtkinter import *
from PIL import Image,ImageTk
from components.widgets.DialogBox.DialogBox import DialogBox

class ServiceNewForm(CTkFrame) : 
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.font =CTkFont(family="Helvetica",weight="bold", size=20)
        self.label = CTkLabel(self,text="Creation d'un type de Service", font=self.font, text_color="#d2d9da")
        self.label.grid(row=0,column=0, pady=(20,0), padx=10)

        self.input_libelle=CTkEntry(master=self,width=340, height=40,placeholder_text="Le Libelle",border_width=0)
        self.input_libelle.grid(row=1,column=0,pady=10)

        self.input_description =CTkEntry(self,placeholder_text="Description du service",border_width=0,width=340,height=40)
        self.input_description.grid(row=2,column=0,pady=10)

        self.input_prix =CTkEntry(master=self,width=340, height=40,placeholder_text="Le Prix",border_width=0)
        self.input_prix.grid(row=3,column=0,pady=10)

        self.type_service =CTkComboBox(self,width=340,height=40,border_width=0,values=[""],state="readonly")
        self.type_service.set("séléctionner le type de service concerné")
        self.type_service.grid(row=4,column=0,pady=(0,10))
        self.btn_submit = CTkButton(self,text="Enregistrer",command=self.submit_form)
        self.btn_submit.grid(row=5,column=0,pady=10)

        self.image_preview=CTkLabel(self,text="L'image s'affiche ici")
        self.image_preview.grid(row=0,column=1, pady=10,padx=10)
        
        self.button_imagePicker =CTkButton(self,text="Choisir une Image",command=self.ImagePicker)
        self.button_imagePicker.grid(row=1,column=1)

    # ajouter la section de selection de l'image

    # ajouter le combo box en recupérant les l'id et le libelle des types service 

        # self.input_libelle=CTkEntry(master=self,width=340, height=40,placeholder_text="Le Nom",border_width=0)
        # self.input_libelle.grid(row=1,column=0)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        self.rowconfigure(5,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.load_type_services()
        self.file_path = None
        self.image = None
        self.photo = None


    def load_type_services(self):
        query = "SELECT id, libelle_type FROM type_service"
        results, status =self.master.master.master.get(query)
        if results:
            libelles = [row[1] for row in results]
            self.type_service.configure(values=libelles)
            self.type_service_data = results
    def get_selected_type_service_id(self):
        selected_libelle = self.type_service.get()
        for id, libelle in getattr(self, "type_service_data", []):
            if libelle == selected_libelle:
                return id
        return None
    
    def ImagePicker(self) : 
        self.file_path = filedialog.askopenfilename(title="Choisir une image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.file_path :
            self.image = Image.open(self.file_path)
            self.image = self.image.resize((200, 200))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_preview.configure(text="")
            self.image_preview.configure(image=self.photo)
        else : 
            self.image_preview.configure(text="Aucune image sélectionnée")
            self.photo = None
            self.image = None

    def submit_form(self):
        libelle = self.input_libelle.get()
        description = self.input_description.get()
        prix = self.input_prix.get()
        id_type = self.get_selected_type_service_id()


        image_data = None
        if hasattr(self, "file_path") and self.file_path:
            with open(self.file_path, "rb") as f:
                image_data = f.read()

        # control validation des champs
        if not all([libelle, description, prix, id_type]):
            DialogBox(self, title="Erreur", message="Veuillez remplir tous les champs.", type="error")
            return
        
        if not image_data:
            DialogBox(self, title="Erreur", message="Veuillez sélectionner une image.", type="error")
            return
        query = "INSERT INTO service (libelle_service, description_service, prix_service, id_type, img_service) VALUES (%s, %s, %s, %s, %s)"
        params = (libelle, description, prix, id_type, image_data)
        self.master.master.master.post(query, params)
        self.input_libelle.configure(text="")
        self.input_description.configure(text="")
        self.input_prix.configure(text="")
        self.type_service.configure(text="")
        self.image_preview.configure(Image="")
        self.image_preview.configure(text="L'image s'affichage ici")
        self.image=""
        self.photo=""
        self.master.update()
