class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"
    
    def drive(self, miles):
        self.mileage = self.mileage + miles

blue_car = Car("Blue", 0)
blue_car.drive(100)
print(blue_car.mileage)


    



