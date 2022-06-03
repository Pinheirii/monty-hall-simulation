#!/bin/env python3

import numpy as np

def monty_hall(numberExperiments):
    # winner simulates one of three doors containing a prize
    winner = np.random.randint(3, size = numberExperiments)
    # pick simulates the chosen door by the player
    pick = np.random.randint(3, size = numberExperiments)
    # two scenarios, pick is winner or not
    bool_takedWinner = winner == pick
    # all who taked the winner and switch door after one reveal definitiv loose
    number_loose = bool_takedWinner.sum()
    # all who taked any loose and switch door after one reveal definitiv wins
    number_winner = numberExperiments - bool_takedWinner.sum()

    print('number looses %d' % number_loose)
    print('number_winner %d' % number_winner)
    print('winning quote: %f' % (float(number_winner)/float(numberExperiments)))

monty_hall(100000)
