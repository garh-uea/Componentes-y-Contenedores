import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkcalendar import DateEntry


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("1000x620")
        self.root.configure(bg="snow")
        self.eventos = []
        self.configurar_estilo()
        self.crear_interfaz()

    def configurar_estilo(self):
        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("Treeview", background="white", foreground="black", fieldbackground="white",
                              font=("Arial", 10))
        self.estilo.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="light grey",
                              foreground="black")
        self.estilo.configure("TButton", font=("Arial", 11), background="light grey")
        self.estilo.configure("TLabel", font=("Arial", 11), background="gray90", foreground="black")
        self.estilo.configure("TRadiobutton", background="gray90", foreground="black", font=("Arial", 11))
        self.estilo.map("TRadiobutton", background=[("active", "gray90")])

    def crear_interfaz(self):
        # Frame para formulario de entrada
        frame_formulario = ttk.LabelFrame(self.root, text="Nuevo Evento/Tarea", padding=10)
        frame_formulario.pack(fill=tk.X, padx=10, pady=10)

        # Primera fila: Título y Categoría
        frame_fila1 = ttk.Frame(frame_formulario)
        frame_fila1.pack(fill=tk.X, pady=5)

        ttk.Label(frame_fila1, text="Título:", width=10).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entrada_titulo = ttk.Entry(frame_fila1, width=100)
        self.entrada_titulo.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_fila1, text="Categoría:", width=10).grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.categoria_var = tk.StringVar()
        categorias = ["Trabajo", "Personal", "Salud", "Estudios", "Otro"]
        self.menu_categoria = ttk.Combobox(frame_fila1, textvariable=self.categoria_var, values=categorias, width=15)
        self.menu_categoria.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.menu_categoria.current(0)

        # Segunda fila: Fecha y Hora
        frame_fila2 = ttk.Frame(frame_formulario)
        frame_fila2.pack(fill=tk.X, pady=5)

        ttk.Label(frame_fila2, text="Fecha:", width=10).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entrada_fecha = DateEntry(frame_fila2, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.entrada_fecha.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_fila2, text="Hora:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        # Separar hora y minutos en dos menús desplegables
        self.hora_var = tk.StringVar()
        horas = [f"{h:02d}" for h in range(24)]
        self.menu_hora = ttk.Combobox(frame_fila2, textvariable=self.hora_var, values=horas, width=5)
        self.menu_hora.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.menu_hora.current(0)

        ttk.Label(frame_fila2, text=":").grid(row=0, column=4, padx=0, pady=5, sticky=tk.W)

        self.minuto_var = tk.StringVar()
        minutos = [f"{m:02d}" for m in range(0, 60, 1)]
        self.menu_minuto = ttk.Combobox(frame_fila2, textvariable=self.minuto_var, values=minutos, width=5)
        self.menu_minuto.grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)
        self.menu_minuto.current(0)

        # Tercera fila: Prioridad
        frame_fila3 = ttk.Frame(frame_formulario)
        frame_fila3.pack(fill=tk.X, pady=5)

        ttk.Label(frame_fila3, text="Prioridad:", width=10).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.prioridad_var = tk.StringVar(value="Media")
        self.radio_alta = ttk.Radiobutton(frame_fila3, text="Alta", variable=self.prioridad_var, value="Alta")
        self.radio_alta.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.radio_media = ttk.Radiobutton(frame_fila3, text="Media", variable=self.prioridad_var, value="Media")
        self.radio_media.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.radio_baja = ttk.Radiobutton(frame_fila3, text="Baja", variable=self.prioridad_var, value="Baja")
        self.radio_baja.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        # Cuarta fila: Descripción
        frame_fila4 = ttk.Frame(frame_formulario)
        frame_fila4.pack(fill=tk.X, pady=5)

        ttk.Label(frame_fila4, text="Descripción:", width=10).grid(row=0, column=0, padx=5, pady=5, sticky=tk.NW)
        self.entrada_desc = scrolledtext.ScrolledText(frame_fila4, width=70, height=5, wrap=tk.WORD)
        self.entrada_desc.grid(row=0, column=1, columnspan=5, padx=5, pady=5, sticky=tk.W)

        # Frame para botones de acción
        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(fill=tk.X, padx=10, pady=5)

        self.btn_agregar = ttk.Button(frame_botones, text="Añadir", command=self.añadir_evento)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)
        self.btn_modificar = ttk.Button(frame_botones, text="Modificar", command=self.modificar_evento)
        self.btn_modificar.pack(side=tk.LEFT, padx=5)
        self.btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)
        self.btn_completar = ttk.Button(frame_botones, text="Marcar como Completado", command=self.marcar_completado)
        self.btn_completar.pack(side=tk.LEFT, padx=5)
        self.btn_detalles = ttk.Button(frame_botones, text="Detalles del Evento", command=self.ver_detalles_boton)
        self.btn_detalles.pack(side=tk.LEFT, padx=5)

        # Frame para la tabla de eventos
        frame_tabla = ttk.Frame(self.root)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear tabla con scrollbar
        self.scrollbar_y = ttk.Scrollbar(frame_tabla)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_x = ttk.Scrollbar(frame_tabla, orient=tk.HORIZONTAL)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree = ttk.Treeview(frame_tabla,
                                 columns=(
                                 "Fecha", "Hora", "Título", "Categoría", "Prioridad", "Descripción", "Completado"),
                                 show="headings",
                                 yscrollcommand=self.scrollbar_y.set,
                                 xscrollcommand=self.scrollbar_x.set)

        self.scrollbar_y.config(command=self.tree.yview)
        self.scrollbar_x.config(command=self.tree.xview)

        # Configurar columnas
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Prioridad", text="Prioridad")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Completado", text="Completado")

        # Configurar anchos de columna
        self.tree.column("Fecha", width=80)
        self.tree.column("Hora", width=60)
        self.tree.column("Título", width=150)
        self.tree.column("Categoría", width=100)
        self.tree.column("Prioridad", width=80)
        self.tree.column("Descripción", width=250)
        self.tree.column("Completado", width=100)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.tag_configure("completado", foreground="gray")

    def añadir_evento(self):
        titulo = self.entrada_titulo.get()
        if not titulo:
            messagebox.showerror("Error", "El título no puede estar vacío")
            return

        fecha = self.entrada_fecha.get()
        hora = f"{self.hora_var.get()}:{self.minuto_var.get()}"
        desc = self.entrada_desc.get("1.0", tk.END).strip()
        categoria = self.categoria_var.get()
        prioridad = self.prioridad_var.get()

        nuevo_evento = {
            "fecha": fecha,
            "hora": hora,
            "titulo": titulo,
            "desc": desc,
            "categoria": categoria,
            "prioridad": prioridad,
            "completado": False
        }

        self.eventos.append(nuevo_evento)
        self.tree.insert("", tk.END, values=(
            fecha, hora, titulo, categoria, prioridad,
            desc[:30] + "..." if len(desc) > 30 else desc, "No"
        ))

        self.limpiar_campos()

    def modificar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Información", "Seleccione un evento para modificar")
            return

        item = seleccionado[0]
        valores = self.tree.item(item, "values")
        indice = self.obtener_indice_evento(item)

        if indice is not None:
            # Cargar datos en el formulario
            self.entrada_titulo.delete(0, tk.END)
            self.entrada_titulo.insert(0, valores[2])

            self.entrada_fecha.set_date(valores[0])

            hora, minuto = valores[1].split(":")
            self.hora_var.set(hora)
            self.minuto_var.set(minuto)

            self.categoria_var.set(valores[3])
            self.prioridad_var.set(valores[4])

            self.entrada_desc.delete("1.0", tk.END)
            self.entrada_desc.insert("1.0", self.eventos[indice]["desc"])

            # Eliminar el evento y la entrada de la tabla
            self.eventos.pop(indice)
            self.tree.delete(item)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Información", "Seleccione un evento para eliminar")
            return

        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmacion:
            for item in seleccionado:
                indice = self.obtener_indice_evento(item)
                if indice is not None:
                    self.eventos.pop(indice)
                self.tree.delete(item)

    def marcar_completado(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Información", "Seleccione un evento para marcar como completado")
            return

        item = seleccionado[0]
        indice = self.obtener_indice_evento(item)

        if indice is not None:
            self.eventos[indice]["completado"] = not self.eventos[indice]["completado"]
            estado = "Sí" if self.eventos[indice]["completado"] else "No"

            valores = list(self.tree.item(item, "values"))
            valores[6] = estado
            self.tree.item(item, values=valores)

            if self.eventos[indice]["completado"]:
                self.tree.item(item, tags=("completado",))
            else:
                self.tree.item(item, tags=())

    def obtener_indice_evento(self, item_id):
        valores = self.tree.item(item_id, "values")
        if not valores:
            return None

        for i, evento in enumerate(self.eventos):
            if (evento["fecha"] == valores[0] and
                    evento["hora"] == valores[1] and
                    evento["titulo"] == valores[2]):
                return i
        return None

    def ver_detalles_boton(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Información", "Seleccione un evento para ver detalles")
            return
        self.mostrar_detalles(seleccionado[0])

    def mostrar_detalles(self, item):
        indice = self.obtener_indice_evento(item)
        if indice is None:
            return

        evento = self.eventos[indice]
        ventana_detalles = tk.Toplevel(self.root)
        ventana_detalles.title("Detalles del Evento")
        ventana_detalles.geometry("500x400")
        ventana_detalles.configure(bg="lightgray")

        frame_detalles = ttk.LabelFrame(ventana_detalles, text="Información del Evento", padding=10)
        frame_detalles.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(frame_detalles, text="Título:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(frame_detalles, text=evento["titulo"]).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_detalles, text="Fecha:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(frame_detalles, text=evento["fecha"]).grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_detalles, text="Hora:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(frame_detalles, text=evento["hora"]).grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_detalles, text="Categoría:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(frame_detalles, text=evento["categoria"]).grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_detalles, text="Prioridad:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(frame_detalles, text=evento["prioridad"]).grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_detalles, text="Completado:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(frame_detalles, text="Sí" if evento["completado"] else "No").grid(row=5, column=1, padx=5, pady=5,
                                                                                    sticky=tk.W)

        ttk.Label(frame_detalles, text="Descripción:").grid(row=6, column=0, padx=5, pady=5, sticky=tk.NW)

        desc_text = scrolledtext.ScrolledText(frame_detalles, width=40, height=8, wrap=tk.WORD)
        desc_text.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
        desc_text.insert(tk.END, evento["desc"])
        desc_text.config(state=tk.DISABLED)

    def limpiar_campos(self):
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_desc.delete("1.0", tk.END)
        self.hora_var.set("00")
        self.minuto_var.set("00")
        self.categoria_var.set("Trabajo")
        self.prioridad_var.set("Media")


root = tk.Tk()
app = AgendaPersonal(root)
root.mainloop()