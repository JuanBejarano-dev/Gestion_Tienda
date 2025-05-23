import tkinter as tk

def mostrarInterfazClientes(ventana_principal):
    ventana_principal.withdraw()
    ventana_clientes = tk.Toplevel()
    ventana_clientes.geometry("500x500")
    tk.Label(ventana_clientes, text="Interfaz de Clientes").pack()
    tk.Button(ventana_clientes, text="Regresar", command=lambda: regresar(ventana_clientes, ventana_principal)).pack()

def regresar(ventana_actual, ventana_principal):
    ventana_actual.destroy()
    ventana_principal.deiconify()