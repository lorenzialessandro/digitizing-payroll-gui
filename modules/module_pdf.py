import fitz  # PyMuPDF
import re
import os

def split_pdf(input_pdf_path, output_folder):
    pdf_document = fitz.open(input_pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]

        page_text = page.get_text("text") # get page text

        fiscal_code = find_fiscal_code(page_text) #search cf
        month = find_first_month(page_text) #search month

        if(fiscal_code != None and month != None):
            output_pdf_path = f"{output_folder}/{fiscal_code}_{month}.pdf"

        
        output_pdf = fitz.open()
        output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

        
        output_pdf.save(output_pdf_path)
        output_pdf.close()

        # print(f"Page {page_num + 1} saved to {output_pdf_path}")


def find_fiscal_code(text):
    code_match = re.search(r'\b([A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z])\b', text)

    # return
    if code_match:
        return code_match.group(0)
    else:
        return None


def find_first_month(text):
    months = [
        'GENNAIO', 'FEBBRAIO', 'MARZO', 'APRILE', 'MAGGIO', 'GIUGNO',
        'LUGLIO', 'AGOSTO', 'SETTEMBRE', 'OTTOBRE', 'NOVEMBRE', 'DICEMBRE'
    ]

    pattern = re.compile(r'\b(?:' + '|'.join(months) + r')\b', re.IGNORECASE)
    match = pattern.search(text)

    #return
    if match:
        return match.group()
    else:
        return None



def remove_files_from_folder(folder_path):
    try:
        files = os.listdir(folder_path)

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

    except Exception as e:
        print(f"Error: {e}")

