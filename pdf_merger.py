import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs_by_folder(main_directory):
    """
    Combines all PDF files in each subfolder of the main directory.
    Creates a single combined file per folder and deletes the original files.
    """
    for folder, _, files in os.walk(main_directory):
        # Filter only PDF files
        pdfs = [os.path.join(folder, file) for file in files if file.endswith('.pdf')]
        
        if not pdfs:
            continue  # Skip if no PDFs in the folder
        
        # Name of the combined file
        combined_filename = os.path.join(folder, "combined.pdf")
        
        # Merge PDFs
        merger = PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        
        merger.write(combined_filename)
        merger.close()
        
        # Delete the original PDFs
        for pdf in pdfs:
            os.remove(pdf)
        
    messagebox.showinfo("Process Completed", f"PDFs have been successfully merged in {main_directory}")

def select_directory():
    """
    Opens a dialog box for the user to select the main directory.
    """
    selected_directory = filedialog.askdirectory(title="Select the main directory")
    if selected_directory:
        label_directory.config(text=f"Selected directory: {selected_directory}")
        button_merge.config(state="normal")  # Enable the merge button
        button_merge.config(command=lambda: merge_pdfs_by_folder(selected_directory))

# Create the main window
window = Tk()
window.title("Merge PDFs by Folder")
window.geometry("500x200")

# Instruction label
label_instructions = Label(window, text="Select a main directory to merge PDFs:", font=("Arial", 12))
label_instructions.pack(pady=10)

# Button to select directory
button_select = Button(window, text="Select Directory", command=select_directory, font=("Arial", 10))
button_select.pack(pady=10)

# Label to display the selected directory
label_directory = Label(window, text="No directory selected", font=("Arial", 10), fg="gray")
label_directory.pack(pady=10)

# Button to merge PDFs
button_merge = Button(window, text="Merge PDFs", state="disabled", font=("Arial", 10))
button_merge.pack(pady=10)

# Run the window
window.mainloop()
