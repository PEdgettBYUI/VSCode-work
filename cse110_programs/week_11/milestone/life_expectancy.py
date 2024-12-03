# Life Expectancy Program
# Patrick T. Edgett
# 11/25/2024

max_exp = 0.00
min_exp = 9999999999999.00
# max_le= []
# min_le = []
max_entity = ""
min_entity = ""
max_year = 0
min_year = 0

with open("life-expectancy.csv") as file:
   # Creates header and avoids header-in-loop issue
   header = file.readline()
   for line in file:
        parts = line.split(",")
        entity = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2])
        life_exp = float(parts[3])

        # Highest Life Exp.
        # In order of file header
        # eneity, code, year, life_exp
        if max_exp < life_exp:
            max_year = year
            max_exp = life_exp
            max_entity = entity
            # max_le[0] = entity
            # max_le[1] = code
            # max_le[2] = year
            # max_le[3] = life_exp


        # Lowest Life Exp.
        if min_exp > life_exp:
            min_year = year
            min_exp = life_exp
            min_entity = entity
            # min_le[0] = entity
            # min_le[1] = code
            # min_le[2] = year
            # min_le[3] = life_exp

        # print(f"{entity} {code} {year} {life_exp}")
print()
print(f"The Highest Life Expectancy across all countries is: {max_exp} from {max_entity} in {max_year}")
print(f"The Lowest Life Expectancy across all countries is: {min_exp} from {min_entity} in {min_year}")
