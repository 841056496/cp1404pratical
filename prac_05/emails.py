def extract_name(email):
    return ' '.join(email.split('@')[0].split('.')).title()

email_to_name = {}

email = input("Email: ")
while email:
    extracted_name = extract_name(email)
    confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()

    if confirmation not in ['y', '']:
        extracted_name = input("Name: ")

    email_to_name[email] = extracted_name

    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
