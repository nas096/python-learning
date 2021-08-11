import random
the_total_times = 0
for i in range(10000):
    flipping_sequence = ""
    the_sequence_len = 0

    the_first_flip = random.randint(0, 1)

    if the_first_flip == 0:
        flipping_sequence = flipping_sequence + "1"
    
    else:
        flipping_sequence = flipping_sequence + "1"
    
    while True:
        the_flips = random.randint(0, 1)
        if the_first_flip == the_flips:
            flipping_sequence = flipping_sequence + "3"
            the_sequence_len = len(flipping_sequence)
            break
        else:
            flipping_sequence = flipping_sequence + "1"
            continue
    
    the_total_times = the_total_times + the_sequence_len
print(f"{(the_total_times/10000):.0f}")