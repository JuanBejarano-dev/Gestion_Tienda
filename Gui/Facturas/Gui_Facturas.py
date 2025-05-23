import tkinter as tk

def mostrarInterfazFacturas(ventana_principal):
    ventana_principal.withdraw()
    
    interfaz_facturas = tk.Toplevel()
    interfaz_facturas.geometry("500x500")
    interfaz_facturas.title("Interfaz de Facturas")

    label1 = tk.Label(interfaz_facturas, text="Interfaz de Facturas")
    label1.pack(pady=10)

    boton_regresar = tk.Button(interfaz_facturas, text="Regresar", command=lambda: regresar(interfaz_facturas, ventana_principal))
    boton_regresar.pack(pady=10)

def regresar(ventana_actual, ventana_principal):
    ventana_actual.destroy()
    ventana_principal.deiconify()