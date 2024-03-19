import email
import imaplib

# Login to your email account
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('email', 'code')
mail.select('inbox')

# Search for the email you want to extract headers from
result, data = mail.search(None, 'ALL')

# Get the email data
email_ids = data[0].split()
latest_email_id = email_ids[-1]

# Fetch the email data
result, data = mail.fetch(latest_email_id, '(RFC822)')
raw_email = data[0][1]

# Parse the raw email
msg = email.message_from_bytes(raw_email)

# Extract the sender's email address from the headers
sender_email = msg['From']
print("Sender's Email Address:", sender_email)
raw_email = data[0][1]

# Parse the raw email
msg = email.message_from_bytes(raw_email)

# Extract and print the email headers
print("Email Headers:")
for key, value in msg.items():
    print(f"{key}: {value}")

# Extract and print the email content (body)
email_content = msg.get_payload()
print("\nEmail Content:")
print(email_content)
mail.logout()
