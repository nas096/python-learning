import random
import operator


def random_problem():
    operators = {
        # '+': operator.add,
        # '-': operator.sub,
        # 'x': operator.mul,
        ':': operator.truediv
    }

    operation = random.choice(list(operators.keys()))
    num1 = random.randint(1000, 9999)
    num2 = random.randint(1000, 9999)

    if operation == '-':
        num2 = random.randint(num1, 9999)

    if operation == ':':
        multiplier = random.randint(1, 20)
        num1 = num2 * multiplier

    answer = (operators.get(operation)(num1, num2))
    print(f'What is {num1} {operation} {num2}')
    return answer


def ask_question():
    answer = random_problem()
    while True:
        try:
            guess = int(input('Answer: '))
        except ValueError:
            print('Not an integer please try again')
            continue
        else:
            return guess == answer


score = 0
print('How well do you know math? \n')
for i in range(5):
    if ask_question() == True:
        score += 1
        print('Correct')
    else:
        print('Incorrect')
print('Your score:', score)
