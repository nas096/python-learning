import random
def roll():
    average = 0
    for i in range(10_000):
        rolling = random.randint(1,6)
        average = average + rolling
    return f"{(average / 10_000):.2f}"
print(roll())