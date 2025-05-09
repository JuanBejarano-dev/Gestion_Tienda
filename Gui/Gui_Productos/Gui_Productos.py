import tkinter as tk
from . import Interfaz
def regresar():
    InterfazProductos.withdraw()
    Interfaz.mostrar_interfaz()
    
def mostrarInterfazProductos():   
    global InterfazProductos
    InterfazProductos = tk.Tk()
    InterfazProductos.geometry("500x500")
    label1 = tk.Label(InterfazProductos, text= "Interfaz de Productos")  
    label1.pack()
    botonC = tk.Button(InterfazProductos,text="Regresar", command=regresar)
    botonC.pack()
    InterfazProductos.mainloop()