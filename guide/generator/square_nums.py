# This function return a list.
# def square_numbers(nums):
# 	result = []
# 	for i in nums:
# 		result.append(i*i)
# 	return result


# Generator has the advantages of performance. Instead of returning all data, it just return a part of data for me to work with.
# def square_numbers(nums):
	# Generator don't hold entire results in memory. It yield a result at a time.
    # for i in nums:
    #     yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])

# You can use comprehension.
my_nums = (x*x for x in [1,2,3,4,5]) 


print((my_nums)) # [1, 4, 9, 16, 25]
# Return generator object

# If you use list, you won't have the advantage of performance.
print(list(my_nums))

# To print out the element in the generator. 
# Each time you print(next(my_nums)), it will return a value in my_nums
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# You can use for loop for a generator
for num in my_nums:
    print(num)