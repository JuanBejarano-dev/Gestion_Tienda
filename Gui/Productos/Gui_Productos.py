import tkinter as tk
from tkinter import messagebox
from Models.Productos import Producto
from Models.ProductosCrud import ProductoCRUD

def mostrarInterfazProductos(ventana_principal):
    ventana_principal.withdraw()
    
    ventana = tk.Toplevel()
    ventana.title("Gestión de Productos")
    ventana.geometry("600x500")
    ventana.configure(bg="white")

    crud = ProductoCRUD()

    # Widgets de entrada
    tk.Label(ventana, text="Nombre", bg="white").pack()
    entry_nombre = tk.Entry(ventana, width=40)
    entry_nombre.pack()

    tk.Label(ventana, text="Cantidad", bg="white").pack()
    entry_cantidad = tk.Entry(ventana, width=40)
    entry_cantidad.pack()

    lista = tk.Listbox(ventana, width=60)
    lista.pack(pady=10)

    # Funciones internas
    def cargar_productos():
        lista.delete(0, tk.END)
        for producto in crud.listar():
            lista.insert(tk.END, f"{producto.id} - {producto.nombre} ({producto.cantidad})")

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
    tk.Button(ventana, text="Agregar", bg="green", fg="white", command=agregar_producto).pack(pady=2)
    tk.Button(ventana, text="Actualizar", bg="blue", fg="white", command=actualizar_producto).pack(pady=2)
    tk.Button(ventana, text="Eliminar", bg="red", fg="white", command=eliminar_producto).pack(pady=2)
    tk.Button(ventana, text="Regresar", bg="gray", fg="white", command=regresar).pack(pady=10)

    cargar_productos()