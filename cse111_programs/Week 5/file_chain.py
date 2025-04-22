# This Chain-Function Practice program will take a variable number of .txt files 
# and compile them and output them as a new document of a given input name.


# NOTE: this is an in-class example of a chain function that calculates arthmetic
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Error: Division by zero is not allowed."

def chain_arithmetic(first, *args, **kwargs):
    result = first;
    for arg in args:
        print(f"result so far: {result}")
        result = arg(result, 3)
    return result
    
print(chain_arithmetic(10.0, divide, add, multiply, subtract))


# # NOTE: Below is an example of Chain Functions
# def chain_functions(s, func1, func2):
#     intermediate_result = func1(s)
#     final_result = func2(intermediate_result)
#     return final_result

# # Example usage
# to_uppercase = lambda s: s.upper()
# reverse_string = lambda s: s[::-1]

# result = chain_functions("hellomybaby", to_uppercase, reverse_string)
# print(result)  # Output: OLLEH


# Chains Text Files together into one big file
def text_file_chain(*text):
    files = []


    pass