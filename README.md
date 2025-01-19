# PDF Merger By Folder
This Python script automates the merging of PDF files in subfolders of a selected directory. 
It generates a single combined PDF per subfolder and removes the original files automatically. 
Ideal for organizing and simplifying large collections of PDFs.

## Features
- Merges all PDFs in each subfolder into a single file named `combined.pdf`.
- Automatically deletes the original PDFs after merging.
- Simple and user-friendly graphical interface using Tkinter.
- Fast and reliable processing of PDF files.

## Requirements
- **Python 3.6+**
- **Libraries**:
  - PyPDF2
  - Tkinter (pre-installed with Python on most systems)

Install the required library with the following command:
```bash
pip install PyPDF2

## How to Use
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/jenriquecdev/PDF-Merger-By-Folder.git
2. Navigate to the project directory:
cd PDF-Merger-By-Folder
3. Run the script:
python pdf_merger.py
4. A graphical window will appear:

    Click "Select Folder" to choose the main directory where your PDF files are stored.
    Click "Combine PDFs" to start the merging process.
5. The script will:

    Merge all PDF files in each subfolder into a single combined.pdf.
    Remove the original PDFs after merging.
    Notify you when the process is complete.

## Example
Imagine you have the following directory structure:
MainFolder/
│
├── Subfolder1/
│   ├── file1.pdf
│   ├── file2.pdf
│
├── Subfolder2/
│   ├── document1.pdf
│   ├── document2.pdf


After running the script:
MainFolder/
│
├── Subfolder1/
│   ├── combined.pdf
│
├── Subfolder2/
│   ├── combined.pdf


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request for any changes.

## Author
Developed by **Enrique Caicedo** ([GitHub Profile](https://github.com/jenriquecdev)).

