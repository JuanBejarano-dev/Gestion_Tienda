import tkinter as tk
import Gui_Clientes as clientes
import Gui_Facturas as facturas
import Gui_Productos as productos


root = tk.Tk()
root.title("Gestion Tienda")
root.geometry("800x400")
root.configure(bg="black")

Frame_titulo = tk.Frame(root, bg="black")
Frame_titulo.pack(expand=True, fill="both", padx=20, pady=20)

titulo = tk.Label(
    Frame_titulo,
    text="Sistema de Gestion",  
    font=("Arial", 20, "bold"),  
    fg="white",  
    bg="black",  
)
titulo.pack(pady=(0, 20))

button_frame = tk.Frame(Frame_titulo, bg="black")
button_frame.pack()

for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
button_frame.grid_columnconfigure(0, weight=1)

botonP = tk.Button(button_frame, text="Productos", bg="red", fg="white",width=50, height=3, command=productos.mostrar_ventana_Producto)
botonF = tk.Button(button_frame, text="Facturas", bg="blue", fg="white",width=50, height=3 ,command=facturas.mostrar_ventana_Facturas)
botonC = tk.Button(button_frame, text="Clientes", bg="blue", fg="white", width=50, height=3, command=clientes.mostrar_ventana_clientes)
botonS = tk.Button(button_frame, text="Salir", bg="green", fg="white",width=50, height=3, command=root.destroy)



botonP.grid(row=0, pady=5, sticky="nsew")
botonF.grid(row=1, pady=5, sticky="nsew")
botonC.grid(row=2, pady=5, sticky="nsew")
botonS.grid(row=3, pady=5, sticky="nsew")


root.mainloop()