# Calculates the grades in a given class
# Patrick T. Edgett
# 10/16/24

grade = float(input("Input your grade %"))

letter = "F"
plus_minus = ""
last_whole_digit = grade % 10
print(last_whole_digit)

# Determine letter grade.
if grade > 90:
    letter = "A"
elif grade > 80:
    letter = "B"
elif grade > 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade < 60:
    letter = "F"

# Determine Plus or Minus
if grade <97.0 and grade >60.0:
    if last_whole_digit >= 7:
        plus_minus = "+"
    elif last_whole_digit <= 3:
        plus_minus = "-"
    else:
        plus_minus = ""
else:
    plus_minus =""

# Print final grade
print(f"\nYour final grade is {letter}{plus_minus}")

# Did the user Pass?
if grade >= 70:
    print("You passed!\n")
else:
    print("You failed. Try again next time.\n")