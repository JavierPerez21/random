import PyPDF2
import os


def convert_pdf_to_text(pdf_path: str, pages_folder_path: str) -> None:
    pdffileobj = open(pdf_path, 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)
    x = pdfreader.numPages
    if not os.path.exists(pages_folder_path):
        os.mkdir(pages_folder_path)
    for i in range(0, x):
        print(i)
        pageobj = pdfreader.getPage(i)
        text = pageobj.extractText()
        file1 = open(f"{pages_folder_path}/pg-{str(i).zfill(4)}.txt", "w", encoding='utf-8')
        file1.writelines(text)
        

def correction_function(pdf_path: str, pages_folder_path: str, keywords_to_remove: list = ["© 2011 Ray Dalio"],
                        lines_to_remove: list = [0], ignore_pages: list = [0, 1, 2]) -> None:
    for (_, _, pages) in os.walk(pages_folder_path):
        break
    for pg in pages:
        if int(pg.replace("pg-", "").replace(".txt", "")) in ignore_pages:
            continue
        pg_input = open(f"{pages_folder_path}/{pg}", 'r', encoding='utf-8')
        lines = pg_input.readlines()
        new_lines = [lines[i] for i in range(0, len(lines)) if i not in lines_to_remove]
        new_lines = "".join(new_lines)
        for keyword in keywords_to_remove:
            new_lines = new_lines.replace(keyword, "")
        pg_output = open(f"{pages_folder_path}/{pg}", 'w', encoding='utf-8')
        pg_output.writelines(new_lines)


def unification_function(pdf_path: str, pages_folder_path: str, first_page: int = 2):
    for (_, _, pages) in os.walk(pages_folder_path):
        break
    txt_content = []
    for pg in pages:
        if int(pg.replace("pg-", "").replace(".txt", "")) < first_page:
            continue
        pg_input = open(f"{pages_folder_path}/{pg}", 'r', encoding='utf-8')
        lines = "".join(pg_input.readlines())
        txt_content.append(lines)
    txt_content = "\n".join(txt_content)
    file = open(f"{pages_folder_path}.txt", 'w', encoding='utf-8')
    file.writelines(txt_content)
