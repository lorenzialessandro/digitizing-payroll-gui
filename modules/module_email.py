import win32com.client
import os

def create_draft_email(subject, body, to, cc=None, bcc=None, path_attachment=None):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    draft = outlook.GetDefaultFolder(16).Items.Add(0)

    draft.Subject = subject
    draft.Body = body

    # Add recipients
    draft.To = to
    if cc:
        draft.CC = cc
    if bcc:
        draft.BCC = bcc
    
    # Attach file
    if(os.path.isfile(path_attachment)):
        draft.Attachments.Add(path_attachment)

    # Save the draft
    draft.Save()

    print("Draft email created successfully.")
    

def send_all_drafts():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    drafts_folder = outlook.GetDefaultFolder(16)  # 16 represents the Drafts folder

    # Access all items in the Drafts folder
    drafts = drafts_folder.Items

    for draft in drafts:
        if draft.Subject:  # Check if the draft has a subject (to exclude empty drafts)
            try:
                print(f"Sent draft: {draft.Subject}")
                draft.Send()  # Send the draft
            except Exception as e:
                print(f"Error sending draft '{draft.Subject}': {e}")