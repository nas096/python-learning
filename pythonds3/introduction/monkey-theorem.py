# A function generates a string that is 28 characters long by choosing random letters from the 26 letter in the alphabet

import secrets


def stringGenerator():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " "]

    generatedString = [secrets.choice(alphabets) for i in range(28)]

    return "".join(generatedString)
# A function scores each generated strings and compared the strings to the goal.


def scoreString():
    goal = "methinks it is like a weasel"

    generation = stringGenerator()
    score = 0
    for index, char in enumerate(goal):
        if goal[index] == generation[index]:
            score += 1

    return score, generation


# Repeatedly call and generate
# This should print out the best string generated so far and its score every 1000 tries


def simulation():
    simulationDict = {}
    for i in range(10000):
        theString = scoreString()
        simulationDict[theString[0]] = theString[1]

    bestString = max(simulationDict)
    return simulationDict, simulationDict[bestString]


print(simulation())
