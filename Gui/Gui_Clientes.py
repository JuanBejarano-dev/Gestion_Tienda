import tkinter as tk
from tkinter import ttk

def mostrar_ventana_clientes():
    ventana = tk.Toplevel()
    ventana.title("Clientes")
    ventana.geometry("400x300")
    ttk.Label(ventana, text="Clientes (vacío por ahora)").pack(pady=20)