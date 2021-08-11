nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# This is a regular way
my_list = []
for n in nums:
  my_list.append(n)
print(my_list)


# This is the comprehensions way.
print([n for n in nums])


# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n * n)
print(my_list)

# This is the comprehensions way.
my_list = [n * n for n in nums]
print(my_list)

# Using a map + lambda
# This is not easily readable esp for beginners.
my_list = map(lambda n: n * n, nums)
print(list(my_list))


# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
  if n % 2 == 0:
    my_list.append(n)
print(my_list)

# List comprehensions way
print([n for n in nums if n % 2 == 0])

# Using a filter + lambda
# filter only runs the list through its function and only gives us the values that are True
my_list = filter(lambda n: n % 2 == 0, nums)
print(list(my_list))

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
  for num in range(4):
    # This is a tuble in pair.
    my_list.append((letter, num))
print(my_list)

# The comprehensions way
my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list)

## Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# Zip function creates a list of tuples that match each element.
print(list(zip(names, heros)))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

# Dictionary comprehensions
# You can even exclude a element, too
my_dict= {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict)
# If name not equal to Peter


## Set Comprehensions
# A set is a list of unique value.
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# Set comprehension way
my_set = {n for n in nums}
print(my_set)


## Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_func(nums):
    for n in nums:
        yield n*n

# my_gen = gen_func(nums)
# Generator comprehensions
my_gen = (n*n for n in nums) 

for i in my_gen:
    print(i)
