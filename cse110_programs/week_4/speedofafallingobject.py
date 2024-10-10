# calculates the speed of a given falling object
# Patrick Edgett
import math

mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_area = float(input("Cross sectional area (in m^2): "))
drag_const = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# calculating "things"
c = 1/2 * density * cross_area * drag_const 
final_velocity = math.sqrt(mass * gravity/c) * (1 - math.exp((-math.sqrt(mass * gravity * c)/mass)* time))

#print result
print(f"\nThe inner value of c is: {c:.3f}")
print(f"The velocity after {time} seconds is: {final_velocity:.3f}m/s\n")