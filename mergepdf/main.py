import os
import glob
import PyPDF2


def merge_pdfs(pdf_files, output="merged.pdf"):
    # Create an empty PDF object
    merged_pdf = PyPDF2.PdfMerger()

    # Iterate over the PDF files and add them to the merged_pdf object
    for file in pdf_files:
        with open(file, 'rb') as f:
            merged_pdf.append(f)

    # Write the merged PDF to a new file
    with open(output, 'wb') as f:
        merged_pdf.write(f)

