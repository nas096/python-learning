class Employee:
	# Class variables are variables that share among the instances of the class.
	num_of_emps = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay): # This function runs everytim we create an instance of Employee.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f"{first}.{last}@company.com"

		Employee.num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) # You add self to the raise_amount so you can have the ability to change the pay specifically.



emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Khoi", "Nguyen", 30000)

# print(emp_1.__dict__)

Employee.raise_amount = 1.04

# You can specific the class variable for each instance
emp_1.raise_amount = 1.05
emp_2.raise_amount = 1.06

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(Employee.num_of_emps)