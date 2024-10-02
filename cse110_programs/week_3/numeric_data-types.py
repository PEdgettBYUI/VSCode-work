# Patrick T. Edgett
# The program below requests the age, number of egg cartons, and cookies the user has, & how many people there are to share said cookies with
# Returns Your age on your next birthday, how many eggs you have, and how many cookies each person gets
age = int(input("How old are you? "))
print(f"On your next birthday, you will be {age+1}\n")

eggs = int(input("How many egg cartons do you have? "))
#eggs = eggs*12
print(f"You have {eggs*12}.\n")

cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
print(f"Each person may have {cookies/people} cookies.\n")