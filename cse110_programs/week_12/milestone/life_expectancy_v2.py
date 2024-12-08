# Life Expectancy Program
# Patrick T. Edgett
# 11/25/2024

max_exp = 0.00
min_exp = 9999999999999.00

max_entity = ""
min_entity = ""
max_year = 0
min_year = 0

user_max_exp = 0.00
user_min_exp = 9999999999999999.00
user_max_entity = ""
user_min_entity = ""
user_highest_exp_drop = 0.00

user_country = ""
user_year = 0

# country_exp_sum = 0.00
# count = 0

with open("life-expectancy.csv") as file:
    # Creates header and avoids header-in-loop issue
    header = file.readline()
   
    user_year = int(input("Which Year Would you Like to Focus on? "))
    # user_country = input("Which country? ").title()


    for line in file:
        parts = line.split(",")
        country = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2])
        life_exp = float(parts[3])

        # Highest Life Exp. overall
        # In order of file header
        # eneity, code, year, life_exp
        if max_exp < life_exp:
            max_year = year
            max_exp = life_exp
            max_entity = country
        # Lowest Life Exp. overall
        if min_exp > life_exp:
            min_year = year
            min_exp = life_exp
            min_entity = country

        
        # Highest Life Exp. in user's given year
        if user_max_exp < life_exp and year == user_year:
            user_max_exp = life_exp
            user_max_entity = country
        # Lowest life expectancy in a user's given year
        if user_min_exp > life_exp and year == user_year:
            user_min_exp = life_exp
            user_min_entity = country

        # # User given Country Average Life Expectancy
        # if country == user_country:
        #     country_exp_sum += life_exp
        #     count += 1
        #     if max_exp < life_exp:
        #         max_year = year
        #         max_exp = life_exp
        #         max_entity = country
        #     # Lowest Life Exp. overall
        #     if min_exp > life_exp:
        #         min_year = year
        #         min_exp = life_exp
        #         min_entity = country




        # print(f"{entity} {code} {year} {life_exp}")
print()
print(f"The Highest Life Expectancy across all countries is: {max_exp} from {max_entity} in {max_year}")
print(f"The Lowest Life Expectancy across all countries is: {min_exp} from {min_entity} in {min_year}")
print()
print(f"For the year {user_year}:")
print(f"The Highest life expectancy was in {user_max_entity} with {user_max_exp}")
print(f"The Lowest life expectancy was in {user_min_entity} with {user_min_exp}")