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
    Interfaz.geometry("700x400")
    Interfaz.configure(bg="black")

    label1 = tk.Label(Interfaz, 
        text= "Menu Principal",
        font=("Arial", 24 ,"bold"),
        pady=18,
        bg="black",
        fg="white")  
    label1.pack()

    botonC = tk.Button(Interfaz,text="Clientes",bg="Red",fg="white", width=50, height=3, bd=2, command=interfazClientes)
    botonf = tk.Button(Interfaz,text="Facturas",bg="blue",fg="white", width=50, height=3, bd=2, command =interfazFacturas)
    botonp = tk.Button(Interfaz,text="Productos",bg="blue",fg="white", width=50, height=3, bd=2, command =interfazProductos)
    botons = tk.Button(Interfaz,text="Salir",bg="green",fg="white", width=50, height=3, bd=2, command=Interfaz.destroy)

    botonC.pack(pady=5)
    botonf.pack(pady=5)
    botonp.pack(pady=5)
    botons.pack(pady=5)

    Interfaz.mainloop()