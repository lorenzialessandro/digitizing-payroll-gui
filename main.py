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
            print(res)
            m.create_draft_email("Cedolino", "In allegato", res, None, None, None)
            # create_draft_email(res, file_name)
