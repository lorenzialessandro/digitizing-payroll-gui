import win32com.client

def create_draft_email(subject, body, to, cc=None, bcc=None, attachments=None):
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

    # Attach files
    if attachments:
        for attachment in attachments:
            draft.Attachments.Add(attachment)

    # Save the draft
    draft.Save()

    print("Draft email created successfully.")