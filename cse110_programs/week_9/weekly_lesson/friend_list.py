# Friend List Program
# The purpose of this program is to ask the user to provide names to a list of friends, ending with the comman word "end" while excluding it from the list
# 11/12/24

friend_list = []
name = ""

while name != "end":
    name = input("Type the name of a friend: ")
    if name != "end":
        friend_list.append(name)
print("Your Friends are: ")
for items in friend_list:
    print(f" - {items.title()}")
print()