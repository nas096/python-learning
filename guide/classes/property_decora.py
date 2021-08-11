# Property decorator allows us to define a method but we can access it like an attributes.
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    # We can also use with fullname

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # You want to change the full name but also the first, last and email attribute, you should use setters
    @fullname.setter
    def fullname(self, name):
    	# Name value is the value we are trying to set
    	first, last = name.split(" ")
    	self.first = first
    	self.last = last	

    @fullname.deleter
    def fullname(self):
    	# You can even delete the full name of the instances!
    	print("Delete Name!")
    	self.first = None
    	self.last = None



emp_1 = Employee("John", "Smith")

# The problem is that if we want to change the first name, the email
# is also changed but with the original method, we can't do that.
# In addition, if we do make email as a method, the customer must
# change the code to work with it well. So we must use @property to
# allow us to define a method but we can access it like an attributes.

emp_1.first = "Jim"

emp_1.fullname = "Khoi Nguyen"


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# With the del function, you can delete the fullname
del emp_1.fullname