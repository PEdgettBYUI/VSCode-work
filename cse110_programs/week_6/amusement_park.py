# Amusement Park Ag &Height Checker
# Compares the age and height of a rider in inches to the required limits of a ride
# Patrick Edgett

first_age = int(input("What is the age of the first rider? "))
first_height = int(input("What is the height of the first rider in inches(round up if neccessary.)? "))

first_golden_pass = input("Do you have a Golden Passport(yes/no)? ").lower()
if first_golden_pass == "yes":
    first_age = 18
else:
    first_age = first_age
print(first_age)

second_golden_pass = ""
second_rider = 0

if first_height < 36:
    print("Rider is too short to ride. Come back next year.")    
else:
    second_rider = input("Is there a second rider (yes/no)? ").lower()
    if second_rider == "yes":
        second_age = int(input("What is the age of the second rider? "))
        second_height = int(input("What is the height of the second rider in inches(round up if neccessary.)? "))
        second_golden_pass = input("Do you have a Golden Passport(yes/no)? ").lower()
        if second_golden_pass == "yes" and second_height >= 36:
            print("Gold Riders detected. Enjoy the ride VIPs!")
        elif second_age >= 18 or first_age >= 18 and second_height >= 36:
            print("Riders permitted. Have a nice day!")
        elif (first_age >= 16 or second_age >= 16 and first_age >= 14 or second_age >= 14) and second_height >= 36:
            print("Mixed Youth riders accepted. Have a nice day!")
        elif first_age >= 12 and second_age >= 12 and first_height >= 52 and second_height >52:
            print("Youth Riders permitted. Have fun you two!")
        else:
            print("Rider Not permitted. Requires an Adult.")
    else:
        if first_age >= 18 and first_height >= 62:
            print("Rider permitted. Have a nice day!")
        elif first_age < 18 or first_height <= 62 and first_height >= 36:
            print("Rider Not Permitted. Requires an Adult.")
        else:
            print("ERROR")
            # print("rider too short to ride. Come back next year!")