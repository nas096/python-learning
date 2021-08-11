class animal:
    def __init__(self, pigs, horses, cows):
        self.pigs = pigs
        self.horses= horses
        self.cows = cows

    def count(self):
        return f"This farm has {self.horses} horses, {self.pigs} pigs, and {self.cows} cows"


class pig(animal):
    def __init__(self, walking_time, sleeping_time):
        super().__init__(walking_time, sleeping_time, walking_time)

    def walking(self):
        return f"A pig should walk for 20 minutes per day."

    def sleeping(self):
        return f"A pig sleeps average for 7.8 hours per day."

    def eating(self):
        print("Your pigs are eating.")


class horse(animal):
    def __init__(self, running_distance, sleeping_time):
        super().__init__(running_distance, sleeping_time, running_distance)

    def sleeping(self):
        print("Your horses is sleeping")
        return "A horse sleeps average 2.9 hours per day"

    def running(self):
        return "A horse can travel 25 to 35 miles a day"


class cow(animal):
    def __init__(self, walking_time, sleeping_times):
        super().__init__(walking_time, sleeping_times, walking_time)

    def walking(self):
        return f"A cow walks averange 12,000 steps per day so all your cows has walked {self.cows * 12_000}"

    def sleeping(self):
        print("Your cows are drowsing")
        return f"A female cow sleeps averange for 4 hours so all your cows has slept {self.cows * 4}"


user_pig = int(input("How many pigs does your farm have? "))

user_horse= int(input("How many horses does your farm have? "))


user_cow = int(input("How many cows does your farm have? "))

print(animal(user_pig, user_horse, user_cow).count())
print(cow(14, "21:00").sleeping())
print(pig(14, "22:00").walking())
print(horse(500, "20:00").running())