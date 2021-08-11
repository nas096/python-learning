
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

    def fullname(self): # Regular methods automatically takes instances as first argument.
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod # Create a class method
    def set_raise_amount(cls, amount): # Class method takes the class as a first argument.

    	# In this method, you are working with the class instead of the method.
    	# We can use class method to provide multiple ways to create class objects.
    	cls.raise_amt = amount
    	pass

    @classmethod
    def from_string(cls, emp_str):
    	first, last, pay = emp_str.split("-")
    	return cls(first, last, pay)

    @staticmethod
    def is_workday(day): # Retrun whether or not today is a work day or not.
    	if day.weekday() == 5 or day.weekday() == 6:
    		return False
    	return True

    # Static method don't pass anything automatically. They behave like a regular function and we pass it in because it has some logical connection with the class.


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Khoi", "Nguyen", 60000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"


# Create a new class object from the string.
new_emp_1 = Employee.from_string(emp_str_1)

# After all of these, we don't want our customer to use split method. So we want to create a class method.
print(new_emp_1.email)


# Employee.set_raise_amount(1.05) # Set a new raise amount
# It is equal to: Employee.raise_amt = 1.05

# Running the the class method in the instance still change the variable globally
# emp_1.set_raise_amount(1.06)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)


import datetime
my_date = datetime.date(2021,7,11)
print(Employee.is_workday(my_date))