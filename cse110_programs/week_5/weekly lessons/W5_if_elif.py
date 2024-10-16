# Week 5 - Decisions with if and elif

# Putting .lower() up here will change the variable at the input
# If you want to preserve casing for later use, use .lower() at the calculation point
do_it = input("Should I do it? ")
really = input("Really, are you sure? ").lower()

# Indentation matters, but the following is acceptable
# This is not good practice
#Indentation that's off by even one space will throw an error
if do_it.lower() == "yes": # Forgetting the () at this stage will have it compare the method itself to a string; difficult to debug
    print("I did it!")


    #This is a comment


    print("I also did this")
elif do_it == "no":
    print("Ok, I won't do it.")
    # # You can nest an input, but it will only exist from the point where it's defined onward (Scope)
    # really = input("Really, are you sure? ").lower()
elif really == "yes":
    # You can use \ to tell python that ' or " is part of a string
    print('Ok, if you\'re sure...') 
    print("Ok, if you're sure...")
else:
    print("Make up your mind!")
print("done")
