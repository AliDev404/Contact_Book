import csv

error="\aInvalid Input!"

def Add():
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
				while True:
					number=(input("Phone Number: "))
					if number.isspace() or len(number)==0 or any(char.isalpha() for char in numbers):
						print(error)
					else:
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


Add()