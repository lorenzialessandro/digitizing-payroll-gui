import modules as m
import os

m.split_pdf("data/input/cedolino.pdf","data/output/")



# print(m.search_excel("data/input/sheet.xlsx", "RSSMRA75L24F205O"))



folder_path = 'data/output/' # Specify the folder path

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        file_name_substring = file_name.split('_')[0]
        res = m.search_excel("data/input/sheet.xlsx", file_name_substring) 
        if res is not None:
             m.create_draft_email("Cedolino", "In allegato", res, None, None, path_attachment=os.path.abspath(file_path))
        