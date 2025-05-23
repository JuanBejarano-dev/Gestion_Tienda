import tkinter as tk
from tkinter import messagebox
from Models.Clientes import Cliente
from Models.ClientesCrud import ClienteCRUD

def mostrarInterfazClientes(ventana_principal):
    ventana_principal.withdraw()
    
    ventana = tk.Toplevel()
    ventana.title("Gestión de Clientes")
    ventana.geometry("800x600")
    ventana.configure(bg="white")
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(5, weight=1)  

    crud = ClienteCRUD()

    # Título
    tk.Label(ventana, text="Gestión de Clientes", font=("Arial", 18, "bold"), bg="white", fg="#333").grid(row=0, column=0, columnspan=2, pady=20)

    # Entradas
    tk.Label(ventana, text="Nombre:", bg="white", anchor="w").grid(row=1, column=0, padx=20, sticky="w")
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.grid(row=1, column=1, padx=20, sticky="we")

    tk.Label(ventana, text="Apellido:", bg="white", anchor="w").grid(row=2, column=0, padx=20, sticky="w")
    entry_telefono = tk.Entry(ventana, width=30)
    entry_telefono.grid(row=2, column=1, padx=20, sticky="we")

    tk.Label(ventana, text="Correo:", bg="white", anchor="w").grid(row=3, column=0, padx=20, sticky="w")
    entry_direccion = tk.Entry(ventana, width=30)
    entry_direccion.grid(row=3, column=1, padx=20, sticky="we")

    # Lista
    lista = tk.Listbox(ventana, width=80, height=15, font=("Consolas", 10))
    lista.grid(row=5, column=0, columnspan=2, padx=20, pady=15, sticky="nsew")

    # Botonera
    frame_botones = tk.Frame(ventana, bg="white")
    frame_botones.grid(row=6, column=0, columnspan=2, pady=10)

    def cargar_clientes():
        lista.delete(0, tk.END)
        for cliente in crud.listar():
            lista.insert(tk.END, f"{cliente.id:03} - {cliente.nombre} | Tel: {cliente.telefono} | Dir: {cliente.direccion}")

    def agregar_cliente():
        nombre = entry_nombre.get()
        telefono = entry_telefono.get()
        direccion = entry_direccion.get()
        
        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
            
        crud.crear(Cliente(nombre=nombre, telefono=telefono, direccion=direccion))
        cargar_clientes()
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)

    def eliminar_cliente():
        seleccion = lista.curselection()
        if not seleccion:
            return
        item = lista.get(seleccion[0])
        id = int(item.split(" - ")[0])
        crud.eliminar(id)
        cargar_clientes()

    def actualizar_cliente():
        seleccion = lista.curselection()
        if not seleccion:
            return
        item = lista.get(seleccion[0])
        id = int(item.split(" - ")[0])
        nombre = entry_nombre.get()
        telefono = entry_telefono.get()
        direccion = entry_direccion.get()
        
        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
            
        crud.actualizar(Cliente(id=id, nombre=nombre, telefono=telefono, direccion=direccion))
        cargar_clientes()

    def seleccionar_cliente(event):
        seleccion = lista.curselection()
        if not seleccion:
            return
        item = lista.get(seleccion[0])
        partes = item.split(" | ")
        id_nombre = partes[0].split(" - ")
        
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, id_nombre[1].strip())
        
        telefono = partes[1].replace("Tel: ", "").strip()
        entry_telefono.delete(0, tk.END)
        entry_telefono.insert(0, telefono)
        
        direccion = partes[2].replace("Dir: ", "").strip()
        entry_direccion.delete(0, tk.END)
        entry_direccion.insert(0, direccion)

    def regresar():
        ventana.destroy()
        ventana_principal.deiconify()

    # Configuración de eventos
    lista.bind("<<ListboxSelect>>", seleccionar_cliente)

    # Botones
    btn_config = {"width": 15, "height": 2, "padx": 5, "pady": 5}
    tk.Button(frame_botones, text="Agregar", bg="#28a745", fg="white", command=agregar_cliente, **btn_config).grid(row=0, column=0)
    tk.Button(frame_botones, text="Actualizar", bg="#007bff", fg="white", command=actualizar_cliente, **btn_config).grid(row=0, column=1)
    tk.Button(frame_botones, text="Eliminar", bg="#dc3545", fg="white", command=eliminar_cliente, **btn_config).grid(row=0, column=2)
    tk.Button(frame_botones, text="Regresar", bg="#6c757d", fg="white", command=regresar, **btn_config).grid(row=0, column=3)

    cargar_clientes()