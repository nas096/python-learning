li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# To sort a list in ascending order:
s_li = sorted(li)

# Sort in descending order
s_li = sorted(li, reverse=True)

# s_li = li.sort() # this returns None as you can see
print("Sorted Variable\t",   s_li)

# Sort original list without creating a new variables:
# li.sort()

# One difference between sorted() and sort() that the sorted() function returns a new sorted list and sort() method rearrage the list and returns None
print("Original Variable\t", li)

tup = tuple(li)

# To sort a tuple in ascending order. (Descending order: put a reverse flag)
s_tup = sorted(tup)
print("Tuple\t", s_tup)

di = {"name": "Khoi", "job": "programming", "age": None, "os": "Windows"}
# To return a sorted list of keys in a dictionary:
s_di = sorted(di)
print("Dict\t", s_di)

# To sorted a list of numbers based on the absolute number of it
li = [-6, -5, -4, 1, 2, 3]
# Run each value through abs value before making comparison
s_li = sorted(li, key=abs)
print(s_li)

# If you want compare each Employee in the class, you need to write custom key to sort it.
class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self): # Tell Python how we want this function to represent  when it prints out the screen.
		return f"{self.name},{self.age},${self.salary}"

from operator import attrgetter
e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

employees = [e1, e2, e3]

# This functio returns the employee name.
def e_sort(emp):
	return emp.name

def e_sort_age(emp):
	return emp.age

def e_sort_salary(emp):
	return emp.salary

# Sort ascendingly by the employee's name.
s_employees = sorted(employees, key=e_sort)


# You can pass a lambda function as a key, too.
s_employees = sorted(employees, key=lambda e: e.name)

# You can even import attrgetter as a replacement for key.
s_employees = sorted(employees, key=attrgetter("name"))
print(s_employees)

