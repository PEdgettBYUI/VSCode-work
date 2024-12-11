# The purpose of this program is to calculate the wind chill of a given temperature
# The program will accept both farenheit and celcius, converting celcius into farenheit
# Patrick T. Edgett
# 12/11/24

# # Prototype for creating the same response regardless of what the input is.
# # AKA, the All in One Function - Probably a bad idea???
# def find_wind_chill_upto(temp, measure, velocity):
#     #NOTE: range([Start], [Stop @, EXCLUDING], [i++ = X])
#     for i in range(5, velocity, 5):
#         chill_rounded = "{:.2f}".format(wind_chill(temp, i))
#         print(f"At Temperature {temp}{measure}, and with a windspeed of {i}mph, the windchill is: {chill_rounded}F")


def c_to_f(temp):
    farenheit = temp*(9/5)+32
    farenheit = round(farenheit, 2)
    return farenheit

def wind_chill(temp, wind_speed):
    chill = 35.74 + (0.6215 * temp) - (35.75*(wind_speed**(0.16)))+ (0.4275 * temp * (wind_speed ** (0.16)))
    return chill

def display_windchill(temp):
    #NOTE: range([Start], [Stop @, EXCLUDING], [i++ = X])
    for i in range(5, 61, 5):
        chill_rounded = "{:.2f}".format(wind_chill(temp,i))
        print(f"At Temperature {temp}F, and with a windspeed of {i}mph, the windchill is: {chill_rounded}F")
 

f_or_c = ""

temp = float(input("What is the Temperature Outside? "))


while f_or_c != 'f' and f_or_c != 'c':
    f_or_c = input("Farenheit or Celsius (F/C)? ")
# Display wind chill at given temp 5mph - 60mph wind chill
    if f_or_c.lower() == 'f':
        display_windchill(temp)
# Convert to Farenheit then Display 5mph - 60mph wind chill
    elif f_or_c.lower() == "c":
        temp = c_to_f(temp)
        display_windchill(temp)
    else:
        print(f"{f_or_c} is not a valid answer.")
print()