import tkinter as tk
from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
import numpy as np

class Dashboard(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.home_dark_icon=Image.open("assets/icons/chart_dark.png")
        self.home_light_icon=Image.open("assets/icons/chart_light.png")
        self.home_icon=CTkImage(light_image=self.home_dark_icon, dark_image=self.home_light_icon, size=(20, 20))

        self.label = CTkLabel(self, text="Dashboard", font=CTkFont(size=20, weight="bold"), image=self.home_icon, compound="left")
        self.label.pack(pady=10)

        # Exemple de stats (remplace par tes vraies valeurs)
        stats = {
            "Produits": 25,
            "Clients": 40,
            "Employés": 10,
            "Rendez-vous": 5,
            "Services": 105
        }
        max_values = {
            "Produits": 100,
            "Clients": 100,
            "Employés": 100,
            "Rendez-vous": 100,
            "Services": 150
        }
        cards_frame = CTkFrame(self, fg_color="transparent")
        cards_frame.pack(pady=20, padx=10, fill="x")
        for label, value in stats.items():
            card = CTkFrame(cards_frame, fg_color="#393e46", corner_radius=10)
            card.pack(side="left", padx=10, pady=10, fill="both", expand=True)
            card_label = CTkLabel(card, text=label, font=CTkFont(size=16, weight="bold"), text_color="#8bb6da")
            card_label.pack(pady=(10, 0))
            card_value = CTkLabel(card, text=str(value), font=CTkFont(size=24, weight="bold"), text_color="#eeeeee")
            card_value.pack(pady=(5, 10))
            
            
        fig, axs = plt.subplots(1, len(stats), figsize=(2.2*len(stats), 3), dpi=100)
        if len(stats) == 1:
            axs = [axs]

        for ax, (label, value) in zip(axs, stats.items()):
            max_val = max_values[label]
            percent = value / max_val
            # Donut chart
            wedges, _ = ax.pie(
                [percent, 1-percent],
                radius=1,
                colors=["#8bb6da", "#393e46"],
                startangle=90,
                counterclock=False,
                wedgeprops=dict(width=0.3, edgecolor="#222831")
            )

            ax.text(0, 0, f"{value}", ha='center', va='center', fontsize=16, color="#8bb6da", fontweight="bold")
            ax.set_title(label, color="#eeeeee", fontsize=12, pad=10)
            ax.set_aspect("equal")
            ax.axis("off")

        fig.patch.set_facecolor("#222831")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20, fill="both", expand=True)
        plt.close(fig)