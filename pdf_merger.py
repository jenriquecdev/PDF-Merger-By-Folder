import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from PyPDF2 import PdfMerger

def combinar_pdfs_por_carpeta(ruta_principal):
    """
    Combina todos los archivos PDF en cada subcarpeta de la ruta principal.
    Deja un único archivo combinado por carpeta y elimina los originales.
    """
    for carpeta, _, archivos in os.walk(ruta_principal):
        # Filtrar solo los archivos PDF
        pdfs = [os.path.join(carpeta, archivo) for archivo in archivos if archivo.endswith('.pdf')]
        
        if not pdfs:
            continue  # Saltar si no hay PDFs en la carpeta
        
        # Nombre del archivo combinado
        nombre_combinado = os.path.join(carpeta, "combinado.pdf")
        
        # Combinar PDFs
        merger = PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        
        merger.write(nombre_combinado)
        merger.close()
        
        # Eliminar los PDFs originales
        for pdf in pdfs:
            os.remove(pdf)
        
    messagebox.showinfo("Proceso Completado", f"Los PDF se han combinado exitosamente en {ruta_principal}")

def seleccionar_carpeta():
    """
    Abre un cuadro de diálogo para que el usuario seleccione la carpeta principal.
    """
    ruta_carpeta = filedialog.askdirectory(title="Selecciona la carpeta principal")
    if ruta_carpeta:
        label_carpeta.config(text=f"Carpeta seleccionada: {ruta_carpeta}")
        boton_combinar.config(state="normal")  # Habilitar el botón de combinar
        boton_combinar.config(command=lambda: combinar_pdfs_por_carpeta(ruta_carpeta))

# Crear la ventana principal
ventana = Tk()
ventana.title("Combinar PDFs por Carpeta")
ventana.geometry("500x200")

# Etiqueta de instrucciones
label_instrucciones = Label(ventana, text="Selecciona una carpeta principal para combinar los PDFs:", font=("Arial", 12))
label_instrucciones.pack(pady=10)

# Botón para seleccionar carpeta
boton_seleccionar = Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta, font=("Arial", 10))
boton_seleccionar.pack(pady=10)

# Etiqueta para mostrar la carpeta seleccionada
label_carpeta = Label(ventana, text="No se ha seleccionado ninguna carpeta", font=("Arial", 10), fg="gray")
label_carpeta.pack(pady=10)

# Botón para combinar PDFs
boton_combinar = Button(ventana, text="Combinar PDFs", state="disabled", font=("Arial", 10))
boton_combinar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
