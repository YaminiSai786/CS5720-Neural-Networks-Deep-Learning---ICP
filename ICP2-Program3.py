#3. Write a program, which reads heights (inches.) of customers into a 
#list and convert these heights to centimeters in a separate list using: 
#1) Nested Interactive loop. 2) List comprehensions 

#Student Name : Yamini Saraswathi Borra
#Student ID : 700748022

#Defining a list
heightList = []

#taking input from user for number of customers
noOfCustomers = int(input("Enter number of customers : "))

#for loop to take input and append to list
for i in range(0, noOfCustomers):
    h = float(input())
    heightList.append(h)

#converting inches to cms and appending to a list
newlist = [x*2.54 for x in heightList] 

#printing the new list
print(newlist)