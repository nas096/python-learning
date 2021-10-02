class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self): 
        return self.length * self.width


class square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        # Replace 2 arguments above with the side_length arguments
jim = square(4)
print(jim.area())