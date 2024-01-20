#1. Write a program that takes two strings from the user: first_name, last_name. 
#Pass these variables to fullname function that should return the (full name). o For example: ▪ First_name = “your first name”, last_name = “your last name” ▪ Full_name = “your full name” 
#Write function named “string_alternative” that returns every other char in the full_name string. 
#Str = “Good evening” Output: Go vnn Note: You need to create a function named “string_alternative” for this program and call it from main function. 
#Student Name: Yamini Saraswathi Borra
#Student ID: 700748022

def fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

def string_alternative(full_name):
    return full_name[::2]

def main():
    # Take user input for first and last names
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Call fullname function
    full_name = fullname(first_name, last_name)

    # Call string_alternative function
    result = string_alternative(full_name)

    # Display the results
    print(f"\nFull Name: {full_name}")
    print(f"Every Other Character: {result}")

# Call the main function
main()