class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# Inheritance allows us to inherit attributes and method from a parent class. We can create subclasses and get all the functionality of all function class and overwrite the function without affecting parent's class.
# And if Python doesn't find anything in the Employee class, it will search over the builtins.object class which is the base class of all Python's classes.

class Developer(Employee):

	raise_amt = 1.10
	# You can overwrite the Employee's variables without having any issues with Employee class.

	def __init__(self, first, last, pay, prog_lang):
    	# You can let the Employee handle first, last, and pay and 
    	# Developer just handles prog_lang:

		super().__init__(first, last, pay) # Pass first, last and pay to the Employee init method.
    	# Employee.__init__(self, first, last, pay) # Another way to do that.
		self.prog_lang = prog_lang

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)
	pass


# If the Developer's __init__ method left empty, Python will search over the Employee class to instantiate the __init__method of that class.

class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []

		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print("--->", emp.fullname())


dev_1= Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Khoi", "Nguyen", 60000, "C++")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
mgr_1.add_emp(dev_2)
print(mgr_1.email)


print(dev_1.prog_lang)

# If an object is an instance of a class
print(isinstance(mgr_1, Employee))

# If an class is an subclass of other
print(issubclass(Manager, Developer))


