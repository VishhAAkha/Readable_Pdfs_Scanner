import os
import pandas as pd
import fitz  # PyMuPDF

def is_readable_pdf(file_path, text_length_threshold=100):
    try:
        document = fitz.open(file_path)
        total_text_length = 0
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text = page.get_text()
            total_text_length += len(text.strip())
            if total_text_length > text_length_threshold:
                return True
        return False
    except Exception as e:
        return False

def main():
    folder_path = input("Enter the folder path: ")
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Display the names and number of documents
    print(f"Found {len(pdf_files)} PDF documents in the folder:")
    for pdf_file in pdf_files:
        print(pdf_file)

    results = []

    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        if is_readable_pdf(file_path):
            results.append({'Document Name': pdf_file, 'Status': 'Readable'})
        else:
            results.append({'Document Name': pdf_file, 'Status': 'Scanned pdf-OCR needed'})

    df = pd.DataFrame(results)
    output_file = os.path.join(folder_path, 'PDF_Status.xlsx')
    
    try:
        df.to_excel(output_file, index=False)
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Failed to save results to Excel file: {e}")

if __name__ == "__main__":
    main()
