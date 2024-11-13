# Add numbers to a  list, compute the sum, total, and average, and find the maxiumum/largest number
# 11/13/24

box = []
number = -1
sum = 0
average = 0
largest_num = 0
smol = 9999999999

# Input into the list
while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        box.append(number)
print("exited input")

# Find the Sum
for each in box:
    sum += each
print(f"The sum is: {sum}")

# Find the Average
average = sum / len(box)
print(f"The average is: {average}")

# Find the Max Number
for each in box:
    if each > largest_num:
        largest_num = each
print(f"The largest number is: {largest_num}")

# Find Smallest Positive Number
for each in box:
    if each > 0:
        if each < smol:
            smol = each
print(f"The smallest positive number is: {smol}")

# Sort the list from lowest to largest
sorted_list = sorted(box)
print(sorted_list)