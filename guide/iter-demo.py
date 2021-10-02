# A list is iterable but not a iterator.
# An iterable is a thing that is loopable
# If something is iterable, it'll have a special dunder iter method.
nums = [1, 2, 3]
for num in nums:
    print(num)

# Create a list iterator
# i_nums = nums.__iter__() # This is so ugly.
# Iterators are also iterable.
i_nums = iter(nums)
print(i_nums)
print(dir(i_nums))


# you can use next() like an generator.
print(next(i_nums))


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)

print(next(nums))

# Generators are useful to create iterators.


def my_range(start):
    current = start
    while True:
        yield current
        current += 1
        if current == 100:
            break


# Iterator is a object with a state. You can fetch data with the next()
# Iterator will keep getting a value at a time until the end.
# Iterator had the advantages of performance.


class Sentence:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.words = self.string.split()

    def __iter__(self):
        return self

    def __next__(self):
        # This works each time we use next function
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentence = Sentence("This is a test")


def sentence(string):
    string = string.split()
    for i in string:
        yield i


my_sentence = sentence("This is a test")

print(next(my_sentence))
