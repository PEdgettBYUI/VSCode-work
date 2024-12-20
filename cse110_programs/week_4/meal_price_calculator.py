# Meal price calculator v2
# updated for week 4's Final Requirements

#Input Initial values
# Number of people and Cost broken up into Adult and Child categories
print("Welcome to the Mealizer900,\n")
kids_meal = float(input("What's the price of a Kids Meal? $"))
adults_meal = float(input("What price is an Adult's Meal? $"))
kids_num = int(input("How many children are there? "))
adults_num = int(input("How many adults are there? "))
group_num = kids_num + adults_num
app_cost = 0
desert_cost = 0

#"Creativity" section
# "Smart"-prompts if everyone will have an appetizer, some, or no one
apps = input("\nWill everyone have appetizers? ('all'/'some'/press ENTER to skip)? ").strip().lower()
if apps == "all":
    app_cost = float(input("Cost of the appetizers: $"))
    app_cost = app_cost * group_num
elif apps == "some":
    app_cost = float(input("Cost of the appetizers: $"))
    app_num = int(input("How many will be having appetizers? "))
    app_cost = app_cost * app_num

desert = input("\nWill everyone have desert? ('all'/'some'/press ENTER to skip)? ").strip().lower()
if desert == "all":
    desert_cost = float(input("Cost of the Desert: $"))
    desert_cost = desert_cost * group_num
elif desert == "some":
    desert_num = int(input("How many will be having desert? "))
    desert_cost = float(input("Cost of the Desert: $"))
    desert_cost = desert_cost * desert_num

sales_tax_rate = float(input("What is the sales tax rate (%)? "))

# Calculating subtotals
kids_subtotal = kids_meal * kids_num
adults_subtotal = adults_meal * adults_num
meal_subtotal = kids_subtotal + adults_subtotal + app_cost + desert_cost
st_value = meal_subtotal * sales_tax_rate/100
total = meal_subtotal + st_value

# Results
# # Original rounding using the round() function
# print(f"\nSubtotal: ${round(meal_subtotal, 2)}")
# print(f"Sales Tax: ${round(st_value, 2)}")
# print(f"Total: ${round(total, 2)}\n")

# Rounded using :.#f
# : indicates that you are about to format it
# . indicates precision rounded to
# f indicates "fixed point" notation; note: e is used for exponent notation
print(f"\nSubtotal: ${meal_subtotal:.2f}")
print(f"Sales Tax: ${st_value:.2f}")
print(f"Total: ${total:.2f}\n")

# Estimating change
payment = float(input("What is the payment amount? $"))
print(f"Change: ${payment - total:.2f}")
# Closing Message
print("\n----------------------------")
print("Thank you for using the Mealizer900, \nWe hope you have a great day, and enjoy your meal!\n")