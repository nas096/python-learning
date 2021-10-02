import datetime, random
import math
"""
    1.Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
    2. Explore the surprising probabilities of the "Birthday Paradox".
    3. More info at https://en.wikipedia.org/wiki/Birthday_problem
    4. View this code at https://nostarch.com/big-book-small-python-projects
    5. Tags: short, math, simulation"""

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays"""

    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1,1)

        # Get a random day into the year

        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    return birthdays

def getMatch(birthdays):
    """Return the date object of a birthday that occurs more than once in the birthday list"""

    if len(birthdays) == len(set(birthdays)):
        return None
    """When you use enumerate(), the function gives you back two loop variables:

The count of the current iteration
The value of the item at the current iteration"""

    # Compare each birthday to every other birthday
    for indexA, birthdayA in enumerate(birthdays):
        for indexA, birthdayB in enumerate(birthdays[indexA + 1:]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matched birthday

# Display the intro:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
   The Birthday Paradox shows us that in a group of N people, the odds
   that two of them have matching birthdays is surprisingly large.
   This program does a Monte Carlo simulation (that is, repeated random
   simulations) to explore this concept.
  
   (It's not actually a paradox, it's just a surprising result.)
   ''')

# Setup a tuple of month names in order
MONTHS = (('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# Keep asking until the user enters a valid amount
while True:
    print("How many birthdays shall I generate? (max 100)")

    response = input('> ')

    if response.isdecimal() and (0 < int(response) <=100):
        numBDays = int(response)
        break

print()

# Generate and display the birthdays

print("Here are", numBDays, "birthdays:")

birthdays = getBirthdays(numBDays)

for i, birthday in enumerate(birthdays):
    if i != 0:
        
        print(", ", end="")

    monthName = MONTHS[birthday.month -1]

    dateText = f"{monthName} {birthday.day}"

    print(dateText, end="")

print()
print()

# Determine if there are 2 birthdays that match
match = getMatch(birthdays)

# Display the results
print("In this simulation, ", end="")

if match != None:
    monthName = MONTHS[match.month -1]
    dateText = f"{monthName} {match.day}"
    print(f"multiple people have a birthday on", dateText)

else:
    print("There are no matching birthdays")


# Run through 100,000 simulations

print("Generating", numBDays, "random birthdays 100, 000 times ..")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations")

simMatch = 0 
for i in range(100_000):
    # Generate a report every 10_000 simulations
    if i % 10000 == 0:
        print(i, "simulation run ...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

print("100,000 simulation run.")

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')


