
import csv
import re


error="\aInvalid Input!"


def Run():
    start=str(input("1) Add\n2) Read\n3) End\n"))
    if start =="1":
        Add()
        Run()
    elif start =="2":
        Read()
        Run()
    elif start =="3":
        print("Ending...")
        return
    else:
        print(error)
        Run()


def Read():
    try:
        with open("book.csv", "r", newline="") as file:
            reader = csv.reader(file)
            contacts = list(reader)

            if not contacts:
                print("No contacts found.")
                return

            print("\n--- Contact List ---")
            for idx, row in enumerate(contacts, start=1):
                name = row[0] if len(row) > 0 else ""
                number = row[1] if len(row) > 1 else ""
                email = row[2] if len(row) > 2 else ""
                print(f"{idx}. Name: {name} | Phone: {number} | Email: {email if email else 'None'}")

    except FileNotFoundError:
        print("No contact book found. Add some contacts first.")

def Add():
    name = Name()
    number = Number()
    email = Email()

    with open("book.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, number, email if email else ""])  # Blank if None

    print(f"Name: {name}\nPhone Number: {number}\nEmail: {email}\nADDED")
    return




def Name():		
	while True:
			name=input("Name: ")
			try:
				if float(name) or name =="0": 
					print(error)
				else:
					pass
			except ValueError:
				if len(name)==0 or name.isspace():
					print(error)
				else:
					break
	return name

def Number():
    while True:
        number = input("Phone Number: ")
        cleaned_phone = re.sub(r'[^0-9+\-]', '', number)
        if not cleaned_phone:
            print(error + "Phone number is empty.")
            continue
        if cleaned_phone.count('+') > 1:
            print(error + "Only one '+' symbol is allowed.")
            continue
        if '+' in cleaned_phone and not cleaned_phone[1:].replace("-", "").isdigit():
            print(error + "After the '+', only digits (and optional '-') are allowed.")
            continue
        if not cleaned_phone.replace("-", "").isdigit() and not (cleaned_phone.startswith('+') and cleaned_phone[1:].replace("-", "").isdigit()):
            print(error + "Invalid phone number.")
            continue
        confirm = input(f"Is this number correct? {cleaned_phone} (Y/n): ").strip().lower()
        if confirm == 'y' or not confirm:
            print(f"Phone number saved: {cleaned_phone}")
            return cleaned_phone
        else:
            print("Let's try again.")


def Email():
    while True:
        email = input("Email (press Enter to skip): ").strip()
        if email == "":
            return "None"
        if "@" not in email or "." not in email:
            print("Error: Email must contain '@' and '.'")
            continue
        try:
            int(email) 
            print("Error: Email cannot be just numbers!")
        except ValueError:
            return email

Run()