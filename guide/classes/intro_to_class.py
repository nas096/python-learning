# A class is a blueprint for instance
class Employee:
	def __init__(self, first, last, pay): # This is a constructor function

		self.first = first # It is equal to emp_1.first = "Khoi"
		# You can even change to self.fname = first

		self.last = last # These self. line are written to access the attributes in a instance
		self.pay = pay
		self.email = f"{first}.{last}@company.com"

	def fullname(self): # Each method in a class automatically take instances as first argument and we always call that self. If you don't include this argument, Python will throw an error
		return f"{self.first} {self.last}"



emp_1 = Employee("Corey", "Schafer", 50000) # This is an instance
emp_2 = Employee("Khoi", "Nguyen", 60000)
# Access the attributes of instance
print(emp_1.first)

print(emp_1.fullname()) # You need the parentheses to distinguish between attribute (without ()) and method(with ())
print(emp_2)

# These 2 lines are the same
print(emp_1.fullname()) # If you do this way, you don't need to pass anything.
print(Employee.fullname(emp_1)) # If you do this way, you need to pass an self argument














