import tkinter as tk
from .Gui_Clientes import Interfaz
def regresar():
    InterfazClientes.withdraw()
    Interfaz.mostrar_interfaz()
    
def mostrarInterfazClientes():   
    global InterfazClientes
    InterfazClientes = tk.Tk()
    InterfazClientes.geometry("500x500")
    label1 = tk.Label(InterfazClientes, text= "Interfaz de clientes")  
    label1.pack()
    botonC = tk.Button(InterfazClientes,text="Regresar", command=regresar)
    botonC.pack()
    InterfazClientes.mainloop()