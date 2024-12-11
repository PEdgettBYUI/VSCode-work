# This function works just like "area_of_shapes.py" from week 3
# This reworks that program to use functions
# Patrick T. Edgett
# 12/11/24
import math

shape = ""

def compute_area_square(length):
    area = compute_area_rectangle(length, length)
    return area

def compute_area_rectangle(length, height):
    area = length*height
    return area

def compute_area_circle(radius):
    area = math.pi*radius**2
    return area


def compute_area(shape:str, measure_1:float, measure_2:float = None):
    if measure_2 is None:
        measure_2 = measure_1

    if shape.lower() == "square":
        area = compute_area_rectangle(measure_1, measure_1)
    elif shape.lower() == "circle":
        area = math.pi*measure_1**2
    elif shape.lower() == "rectangle":
        area = compute_area_rectangle(measure_1, measure_2)

    return area


while shape != "quit":
    print()
    shape = str(input("What shape do you want to know the area of? (SQUARE, RECTANGLE, or CIRCLE, or type QUIT to stop): ")).lower()
    
    if shape != "quit":
        measure = float(input("What is the measurement (side OR radius): "))
        if shape == "rectangle":
            measure_2 = float(input("Input the second measurement of the rectangle: "))
        print(f"The area of {shape} is {compute_area(shape, measure, measure_2)}")

    elif shape == "quit":
        print("Ending Program. Have a nice day!")
    else:
        print("Input Invalid. Please use a valid input.")


    # if shape == "square":
    #     side = float(input("What is the side of the square: "))
    #     print(f"The area of the square is {compute_area_square(side)}.")
    # elif shape == "rectangle":
    #     side_r = float(input("What is the length of the rectangle? "))
    #     height = float(input("What is the height of the rectangle? "))
    #     print(f"The area of the rectangle is {compute_area_rectangle(side_r, height)}.")
    # elif shape == "circle":
    #     user_rad = float(input("What is the radius of the circle? "))
    #     print(f"The area of the circle is {compute_area_circle(user_rad)}.")
    # elif shape == "quit":
    #     print("Ending Program. Have a nice day!")
    # else:
    #     print("Input Invalid. Please use a valid input.")