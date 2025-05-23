import tkinter as tk
from Gui.Clientes import Gui_Clientes
from Gui.Facturas import Gui_Facturas
from Gui.Productos import Gui_Productos

def interfazClientes():
    Interfaz.withdraw()
    Gui_Clientes.mostrarInterfazClientes(Interfaz)

def interfazFacturas():
    Interfaz.withdraw()
    Gui_Facturas.mostrarInterfazFacturas(Interfaz)
    
def interfazProductos():
    Interfaz.withdraw()
    Gui_Productos.mostrarInterfazProductos(Interfaz)

def mostrar_interfaz():
    global Interfaz
    Interfaz = tk.Tk()
    Interfaz.geometry("700x400")
    Interfaz.configure(bg="black")

    label1 = tk.Label(Interfaz, text="Menu Principal", font=("Arial", 24 ,"bold"), pady=18, bg="black", fg="white")
    label1.pack()

    tk.Button(Interfaz,text="Clientes",bg="red",fg="white", width=50, height=3, bd=2, command=interfazClientes).pack(pady=5)
    tk.Button(Interfaz,text="Facturas",bg="blue",fg="white", width=50, height=3, bd=2, command=interfazFacturas).pack(pady=5)
    tk.Button(Interfaz,text="Productos",bg="blue",fg="white", width=50, height=3, bd=2, command=interfazProductos).pack(pady=5)
    tk.Button(Interfaz,text="Salir",bg="green",fg="white", width=50, height=3, bd=2, command=Interfaz.destroy).pack(pady=5)

    Interfaz.mainloop()