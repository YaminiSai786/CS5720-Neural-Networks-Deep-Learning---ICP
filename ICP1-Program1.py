#1. Write a python program for the following: 
# Input the string “Python” as a list of characters from console, delete at least 2 characters, 
# reverse the resultant string and print it. 
#Student Name: Yamini Saraswathi Borra
#Student ID: 700748022

# Input the string "Python" as a list of characters from console
input_string = list(input("Enter a string: "))

# Delete at least 2 characters
if len(input_string) >= 2:
    del input_string[1]
    del input_string[2]

# Reverse the resultant string
result = ''.join(reversed(input_string))

# Print the result
print("Result:", result)

# Take two numbers from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Perform at least 4 arithmetic operations
sum_result = number1 + number2
difference_result = number1 - number2
product_result = number1 * number2
quotient_result = number1 / number2

# Print the results of arithmetic operations
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)