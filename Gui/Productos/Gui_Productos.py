import tkinter as tk
from tkinter import messagebox
from Models.Productos import Producto
from Models.ProductosCrud import ProductoCRUD

def mostrarInterfazProductos(ventana_principal):
    ventana_principal.withdraw()
    
    ventana = tk.Toplevel()
    ventana.title("Gestión de Productos")
    ventana.geometry("700x500")
    ventana.configure(bg="white")
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(4, weight=1)  # Hace el listbox expandible

    crud = ProductoCRUD()

    # Título
    tk.Label(ventana, text="Gestión de Productos", font=("Arial", 18, "bold"), bg="white", fg="#333").grid(row=0, column=0, columnspan=2, pady=20)

    # Entradas
    tk.Label(ventana, text="Nombre:", bg="white", anchor="w").grid(row=1, column=0, padx=20, sticky="w")
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.grid(row=1, column=1, padx=20, sticky="we")

    tk.Label(ventana, text="Cantidad:", bg="white", anchor="w").grid(row=2, column=0, padx=20, sticky="w")
    entry_cantidad = tk.Entry(ventana, width=30)
    entry_cantidad.grid(row=2, column=1, padx=20, sticky="we")

    # Lista
    lista = tk.Listbox(ventana, width=60, height=10, font=("Consolas", 10))
    lista.grid(row=4, column=0, columnspan=2, padx=20, pady=15, sticky="nsew")

    # Botonera
    frame_botones = tk.Frame(ventana, bg="white")
    frame_botones.grid(row=5, column=0, columnspan=2, pady=10)

    def cargar_productos():
        lista.delete(0, tk.END)
        for producto in crud.listar():
            lista.insert(tk.END, f"{producto.id:03} - {producto.nombre} ({producto.cantidad})")

    def agregar_producto():
        nombre = entry_nombre.get()
        cantidad = entry_cantidad.get()
        if not nombre or not cantidad.isdigit():
            messagebox.showerror("Error", "Datos inválidos")
            return
        crud.crear(Producto(nombre=nombre, cantidad=int(cantidad)))
        cargar_productos()
        entry_nombre.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)

    def eliminar_producto():
        seleccion = lista.curselection()
        if not seleccion:
            return
        item = lista.get(seleccion[0])
        id = int(item.split(" - ")[0])
        crud.eliminar(id)
        cargar_productos()

    def actualizar_producto():
        seleccion = lista.curselection()
        if not seleccion:
            return
        item = lista.get(seleccion[0])
        id = int(item.split(" - ")[0])
        nombre = entry_nombre.get()
        cantidad = entry_cantidad.get()
        if not nombre or not cantidad.isdigit():
            messagebox.showerror("Error", "Datos inválidos")
            return
        crud.actualizar(Producto(id=id, nombre=nombre, cantidad=int(cantidad)))
        cargar_productos()

    def regresar():
        ventana.destroy()
        ventana_principal.deiconify()

    # Botones
    btn_config = {"width": 15, "height": 2, "padx": 5, "pady": 5}
    tk.Button(frame_botones, text="Agregar", bg="#28a745", fg="white", command=agregar_producto, **btn_config).grid(row=0, column=0)
    tk.Button(frame_botones, text="Actualizar", bg="#007bff", fg="white", command=actualizar_producto, **btn_config).grid(row=0, column=1)
    tk.Button(frame_botones, text="Eliminar", bg="#dc3545", fg="white", command=eliminar_producto, **btn_config).grid(row=0, column=2)
    tk.Button(frame_botones, text="Regresar", bg="#6c757d", fg="white", command=regresar, **btn_config).grid(row=0, column=3)

    cargar_productos()
