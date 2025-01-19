# PDF Merger By Folder
This Python script automates the merging of PDF files in subfolders of a selected directory. 
It generates a single combined PDF per subfolder and removes the original files automatically. 
Ideal for organizing and simplifying large collections of PDFs.

## Features
- Merges all PDFs in each subfolder into a single file named `combined.pdf`.
- Automatically deletes the original PDFs after merging.
- Simple and user-friendly graphical interface using Tkinter.
- Fast and reliable processing of PDF files.

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

Example.
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
- This project is licensed under the **MIT License**.
- For more details, see the [LICENSE](LICENSE) file included in this repository.

## Contributing
- Contributions are highly encouraged and appreciated!
- To contribute:
  1. **Fork** this repository to your GitHub account.
  2. Create a new branch for your changes:
     ```bash
     git checkout -b feature-name
     ```
  3. Make your changes and commit them:
     ```bash
     git commit -m "Describe your changes here"
     ```
  4. Push the branch to your fork:
     ```bash
     git push origin feature-name
     ```
  5. Open a **Pull Request** to propose your changes.
 
  ## Author
- This project was developed by **Enrique Caicedo**.
- Connect with me on GitHub: [jenriquecdev](https://github.com/jenriquecdev).
