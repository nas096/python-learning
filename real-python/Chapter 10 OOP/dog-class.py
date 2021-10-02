class Dog:

    species = 'Canis familiaris'

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    # Instance Method

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
        return f"{self.name}'s coat is {self.coat_color}."


# buddy = Dog('Buddy', 9)
# miles = Dog('Miles', 4)

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}")
