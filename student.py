class Student: # tạo ra 1 data type mới

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name # self.name là 1 thuộc tính của class Student
        self.major = major # self.major là actual object, the name of the student major equals to the name that we passed in
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def on_honor_roll(self): # cách tạo class functions
        if self.gpa >= 3.5:
            return True
        else:
            return False
