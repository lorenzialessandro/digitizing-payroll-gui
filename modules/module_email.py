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

    #print(attachments)

    
    # Attach file
    if(os.path.isfile(path_attachment)):
        draft.Attachments.Add(path_attachment)

    # Save the draft
    draft.Save()

    print("Draft email created successfully.")