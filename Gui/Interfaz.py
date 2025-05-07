import tkinter as tk
from . import Gui_Clientes
from . import Gui_Facturas
from . import Gui_Productos


def interfazClientes():
    Interfaz.withdraw()
    Gui_Clientes.mostrarInterfazClientes()

def interfazFacturas():
    Interfaz.withdraw()
    Gui_Facturas.mostrarInterfazFacturas()

def interfazProductos():
    Interfaz.withdraw()
    Gui_Productos.mostrarInterfazProductos()

def mostrar_interfaz():
    global Interfaz
    Interfaz = tk.Tk()
    Interfaz.geometry("500x500")
    label1 = tk.Label(Interfaz, text= "ventana principal")  
    label1.pack()
    botonC = tk.Button(Interfaz,text="Clientes", command =interfazClientes)
    botonf = tk.Button(Interfaz,text="Facturas", command =interfazFacturas)
    botonp = tk.Button(Interfaz,text="Productos", command =interfazProductos)
    botons = tk.Button(Interfaz,text="Salir", command=Interfaz.destroy)
    botonC.pack()
    botonf.pack()
    botonp.pack()
    botons.pack()
    Interfaz.mainloop()
