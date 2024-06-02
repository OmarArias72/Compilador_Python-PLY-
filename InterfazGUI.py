import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from Analizador_lexico import analizador
from Analizador_sintactico import parser
from Analizador_lexico import resultado_lexema
#from Analizador_sintactico import resultado_gramatica
#import ply.yacc as yacc
from Documentador import*
from Prueba_analizador_sintactico import*


class CompilerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador")

        # Botones
        buttons_frame = tk.Frame(root)
        buttons_frame.grid(row=0, column=0, columnspan=4, pady=(5, 0))
        btn_clear = tk.Button(buttons_frame, text="Limpiar campos", command=self.clear_fields)
        btn_clear.grid(row=0, column=0, padx=5,pady=5)
        btn_lexical_analysis = tk.Button(buttons_frame, text="Análisis léxico", command=self.lexical_analysis)
        btn_lexical_analysis.grid(row=0, column=1, padx=5,pady=5)
        btn_compile = tk.Button(buttons_frame, text="Compilar", command=self.compile_code)
        btn_compile.grid(row=0, column=2, padx=5,pady=5)
        btn_export_pdf = tk.Button(buttons_frame, text="Exportar PDF", command=self.export_pdf)
        btn_export_pdf.grid(row=0, column=3, padx=5,pady=5)
        btn_export_pdf = tk.Button(buttons_frame, text="Exportar archivo .py", command=self.export_py)
        btn_export_pdf.grid(row=0, column=4, padx=5,pady=5)

        # Cuadro de entrada de texto
        self.textbox = tk.Text(root, wrap="word",width=50)
        self.textbox.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.textbox.bind("<Key>", self.update_line_numbers)
        self.textbox_scroll = ttk.Scrollbar(root, orient="vertical", command=self.textbox.yview)
        self.textbox_scroll.grid(row=1, column=4, sticky="ns")
        self.textbox.configure(yscrollcommand=self.textbox_scroll.set)

        # Cuadro de salida de texto con scroll
        self.output_text = tk.Text(root, wrap="word", height=10, width=57)  # Ajustar el tamaño
        self.output_text.grid(row=1, column=6, padx=5, pady=5, sticky="nsew")
        self.output_text_scroll = ttk.Scrollbar(root, orient="vertical", command=self.output_text.yview)
        self.output_text_scroll.grid(row=1, column=7, sticky="ns")
        self.output_text.configure(yscrollcommand=self.output_text_scroll.set)

        # Números de línea más compactos
        self.line_numbers = tk.Text(root, width=2, padx=3, pady=3, bg="lightgray", state="disabled")  # Ajustar el width
        self.line_numbers.grid(row=1, column=0, sticky="nsew")

        # Frame para la tabla de tokens con scroll
        token_frame = tk.Frame(root)
        token_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Tabla de tokens
        self.token_table = ttk.Treeview(token_frame, columns=("Token", "Lexema", "Linea"))
        self.token_table.heading("Token", text="Token")
        self.token_table.heading("Lexema", text="Lexema")
        self.token_table.heading("Linea", text="Linea")
        self.token_table.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Scrollbar para la tabla de tokens
        token_scroll = ttk.Scrollbar(token_frame, orient="vertical", command=self.token_table.yview)
        token_scroll.grid(row=0, column=1, sticky="ns")
        self.token_table.configure(yscrollcommand=token_scroll.set)

    def update_line_numbers(self, event=None):
        lines = self.textbox.get(1.0, "end-1c").split("\n")
        line_numbers_text = "\n".join(str(i) for i in range(1, len(lines)+1))
        self.line_numbers.config(state="normal")
        self.line_numbers.delete(1.0, "end")
        self.line_numbers.insert(1.0, line_numbers_text)
        self.line_numbers.config(state="disabled")

    def clear_fields(self):
        self.textbox.delete(1.0, "end")
        self.output_text.delete(1.0, "end")
        self.token_table.delete(*self.token_table.get_children())
        self.line_numbers.config(state="normal")
        self.line_numbers.delete(1.0, "end")
        self.line_numbers.config(state="disabled")
        self.output_text.delete(1.0, "end")

    def lexical_analysis(self):
        global counter
        counter=1
        # Obtener el texto del cuadro de texto
        text_content = self.textbox.get(1.0, "end-1c")
        # Dividir el texto en líneas
        lines = text_content.split("\n")
        # Llamar al analizador léxico para cada línea
        for line in lines:
            tokens = self.tokenize(line,counter)
            self.update_token_table(tokens)
            counter +=1

    def tokenize(self, data,counter):
        
        # Resetear resultado_lexema para evitar que acumule resultados de análisis anteriores
        resultado_lexema.clear()
        # Inicializar el analizador léxico
        analizador.input(data)
        tokens = []
        # Tokenize
        while True:
            tok = analizador.token()
            if not tok: 
                break      # No more input
            tokens.append((tok.type, tok.value, counter))
            
        
        return tokens

    def update_token_table(self, tokens):
        # Limpiar la tabla de tokens
        #self.token_table.delete(*self.token_table.get_children())
        # Agregar los tokens a la tabla
        for token in tokens:
            self.token_table.insert("", "end", values=token)

    def compile_code(self):
        global compiladoCompleto
        text_content = self.textbox.get(1.0, "end-1c")
        self.output_text.delete(1.0, "end")
        errores_sintaxis.clear()
        separar_codigo(text_content)
        if(errores_sintaxis==None or len(errores_sintaxis)==0):
            compiladoCompleto=True
            self.output_text.insert("end", "Compilacion realizada no se detectaron errores" + "\n")
        else:
            compiladoCompleto=False
            for i in errores_sintaxis:
                self.output_text.insert("end", i+"\n")

       
        
    def export_pdf(self):
    # Obtener el texto del cuadro de texto
        if compiladoCompleto:
            text_content = self.textbox.get(1.0, "end-1c")
            limpiar_arreglos()
            obtener_encabezados(text_content)
            if not verificar_encabezados():
                messagebox.showinfo("Error", "Asegurase de escribir los encabezados al principio del codigo.\n"
                                    + "Sigue el siguiente formato: \nNombre: Segundo Nombre (Opcional) Apellido Paterno Apellido Materno\n"
                                    + "Numero: +521 7245879023, 7894572901 o (+521) 7489704327\n"
                                    + "Correo electronico: john.doe@example.com/alice.smith123@email-example.com/juan.perez@email-123.net")
                return 
            documentar_lineas()

            # Abrir el cuadro de diálogo para seleccionar la ubicación del archivo
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

            if file_path:
                # Generar el PDF
                c = canvas.Canvas(file_path, pagesize=letter)

                # Ajustar el tamaño de la fuente
                c.setFont("Helvetica", 10)  # Tamaño de fuente 10

                y_coordinate = 750  # Posición vertical inicial
                for line in lineas_documentadas:
                    # Convertir la línea a cadena si no lo es
                    if line is None:
                        line = ""
                    else:
                        line = str(line)
                    # Dividir las líneas largas en varias líneas más cortas usando simpleSplit
                    wrapped_lines = simpleSplit(line, "Helvetica", 10, 450)  # Ajustar el ancho según sea necesario
                    for wrapped_line in wrapped_lines:
                        if y_coordinate < 40:
                            c.showPage()
                            c.setFont("Helvetica", 10)
                            y_coordinate = 750
                        c.drawString(100, y_coordinate, wrapped_line)
                        y_coordinate -= 15  # Ajustar la posición vertical para la próxima línea

                c.save()
                messagebox.showinfo("Mensaje", "Archivo PDF creado con éxito")
        else:
            messagebox.showinfo("Mensaje", "No se puede exportar el PDF ya que el codigo tiene errores")

            
    def export_py(self):
        text_content = self.textbox.get(1.0, "end-1c")
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_content)
        messagebox.showinfo("Mensaje", "Archivo .py creado con éxito")
                
if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerApp(root)
    root.mainloop()
