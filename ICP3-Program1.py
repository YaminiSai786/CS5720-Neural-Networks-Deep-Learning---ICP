
# ICP 3 - Program 1
# Program Question1 : 1. Create a class Employee and then do the following
# Create a data member to count the number of Employees 
# Create a constructor to initialize name, family, salary, department 
# Create a function to average salary
# Create a Fulltime Employee class and it should inherit the properties of Employee class 
# Create the instances of Fulltime Employee class and Employee class and call their member functions.

#Student Name : Yamini Saraswathi Borra
#Student ID : 700748022

class Employee:
    # Class variable to count the number of Employees
    employee_count = 0

    def __init__(self, name, family, salary, department):
        # Instance variables
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        # Increment the employee count
        Employee.employee_count += 1

    def display_employee_details(self):
        print(f"Name: {self.name}, Family: {self.family}, Salary: {self.salary}, Department: {self.department}")

    @staticmethod
    def average_salary(employee_list):
        total_salary = sum(emp.salary for emp in employee_list)
        return total_salary / len(employee_list) if len(employee_list) > 0 else 0


class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, hours_worked):
        # Call the constructor of the base class
        super().__init__(name, family, salary, department)
        self.hours_worked = hours_worked

    def display_employee_details(self):
        # Call the display_employee_details method of the base class
        super().display_employee_details()
        print(f"Hours Worked: {self.hours_worked}")

# Create instances of Employee class
employee1 = Employee("Kiran Reddy", "Nare's Family", 50000, "HR")
employee2 = Employee("Jayanth", "Mallu's Family", 60000, "IT")

# Create instances of FulltimeEmployee class
fulltime_employee1 = FulltimeEmployee("Yamini Saraswathi", "Borra's Family", 250000, "Product & Project Management", 40)
fulltime_employee2 = FulltimeEmployee("Siva Koti Reddy", "Borra's Family", 250000, "Share Market & Intraday Trading", 35)

# Display details of all employees
print("Details of Employee Instances:")
employee1.display_employee_details()
employee2.display_employee_details()

print("\nDetails of Fulltime Employee Instances:")
fulltime_employee1.display_employee_details()
fulltime_employee2.display_employee_details()

# Display average salary
employee_list = [employee1, employee2, fulltime_employee1, fulltime_employee2]
avg_salary = Employee.average_salary(employee_list)
print(f"\nAverage Salary: {avg_salary}")
