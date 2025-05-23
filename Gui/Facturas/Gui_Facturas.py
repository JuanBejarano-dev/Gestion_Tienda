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
    ventana.geometry("1100x750")
    ventana.minsize(900, 650)
    ventana.configure(bg="white")
    
    # Configuración de pesos para grid responsive
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)
    
    # Frame principal contenedor
    main_container = tk.Frame(ventana, bg="white")
    main_container.grid(row=0, column=0, sticky="nsew")
    main_container.columnconfigure(0, weight=1)
    
    # Configuración responsive del contenedor principal
    for i in range(6):  # 6 filas principales
        main_container.rowconfigure(i, weight=0 if i < 5 else 1)
    
    # Título
    lbl_titulo = tk.Label(main_container, text="Gestión de Facturas", 
                         font=("Arial", 18, "bold"), bg="white", fg="#333")
    lbl_titulo.grid(row=0, column=0, pady=(10, 20), sticky="ew", columnspan=2)
    
    # ----------------- Sección Datos Factura -----------------
    frame_factura = tk.LabelFrame(main_container, text="Datos de Factura", 
                                bg="white", padx=10, pady=10)
    frame_factura.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
    frame_factura.columnconfigure(1, weight=1)
    frame_factura.columnconfigure(3, weight=1)
    
    # Cliente
    tk.Label(frame_factura, text="Cliente:", bg="white", anchor="w").grid(
        row=0, column=0, sticky="ew", padx=5, pady=5)
    
    clientes = [c.nombre for c in ClienteCRUD().listar()]
    combo_cliente = ttk.Combobox(frame_factura, values=clientes, state="readonly")
    combo_cliente.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    
    # Fecha
    tk.Label(frame_factura, text="Fecha:", bg="white", anchor="w").grid(
        row=0, column=2, sticky="ew", padx=5, pady=5)
    
    entry_fecha = tk.Entry(frame_factura)
    entry_fecha.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
    entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
    
    # ----------------- Sección Detalles Factura -----------------
    frame_detalles = tk.LabelFrame(main_container, text="Detalles de Factura", 
                                 bg="white", padx=10, pady=10)
    frame_detalles.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
    
    # Configuración responsive del frame de detalles
    for i in range(4):
        frame_detalles.columnconfigure(i, weight=1 if i % 2 == 1 else 0)
    frame_detalles.rowconfigure(3, weight=1)
    
    # Producto
    tk.Label(frame_detalles, text="Producto:", bg="white", anchor="w").grid(
        row=0, column=0, sticky="ew", padx=5, pady=5)
    
    productos = [f"{p.id} - {p.nombre}" for p in ProductoCRUD().listar()]
    combo_producto = ttk.Combobox(frame_detalles, values=productos, state="readonly")
    combo_producto.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    
    # Cantidad
    tk.Label(frame_detalles, text="Cantidad:", bg="white", anchor="w").grid(
        row=0, column=2, sticky="ew", padx=5, pady=5)
    
    entry_cantidad = tk.Entry(frame_detalles)
    entry_cantidad.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
    
    # Precio Unitario
    tk.Label(frame_detalles, text="Precio Unitario:", bg="white", anchor="w").grid(
        row=1, column=0, sticky="ew", padx=5, pady=5)
    
    entry_precio = tk.Entry(frame_detalles)
    entry_precio.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    
    # Botones de detalles
    btn_frame = tk.Frame(frame_detalles, bg="white")
    btn_frame.grid(row=1, column=2, columnspan=2, sticky="e", padx=5, pady=5)
    
    btn_agregar_detalle = tk.Button(btn_frame, text="Agregar Detalle", bg="#4CAF50", fg="white")
    btn_agregar_detalle.pack(side=tk.LEFT, padx=2)
    
    # Tabla de detalles
    columns = ("Producto", "Cantidad", "Precio Unitario", "Subtotal")
    tree_detalles = ttk.Treeview(frame_detalles, columns=columns, show="headings", height=4)
    
    for col in columns:
        tree_detalles.heading(col, text=col)
        tree_detalles.column(col, width=120, stretch=True)
    
    tree_detalles.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
    
    # Scrollbar para la tabla de detalles
    scroll_detalles = ttk.Scrollbar(frame_detalles, orient="vertical", command=tree_detalles.yview)
    scroll_detalles.grid(row=2, column=4, sticky="ns")
    tree_detalles.configure(yscrollcommand=scroll_detalles.set)
    
    # Total
    tk.Label(frame_detalles, text="Total:", bg="white", font=("Arial", 10, "bold"), 
            anchor="e").grid(row=3, column=2, sticky="e", padx=5, pady=5)
    
    lbl_total = tk.Label(frame_detalles, text="0.00", bg="white", 
                       font=("Arial", 10, "bold"), anchor="w")
    lbl_total.grid(row=3, column=3, sticky="w", padx=5, pady=5)
    
    # ----------------- Sección Listado Facturas -----------------
    frame_lista = tk.LabelFrame(main_container, text="Facturas Registradas", 
                              bg="white", padx=10, pady=10)
    frame_lista.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
    frame_lista.columnconfigure(0, weight=1)
    frame_lista.rowconfigure(0, weight=1)
    
    # Tabla de facturas
    columns_facturas = ("ID", "Cliente", "Fecha", "Total")
    tree_facturas = ttk.Treeview(frame_lista, columns=columns_facturas, show="headings", height=8)
    
    for col in columns_facturas:
        tree_facturas.heading(col, text=col)
        tree_facturas.column(col, width=120, stretch=True)
    
    tree_facturas.grid(row=0, column=0, sticky="nsew")
    
    # Scrollbars para la tabla de facturas
    scroll_y = ttk.Scrollbar(frame_lista, orient="vertical", command=tree_facturas.yview)
    scroll_y.grid(row=0, column=1, sticky="ns")
    
    scroll_x = ttk.Scrollbar(frame_lista, orient="horizontal", command=tree_facturas.xview)
    scroll_x.grid(row=1, column=0, sticky="ew")
    
    tree_facturas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    
    # ----------------- Botones Principales -----------------
    frame_botones = tk.Frame(main_container, bg="white")
    frame_botones.grid(row=4, column=0, pady=10, sticky="ew")
    
    btn_guardar = tk.Button(frame_botones, text="Guardar Factura", bg="#2196F3", fg="white", width=15)
    btn_guardar.pack(side=tk.LEFT, padx=5, expand=True)
    
    btn_eliminar = tk.Button(frame_botones, text="Eliminar Factura", bg="#F44336", fg="white", width=15)
    btn_eliminar.pack(side=tk.LEFT, padx=5, expand=True)
    
    btn_limpiar = tk.Button(frame_botones, text="Limpiar Formulario", bg="#FF9800", fg="white", width=15)
    btn_limpiar.pack(side=tk.LEFT, padx=5, expand=True)
    
    btn_regresar = tk.Button(frame_botones, text="Regresar", bg="#607D8B", fg="white", width=15,
                           command=lambda: [ventana.destroy(), ventana_principal.deiconify()])
    btn_regresar.pack(side=tk.LEFT, padx=5, expand=True)
    
    # ----------------- Funcionalidades -----------------
    def calcular_total():
        total = 0.0
        for child in tree_detalles.get_children():
            valores = tree_detalles.item(child)['values']
            subtotal = float(valores[2]) * int(valores[1])
            total += subtotal
        lbl_total.config(text=f"{total:.2f}")
    
    def agregar_detalle():
        producto = combo_producto.get()
        cantidad = entry_cantidad.get()
        precio = entry_precio.get()

        if not all([producto, cantidad, precio]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            id_producto = int(producto.split(" - ")[0])
            cantidad = int(cantidad)
            precio = float(precio)
            
            if cantidad <= 0 or precio <= 0:
                messagebox.showerror("Error", "Los valores deben ser positivos")
                return

            subtotal = cantidad * precio
            nombre_producto = producto.split(" - ")[1]

            tree_detalles.insert("", tk.END, values=(
                nombre_producto, 
                cantidad, 
                f"{precio:.2f}", 
                f"{subtotal:.2f}"
            ))

            combo_producto.set('')
            entry_cantidad.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            calcular_total()

        except ValueError:
            messagebox.showerror("Error", "Valores inválidos")
    
    def guardar_factura():
        cliente = combo_cliente.get()
        fecha = entry_fecha.get()
        detalles = []

        if not cliente:
            messagebox.showerror("Error", "Seleccione un cliente")
            return

        if not tree_detalles.get_children():
            messagebox.showerror("Error", "Agregue al menos un detalle")
            return

        try:
            for child in tree_detalles.get_children():
                valores = tree_detalles.item(child)['values']
                id_producto = int([p.split(" - ")[0] for p in productos if valores[0] in p][0])
                detalles.append(DetalleFactura)(
                    id_producto=id_producto,
                    cantidad=int(valores[1]),
                    precio_unitario=float(valores[2])
                )

            id_cliente = [c.id for c in ClienteCRUD().listar() if c.nombre == cliente][0]
            total = float(lbl_total.cget("text"))

            nueva_factura = Factura(
                id_cliente=id_cliente,
                fecha=fecha,
                total=total,
                detalles=detalles
            )

            FacturaCRUD().crear(nueva_factura)
            cargar_facturas()
            messagebox.showinfo("Éxito", "Factura guardada correctamente")
            limpiar_formulario()

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def eliminar_factura():
        seleccion = tree_facturas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una factura para eliminar")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta factura?")
        if confirmar:
            id_factura = int(tree_facturas.item(seleccion[0])['values'][0])
            FacturaCRUD().eliminar(id_factura)
            cargar_facturas()
            messagebox.showinfo("Éxito", "Factura eliminada correctamente")
    
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
    
    # Configurar eventos
    btn_agregar_detalle.config(command=agregar_detalle)
    btn_guardar.config(command=guardar_factura)
    btn_eliminar.config(command=eliminar_factura)
    btn_limpiar.config(command=limpiar_formulario)
    
    # Manejar redimensionamiento
    def on_resize(event):
        # Ajustar altura de las tablas según el tamaño de la ventana
        new_height = max(4, (ventana.winfo_height() - 400) // 30)
        tree_detalles.configure(height=new_height)
        tree_facturas.configure(height=new_height + 2)
    
    ventana.bind("<Configure>", on_resize)
    
    # Cargar datos iniciales
    cargar_facturas()
    
    # Centrar ventana
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f"{width}x{height}+{x}+{y}")