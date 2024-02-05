import modules as m
import os


output_folder_path = 'data/output/' # Specify the folder path

m.remove_files_from_folder(output_folder_path)

m.split_pdf("data/input/cedolino.pdf","data/output/")


for file_name in os.listdir(output_folder_path):
    file_path = os.path.join(output_folder_path, file_name)

    if os.path.isfile(file_path):
        file_name_substring = file_name.split('_')[0]
        res = m.search_excel("data/input/sheet.xlsx", file_name_substring) 
        if res is not None:
             m.create_draft_email("Cedolino", "In allegato", res, None, None, path_attachment=os.path.abspath(file_path))

# ------
# console
user_input = input("Type 'yes' to execute the function: ")

if user_input.lower() == 'yes':
    m.send_all_drafts()
    print("Function executed successfully.")
else:
    print("Function not executed.")     
