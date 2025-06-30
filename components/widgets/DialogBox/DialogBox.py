import customtkinter

class DialogBox(customtkinter.CTkToplevel):
    def __init__(self, master, title="Message", message="", type="info"):
        super().__init__(master)
        self.title(title)
        self.geometry("350x150")
        self.resizable(False, False)
        self.grab_set()  # Rendre la fenêtre modale

        color = "#4BB543" if type == "success" else "#FF3333" if type == "error" else "#007ACC"

        self.label = customtkinter.CTkLabel(self, text=message, text_color=color, font=customtkinter.CTkFont(size=16, weight="bold"))
        self.label.pack(pady=30, padx=20)

        self.ok_btn = customtkinter.CTkButton(self, text="OK", command=self.destroy, width=80)
        self.ok_btn.pack(pady=10)