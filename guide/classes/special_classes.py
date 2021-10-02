class Employee:

    raise_amt = 1.04
    # Dunder is double underscore.

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        # An unambigious representation of the object and should be used for debugging and logging.
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
        pass

    def __str__(self):
        # An readable representation of the object and it meant to be used as a display to the end-user.

        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
            # Combine the pay of 2 employee
        return self.pay + other.pay

    def __len__(self):
    	return len(self.fullname())


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Khoi", "Nguyen", 60000)

# print(emp_1)

# You can access them specifically:
print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(1 + 2)  # In the background, Python use the dunder add method.
print(int.__add__(1, 2))

print(str.__add__("1", "2"))  # String also has its own dunder add method.

# How to use dunder add method:
print(emp_1.pay + emp_2.pay)

# In this function, Python run background the dunder len method.
print(len("test"))
print("test".__len__())


# So we can use the len function to the object.
print(len(emp_1))

