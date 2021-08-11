from random import random


    
numbers_A_wins = 0
numbers_B_wins = 0
num_trials = 10000

for trials in range(num_trials):
    regions_A_wins = 0
    regions_B_wins = 0

    if random() < 0.87:
        regions_A_wins += 1
    else: 
        regions_B_wins += 1
        
    if random() < 0.65:
        regions_A_wins += 1
    else:
        regions_B_wins +=1

    if random() < 0.17:
        regions_A_wins += 1
    else:
        regions_B_wins += 1
        
    if regions_A_wins > regions_B_wins:
        numbers_A_wins += 1
    else:
        numbers_B_wins += 1
    


print(f'Probability A wins is {numbers_A_wins/num_trials}')
print(f'Probability B wins is {numbers_B_wins/num_trials}')
