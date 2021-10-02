from random import random

def run_regional_election(chance_A_wins):
    if random() < chance_A_wins:
        return "A"
    else:
        return "B"

def run_election(regional_chances):
    
    number_regions_won_by_A = 0
    number_regions_won_by_B = 0

    for chance_A_wins in regional_chances:
        if run_regional_election(chance_A_wins) == "A":
            number_regions_won_by_A += 1
        else: 
            number_regions_won_by_B += 1
    
    if number_regions_won_by_A > number_regions_won_by_B:
        return "A"
    else:
        return "B"

numbers_of_trials = 10000

numbers_A_wins = 0
numbers_B_wins = 0

changes_win_by_regions = [0.87,0.65,0.17]
for trials in range(numbers_of_trials):
    if run_election(changes_win_by_regions) == "A":
        numbers_A_wins += 1
    else:
        numbers_B_wins += 1

print(f'Probability A wins is {numbers_A_wins/numbers_of_trials}')
print(f'Probability B wins is {numbers_B_wins/numbers_of_trials}')

