import re


text = "Example: Contact us at support@example.com or sales@company.com for assistance."
print(text)
text = input("ENTER TEXT: ");



email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'



email_addresses = re.findall(email_pattern, text, re.IGNORECASE)


for email in email_addresses:
    print("Found email address:", email)
