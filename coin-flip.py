# Write a program to find out how often a streak of six heads or tails comes up in a randomly generated list of heads and tails
# Part 1: Generate a list of randomly selected "heads" and "tails" values
# Part 2: Check if there is a streak in it
# Put this all in a loop that repeats the experiment 10,000 times to find what percentage of flips contains a streak of 6 in a row

import random
num_of_streaks = 0
for experiment_number in range(1):
    # Code that creates a list of 100 'heads' or 'tails' values.
    test_list = []
    for test in range(100):
        flip = random.randint(0, 1)
        if flip == 0: test_list.append('H')
        else: test_list.append('T')
    

    # Code that checks if there is a streak of 6 heads or tails in a row.

print('Chance of streak: %s%%' % (num_of_streaks / 100))