#3. Use the if statement conditions to write a program to print the letter grade based 
#on an input class score. Use the grading scheme we are using in this class.
#Student Name : Yamini Saraswathi Borra
#Student ID : 700748022

# Get the class score from the user
class_score = float(input("Enter the class score: "))

# Use if statements to determine the letter grade
if class_score >= 90:
    grade = 'A'
elif class_score >= 80:
    grade = 'B'
elif class_score >= 70:
    grade = 'C'
elif class_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the letter grade
print("Letter Grade:", grade)