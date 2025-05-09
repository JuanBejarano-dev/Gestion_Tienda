import tkinter as tk
from . import Interfaz
def regresar():
    InterfazFacturas.withdraw()
    Interfaz.mostrar_interfaz()
    

def mostrarInterfazFacturas():   
    global InterfazFacturas
    InterfazFacturas = tk.Tk()
    InterfazFacturas.geometry("500x500")
    label1 = tk.Label(InterfazFacturas, text= "Interfaz de Facturas ")  
    label1.pack()
    botonC = tk.Button(InterfazFacturas,text="Regresar", command=regresar)
    botonC.pack()
    InterfazFacturas.mainloop()