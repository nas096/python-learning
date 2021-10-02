import random
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

random_state = random.choice(list(capitals_dict.keys()))

answer = capitals_dict[random_state]
while True:
    user_input = input(f"Enter a the capital of {random_state}: ")
    if user_input.lower() == "exit":
        print(f'The capital of {random_state} is {answer}')
        print("Goodbye")
        break
    if user_input.lower() == answer.lower():
        print("Correct")
        break