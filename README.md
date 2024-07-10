 Readable PDFs Scanner

This project provides a Python script designed to determine the readability of PDF documents within a specified directory. The script identifies whether each PDF is readable (containing selectable and extractable text) or if it is a scanned document that would require Optical Character Recognition (OCR) for text extraction. This tool is particularly useful for processing large collections of PDFs where manual inspection would be time-consuming and inefficient.

#Features
- Automated PDF Scanning:The script scans through all PDF files in the provided directory.
- Readability Check: Utilizes the PyMuPDF library to extract text from each PDF, determining its readability based on the length of the extracted text.
- Excel Report Generation: Outputs the results into an Excel file (`PDF_Status.xlsx`), listing each document's name and its readability status ("Readable" or "Scanned pdf-OCR needed").
- User-Friendly:Easy-to-use command-line interface prompts the user for the folder path and handles the rest automatically.

#Usage
1. Prerequisites:Ensure you have Python installed along with the required libraries (`pandas`, `PyMuPDF`, and `openpyxl`).
   ```sh
   pip install pandas PyMuPDF openpyxl
   ```
2. Running the Script:
   - Place the script (`check_pdfs.py`) in the desired directory.
   - Open a terminal, navigate to the directory containing the script, and run:
     ```sh
     python check_pdfs.py
     ```
   - Enter the path to the folder containing the PDF files when prompted.
3. Output:
   - The script will analyze each PDF in the specified folder and generate an Excel file named `PDF_Status.xlsx` in the same folder, summarizing the readability status of each document.

This project aims to streamline the process of PDF readability assessment, saving time and effort for users who deal with large volumes of documents. Contributions and feedback are welcome to further enhance the functionality and usability of this tool.

---
