S = 4000 # Number of switches
P = 4000 # Number of people
M = 3 # Max factor before looping

switches = [0] * S

for i in [j % M for j in range(P)]: # Equivalent to range(P % (M * 2))
    for n in range(i, S, i + 1):
        switches[n] ^= 1

print(switches)
print(sum(switches))
