import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from Models.Facturas import Factura, DetalleFactura
from Models.FacturasCrud import FacturaCRUD
from Models.ClientesCrud import ClienteCRUD
from Models.ProductosCrud import ProductoCRUD

def mostrarInterfazFacturas(ventana_principal):
    ventana_principal.withdraw()
    
    ventana = tk.Toplevel()
    ventana.title("Gestión de Facturas")
    ventana.geometry("1200x800")
    ventana.minsize(1000, 700)
    ventana.configure(bg="white")
    
    # Configuración grid principal
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)
    
    # Contenedor principal
    main_frame = tk.Frame(ventana, bg="white")
    main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(3, weight=1)

    # Título
    lbl_titulo = tk.Label(main_frame, text="Gestión de Facturas", 
                        font=("Arial", 16, "bold"), bg="white", fg="#333")
    lbl_titulo.grid(row=0, column=0, pady=10, sticky="ew")

    # Sección Datos Factura
    frame_datos = tk.LabelFrame(main_frame, text="Datos de Factura", 
                              bg="white", padx=10, pady=10)
    frame_datos.grid(row=1, column=0, sticky="ew", pady=5)
    frame_datos.columnconfigure(1, weight=1)
    frame_datos.columnconfigure(3, weight=1)

    # Campos Cliente y Fecha
    tk.Label(frame_datos, text="Cliente:", bg="white").grid(row=0, column=0, padx=5, sticky="w")
    clientes = [f"{c.id} - {c.nombre}" for c in ClienteCRUD().listar()]
    combo_cliente = ttk.Combobox(frame_datos, values=clientes, state="readonly", width=30)
    combo_cliente.grid(row=0, column=1, padx=5, sticky="ew")

    tk.Label(frame_datos, text="Fecha:", bg="white").grid(row=0, column=2, padx=5, sticky="w")
    entry_fecha = tk.Entry(frame_datos, width=15)
    entry_fecha.grid(row=0, column=3, padx=5, sticky="ew")
    entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))

    # Sección Detalles
    frame_detalles = tk.LabelFrame(main_frame, text="Detalles de Factura", 
                                 bg="white", padx=10, pady=10)
    frame_detalles.grid(row=2, column=0, sticky="nsew", pady=5)
    frame_detalles.columnconfigure(1, weight=1)
    frame_detalles.rowconfigure(2, weight=1)

    # Campos Producto
    tk.Label(frame_detalles, text="Producto:", bg="white").grid(row=0, column=0, padx=5, sticky="w")
    productos = [f"{p.id} - {p.nombre} (Stock: {p.cantidad})" for p in ProductoCRUD().listar()]
    combo_producto = ttk.Combobox(frame_detalles, values=productos, state="readonly")
    combo_producto.grid(row=0, column=1, padx=5, sticky="ew")

    tk.Label(frame_detalles, text="Cantidad:", bg="white").grid(row=0, column=2, padx=5, sticky="w")
    entry_cantidad = tk.Entry(frame_detalles, width=10)
    entry_cantidad.grid(row=0, column=3, padx=5, sticky="ew")

    tk.Label(frame_detalles, text="Precio Unitario:", bg="white").grid(row=1, column=0, padx=5, sticky="w")
    entry_precio = tk.Entry(frame_detalles, width=15)
    entry_precio.grid(row=1, column=1, padx=5, sticky="ew")

    # Botón Agregar Detalle
    btn_agregar = tk.Button(frame_detalles, text="Agregar Detalle", bg="#4CAF50", fg="white", command=lambda: agregar_detalle())
    btn_agregar.grid(row=1, column=3, padx=5, sticky="e")

    # Tabla de detalles
    columns = ("Producto", "Cantidad", "Precio", "Subtotal")
    tree_detalles = ttk.Treeview(frame_detalles, columns=columns, show="headings", height=4)
    for col in columns:
        tree_detalles.heading(col, text=col)
        tree_detalles.column(col, width=100, anchor="center")
    tree_detalles.grid(row=2, column=0, columnspan=4, sticky="nsew", pady=5)

    # Scrollbar
    scroll = ttk.Scrollbar(frame_detalles, orient="vertical", command=tree_detalles.yview)
    scroll.grid(row=2, column=4, sticky="ns")
    tree_detalles.configure(yscrollcommand=scroll.set)

    # Total
    tk.Label(frame_detalles, text="Total:", bg="white", font=("Arial", 10, "bold")).grid(row=3, column=2, sticky="e")
    lbl_total = tk.Label(frame_detalles, text="0.00", bg="white", font=("Arial", 10, "bold"))
    lbl_total.grid(row=3, column=3, sticky="w")

    # Listado de Facturas
    frame_listado = tk.LabelFrame(main_frame, text="Facturas Registradas", 
                                bg="white", padx=10, pady=10)
    frame_listado.grid(row=3, column=0, sticky="nsew", pady=5)
    frame_listado.columnconfigure(0, weight=1)
    frame_listado.rowconfigure(0, weight=1)

    columns = ("ID", "Cliente", "Fecha", "Total")
    tree_facturas = ttk.Treeview(frame_listado, columns=columns, show="headings", height=8)
    for col in columns:
        tree_facturas.heading(col, text=col)
        tree_facturas.column(col, width=100, anchor="center")
    tree_facturas.grid(row=0, column=0, sticky="nsew")

    scroll_y = ttk.Scrollbar(frame_listado, orient="vertical", command=tree_facturas.yview)
    scroll_y.grid(row=0, column=1, sticky="ns")
    tree_facturas.configure(yscrollcommand=scroll_y.set)

    # Botonera inferior
    frame_botones = tk.Frame(main_frame, bg="white")
    frame_botones.grid(row=4, column=0, pady=10, sticky="ew")
    
    botones = [
        ("Guardar", "#2196F3", lambda: guardar_factura()),
        ("Eliminar", "#F44336", lambda: eliminar_factura()),
        ("Limpiar", "#FF9800", lambda: limpiar_formulario()),
        ("Regresar", "#607D8B", lambda: [ventana.destroy(), ventana_principal.deiconify()])
    ]
    
    for i, (texto, color, comando) in enumerate(botones):
        btn = tk.Button(frame_botones, text=texto, bg=color, fg="white", width=12)
        btn.grid(row=0, column=i, padx=5, ipady=3)
        btn.configure(command=comando)

    # Funcionalidades
    def actualizar_lista_productos():
        nonlocal productos
        productos = [f"{p.id} - {p.nombre} (Stock: {p.cantidad})" for p in ProductoCRUD().listar()]
        combo_producto['values'] = productos

    def agregar_detalle():
        producto = combo_producto.get()
        cantidad = entry_cantidad.get()
        precio = entry_precio.get()

        if not all([producto, cantidad, precio]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            # Extraer datos del producto
            id_producto = int(producto.split(" - ")[0])
            nombre_producto = producto.split(" - ")[1].split(" (Stock")[0]
            stock = int(producto.split("Stock: ")[1].replace(")", ""))
            cantidad = int(cantidad)
            precio = float(precio)
            
            # Validar stock
            if cantidad > stock:
                messagebox.showerror("Error", f"Stock insuficiente! Disponible: {stock}")
                return
                
            if cantidad <= 0 or precio <= 0:
                messagebox.showerror("Error", "Valores deben ser positivos")
                return

            # Agregar a la tabla
            subtotal = cantidad * precio
            tree_detalles.insert("", tk.END, values=(
                nombre_producto, 
                cantidad, 
                f"{precio:.2f}", 
                f"{subtotal:.2f}"
            ))

            # Limpiar campos
            combo_producto.set('')
            entry_cantidad.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            calcular_total()
            actualizar_lista_productos()

        except Exception as e:
            messagebox.showerror("Error", f"Dato inválido: {str(e)}")

    def calcular_total():
        total = 0.0
        for child in tree_detalles.get_children():
            valores = tree_detalles.item(child)['values']
            total += float(valores[3])  # Sumar subtotales
        lbl_total.config(text=f"{total:.2f}")

    def guardar_factura():
        if not combo_cliente.get():
            messagebox.showerror("Error", "Seleccione un cliente")
            return

        if not tree_detalles.get_children():
            messagebox.showerror("Error", "Agregue al menos un detalle")
            return

        try:
            # Crear factura (ID se genera automáticamente)
            factura = Factura(
                id=None,  # Corregido: no requiere ID inicial
                id_cliente=int(combo_cliente.get().split(" - ")[0]),
                fecha=entry_fecha.get(),
                total=float(lbl_total.cget("text"))
            )
            
            # Crear detalles
            detalles = []
            for child in tree_detalles.get_children():
                valores = tree_detalles.item(child)['values']
                # Obtener ID del producto desde la lista actualizada
                id_producto = int([p.split(" - ")[0] for p in productos if valores[0] in p][0])
                detalles.append(DetalleFactura(
                    id_producto=id_producto,
                    cantidad=int(valores[1]),
                    precio_unitario=float(valores[2])
                ))

            # Guardar en base de datos (usando transacción)
            with FacturaCRUD() as crud:
                factura_id = crud.crear(factura)
                for detalle in detalles:
                    crud.crear_detalle(crud.conn.cursor(), factura_id, detalle)  # Pasar cursor explícitamente
                    # Actualizar stock
                    ProductoCRUD().actualizar_stock(detalle.id_producto, -detalle.cantidad)

            messagebox.showinfo("Éxito", "Factura guardada correctamente")
            limpiar_formulario()
            cargar_facturas()
            actualizar_lista_productos()

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")

    def eliminar_factura():
        seleccion = tree_facturas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una factura")
            return
            
        id_factura = tree_facturas.item(seleccion[0])['values'][0]
        if messagebox.askyesno("Confirmar", "¿Eliminar esta factura?"):
            try:
                FacturaCRUD().eliminar(id_factura)
                cargar_facturas()
                messagebox.showinfo("Éxito", "Factura eliminada")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar: {str(e)}")

    def cargar_facturas():
        tree_facturas.delete(*tree_facturas.get_children())
        for factura in FacturaCRUD().listar():
            cliente = next((c.nombre for c in ClienteCRUD().listar() if c.id == factura.id_cliente), "Desconocido")
            tree_facturas.insert("", tk.END, values=(
                factura.id,
                cliente,
                factura.fecha,
                f"{factura.total:.2f}"
            ))

    def limpiar_formulario():
        combo_cliente.set('')
        entry_fecha.delete(0, tk.END)
        entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
        tree_detalles.delete(*tree_detalles.get_children())
        lbl_total.config(text="0.00")
        actualizar_lista_productos()

    # Carga inicial
    cargar_facturas()
    actualizar_lista_productos()
    
    # Centrado de ventana
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    ventana.mainloop()