# Meal price calculator
# to be used in Week 3 & 4

#Input Initial values
# Number of people and Cost broken up into Adult and Child categories
print("Welcome to the Mealizer900,")
kids_meal = float(input("What's the price of a Kids Meal? $"))
adults_meal = float(input("What price is an Adult's Meal? $"))
kids_num = int(input("How many children are there? "))
adults_num = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate (%)? "))

# Calculating subtotals
kids_subtotal = kids_meal * kids_num
adults_subtotal = adults_meal * adults_num
meal_subtotal = kids_subtotal + adults_subtotal
st_value = meal_subtotal * sales_tax_rate/100
total = meal_subtotal + st_value

# Results
print(f"\nSubtotal: ${round(meal_subtotal, 2)}")
print(f"Sales Tax: ${round(st_value, 2)}")
print(f"Total: ${round(total, 2)}\n")

# Estimating change
payment = float(input("What is the payment amount? $"))
print(f"Change: ${round(payment - total, 2)}")
# Closing Message
print("\n----------------------------")
print("Thank you for using the Mealizer900, \nwe hope you have a great day, and enjoy your meal!\n")