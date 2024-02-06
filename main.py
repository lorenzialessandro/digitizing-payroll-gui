import tkinter as tk
from tkinter import filedialog
import os
import modules as m


def browse_pdf():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filename:
        pdf_entry.delete(0, tk.END)
        pdf_entry.insert(0, filename)
        check_enable_generate_button()

def browse_excel():
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if filename:
        excel_entry.delete(0, tk.END)
        excel_entry.insert(0, filename)
        check_enable_generate_button()

def check_enable_generate_button():
    if pdf_entry.get() and excel_entry.get():
        generate_button.config(state=tk.NORMAL)
    else:
        generate_button.config(state=tk.DISABLED)


def check_enable_send_button():
    if generate_button.cget("state") == tk.NORMAL:
        send_button.config(state=tk.NORMAL)
    else:
        send_button.config(state=tk.DISABLED)

def process_files():
    pdf_file = pdf_entry.get()
    excel_file = excel_entry.get()
    # Do something with the files
    print("PDF file:", pdf_file) #debug
    print("Excel file:", excel_file) #debug

    # --------------------------------------

    output_folder_path = 'data/output/' # Specify the folder path
    m.create_folder(output_folder_path) #create the folder
    m.remove_files_from_folder(output_folder_path)
    m.split_pdf(pdf_file,output_folder_path)

    for file_name in os.listdir(output_folder_path):
        file_path = os.path.join(output_folder_path, file_name)

        if os.path.isfile(file_path):
            cf_substring = file_name.split('_')[0]
            month_substring = file_name[file_name.find('_')+1:]
            res = m.search_excel(excel_file, cf_substring) 
            if res is not None:
                m.create_draft_email("Cedolino "+month_substring, "In allegato", res, None, None, path_attachment=os.path.abspath(file_path))

    check_enable_send_button()

def send_email():
    m.send_all_drafts()
    
    success_label = tk.Label(root, text="E-mail inviate con successo, è possibile chiudere il programma.")
    success_label.grid(row=4, column=1, padx=5, pady=5)



# --------------------------------------
# --------------------------------------


root = tk.Tk()
root.title("Gestione e invio cedolini")

pdf_label = tk.Label(root, text="Carica pdf cedolino unico:")
pdf_label.grid(row=0, column=0, padx=5, pady=5)

pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=5, pady=5)

pdf_button = tk.Button(root, text="Seleziona", command=browse_pdf, width=10)
pdf_button.grid(row=0, column=2, padx=5, pady=5)

excel_label = tk.Label(root, text="Carica foglio excel:")
excel_label.grid(row=1, column=0, padx=5, pady=5)

excel_entry = tk.Entry(root, width=50)
excel_entry.grid(row=1, column=1, padx=5, pady=5)

excel_button = tk.Button(root, text="Seleziona", command=browse_excel, width=10)
excel_button.grid(row=1, column=2, padx=5, pady=5)

generate_button = tk.Button(root, text="GENERA CEDOLINI E BOZZE E-MAIL", command=process_files, state=tk.DISABLED, width=50, height=2)
generate_button.grid(row=2, column=1, padx=5, pady=5)

send_button = tk.Button(root, text="INVIA TUTTE LE E-MAIL", command=send_email, state=tk.DISABLED, width=50, height=2)
send_button.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()