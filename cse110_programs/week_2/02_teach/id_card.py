# creates a "card" boarder
boarder = "---------------------------------"

print("Please enter the following information:\n")

first_name = input("First name: ")
last_name = input("Least name: ")
email = input("Email address: ")
phone_num = input("Phone number: ")
job = input("Job title: ")
id_num = input("ID Number: ")
# stretch activity variables

# prints ID Card
print(f"\nThe ID Card is:\n {boarder}")
print(f"{last_name.upper()}, {first_name.title()}")
print(f"{job.title()}")
print(f"ID: {id_num}\n")
print(f"\n{email.lower()}")
print(f"{phone_num}")

# stretch activity info
# Hair color, eye color, month started, advanced training certification(bool?)
print(boarder)
print() #Empty space