# Split a list of names and ages into seperate components
# Use it to identify which person is the youngest
# Patrick T. Edgett
# 12/4/24

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Micheal 2",
    "Jacob 10"
]

young_man = 99999999999999999999
young_name = ""

for item in people:
    print(item)
    print()

    line = item.split()
    name = line[0]
    age = int(line[1])

    if age < young_man:
        young_man = age
        young_name = name

print(f"The Youngest is '{young_name}' at '{young_man}'.")
