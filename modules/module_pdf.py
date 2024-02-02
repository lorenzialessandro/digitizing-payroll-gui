import fitz  # PyMuPDF
import re

def split_pdf(input_pdf_path, output_folder):
    pdf_document = fitz.open(input_pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]

        page_text = page.get_text("text") # get page text
        fiscal_code = extract_fiscal_code(page_text) #search cf
        
        output_pdf_path = f"{output_folder}/{fiscal_code}.pdf"

        
        output_pdf = fitz.open()
        output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

        
        output_pdf.save(output_pdf_path)
        output_pdf.close()

        # print(f"Page {page_num + 1} saved to {output_pdf_path}")


def extract_fiscal_code(text):
    code_match = re.search(r'\b([A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z])\b', text)

    # return
    if code_match:
        return code_match.group(0)
    else:
        return None