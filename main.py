
import csv
import re


error="\aInvalid Input!"

def Read():
	pass


def Add():
	name = Name()
	number= Number()
	email = Email()
	print(f"Name: {name}\nPhone Number: {number}\nEmail: {email}\n ADDED")
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


Add()