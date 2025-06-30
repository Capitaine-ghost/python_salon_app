import tkinter as tk
from tkinter import ttk

class TableFrame(tk.Frame):
    def __init__(self, master, columns, headings=None,**kwargs):
        super().__init__(master, **kwargs)
        self.columns = columns
        style = ttk.Style()
        style.configure(
            "Custom.Treeview",
            background="#222222",      # fond des lignes
            foreground="#ffffff",      # texte des lignes
            fieldbackground="#222222", # fond du tableau
            rowheight=30,
            
        )
        style.map("Custom.Treeview", background=[("selected", "#444444")])
        self.tree = ttk.Treeview(self, columns=columns, show="headings",style="Custom.Treeview")
        for idx, col in enumerate(columns):
            heading = headings[idx] if headings else col
            self.tree.heading(col, text=heading)
            self.tree.column(col, anchor="center",width=25)
        self.tree.pack(expand=True, fill="both")

    def set_data(self,data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in data:
            self.tree.insert("", "end", values=row)