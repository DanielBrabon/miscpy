# Testing the probability calculations I did regarding 6÷2(1+2)

# I guessed that the probabilities of choosing to write it that way are:
# P("6÷2(1+2)"|9) = 1/20
# P("6÷2(1+2)"|1) = 1/3

# I also assumed that:
# The 9 and 1 cases are equally likely for someone to want to express (priors)
# The total number of expressions someone could want to express doesn't matter

# My calculation then had it that:
# P(9|"6÷2(1+2)") = 3/23 ≈ 0.13043
# P(1|"6÷2(1+2)") = 20/23 ≈ 0.86957
# Expected value is 47/23 ≈ 2.0435
# Should answer 47/23 to minimize error

from random import random
from math import log10

ROUNDS = int(1e6)
TOTAL_EXPRESSIONS = int(2e0)

nines = ones = 0

for _ in range(ROUNDS):
    expression_roll = random() * TOTAL_EXPRESSIONS

    if expression_roll < 1: # If want to communicate the 9 case
        if random() < 1/20:
            nines += 1
    elif expression_roll < 2: # If want to communicate the 1 case
        if random() < 1/3:
            ones += 1

total = nines + ones
digits = int(log10(total)) + 1

print(f"Nines  : {nines:{digits}} (proportion: {(nines / total):.5})")
print(f"Ones   : {ones:{digits}} (proportion: {(ones / total):.5})")
print(f"Average: {((nines * 9) + ones) / total:{digits}.5}")
