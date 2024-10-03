#Calculate the areas of 3 different shapes
import math

side = float(input("What is the length of a side of the square? "))
print(f"The area of square is: {side**2}\n")

length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the the rectanlge? "))
print(f"The area of the rectangle is: {length*width}\n")
 
radius = float(input("What is the radius of the circle? "))
print(f"The area of the circle is: {3.14*radius**2}\n")


#Stretch Goals
radius = float(input("What is the radius of the circle? "))
print(f"The area of the circle is: {math.pi*radius**2}\n")

# Single input, multiple-calculations
number = float(input("Give us a value to calculate with: "))

# Area of a square
print(f"The area of square is: {number**2}\n")

# Area of a circle
print(f"The area of the circle is: {round(math.pi*number**2, 2)}\n")

# Area of a cube
print(f"The area of a cube is: {6*number**2}\n")

# Area of a sphere
print(f"The area of a sphere is: {round(4*math.pi*number**2, 2)}\n")
print("---------------------------------------------\n")

#Stretch Goal - Convert to Centimeters and Meters squared
side = float(input("What is the length of a side of the square(in cm)? "))
print(f"The area of square is: {(side**2)/10000}cm^2\n")

length = float(input("What is the length of the rectangle(in cm)? "))
width = float(input("What is the width of the the rectanlge? "))
print(f"The area of the rectangle is: {(length*width)/10000}cm^s\n")
 
radius = float(input("What is the radius of the circle(in cm)? "))
print(f"The area of the circle is: {(3.14*radius**2)/10000}cm^2\n")