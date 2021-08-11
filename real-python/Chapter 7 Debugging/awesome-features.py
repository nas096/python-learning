def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"You are awesome {name}"

my_list = [be_awesome, say_hello]
print(my_list[1]("Bob"))

def greetings(a_greeter):
    return a_greeter('Bob')

print(greetings(say_hello))
print(greetings(be_awesome))