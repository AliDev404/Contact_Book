import csv
import re


error="\aInvalid Input!"

def Add():
	Name()
	Number()
	iscorrect=input(f"is the number correct? : {number} (y/n)").lower()
	if iscorrect == "y":
		email=input("Email:")
			try:
				int(email)
				print(error)
			except ValueError:
				print(f"Name: {name}\nPhone Number: {number}\nEmail: {email}\n ADDED")
				break
		elif iscorrect == "n":
			pass
		else:
			print(error)
	
				break	
	return

def Read():
	pass




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
	number=(input("Phone Number: "))

    cleaned_phone = re.sub(r'[^0-9+\-]', '', number)
    if not cleaned_phone:
        print(error+"Phone number is empty.")
    if cleaned_phone.count('+') > 1:
        print(error+"Only one '+' symbol is allowed.")
        if not cleaned_phone[1:].isdigit():
            print(error+"After the '+', only digits are allowed.")
    if cleaned_phone.isdigit():
    print(error+ "Invalid phone number.")


Add()