from pdf2txt import *
from txt2speech import *

pdf_path = "inputs/principles-ray_dalio.pdf"
pages_folder_path = f"outputs/principles-ray_dalio"
convert_pdf_to_text(pdf_path, pages_folder_path)
correction_function(pdf_path, pages_folder_path, ["© 2011 Ray Dalio"], [0], [0, 1, 2])
unification_function(pdf_path, pages_folder_path, 2)

txt_content = open(f"outputs/principles-ray_dalio.txt", 'r', encoding='utf-8').read()
convert_text_to_speech(txt_content, "outputs/principles-ray_dalio")