print("Welcome to the email address generator!")
first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
company_name = input("Enter your company name: ").lower()
first_letter = first_name[0]

print("Your email options:")
print(first_name + "." + last_name + "@" + company_name + ".com")
print(first_letter + "." + last_name + "@" + company_name + ".com")
print(last_name + "." + first_letter + "@" + company_name + ".com")