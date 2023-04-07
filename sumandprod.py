# The Sum and Product Puzzle

# X and Y are two different whole numbers greater than 1
# Their sum is not greater than 100
# S and P are two perfect logicians
# S knows the sum X + Y
# P knows the product X × Y
# Both S and P know all the information in this section

# In the following conversation, both participants are always telling the truth:
# S says "P does not know X and Y."
# P says "Now I know X and Y."
# S says "Now I also know X and Y."

# What are X and Y?

###################################################################################################

# Dictionary of all legal X, Y pairs in the format of {(X, Y): {"sum": X + Y, "product": X * Y}, ...}
all_pairs = {}
for x in range(2, 99):
    for y in range(x + 1, 101 - x):
        all_pairs[(x, y)] = {"sum": x + y, "product": x * y}

nondup_pairs = [] # All legal pairs which do not have the same product as any other legal pair
dup_pairs = [] # All legal pairs which have the same product as at least one other legal pair

# For each legal pair
for pair in all_pairs:
    # Count how many legal pairs have its product
    count = 0
    for pair2 in all_pairs:
        if all_pairs[pair2]["product"] == all_pairs[pair]["product"]:
            count += 1
    
    # If this pair is the only one with that product, add it to nondup_pairs
    if count == 1:
        nondup_pairs.append(pair)
    # Else add it to dup_pairs
    else:
        dup_pairs.append(pair)

# print(len(nondup_pairs)) # 605
# print(len(dup_pairs)) # 1747

# For S to know that P does not know X and Y, 
# the sum of the pair must be a value that is only the sum of legal pairs which have the same product as another legal pair
# In other words: (X, Y) is a pair in dup_pairs whose sum is not the sum of any pair in nondup_pairs

possible_pairs = [] # All pairs meeting this condition
for pair in dup_pairs:    
    count = 0
    for pair2 in nondup_pairs:
        if all_pairs[pair2]["sum"] == all_pairs[pair]["sum"]:
            count += 1
    
    if count == 0:
        possible_pairs.append(pair)

# print(len(possible_pairs)) # 145
# print(possible_pairs)

# For this to tell P which pair it is, (X, Y) must be a pair in possible_pairs whose product is not the product of any other pair in that list

possible_pairs2 = [] # All pairs meeting this condition
for pair in possible_pairs:    
    count = 0
    for pair2 in possible_pairs:
        if all_pairs[pair2]["product"] == all_pairs[pair]["product"]:
            count += 1
    
    if count == 1:
        possible_pairs2.append(pair)

# print(len(possible_pairs2)) # 86
# print(possible_pairs2)

# For this to tell S which pair it is, (X, Y) must be a pair in possible_pairs2 whose sum is not the sum of any other pair in that list

possible_pairs3 = [] # All pairs meeting this condition
for pair in possible_pairs2:    
    count = 0
    for pair2 in possible_pairs2:
        if all_pairs[pair2]["sum"] == all_pairs[pair]["sum"]:
            count += 1
    
    if count == 1:
        possible_pairs3.append(pair)

# print(len(possible_pairs3)) # 1
print(possible_pairs3) # [(4, 13)]

# There is only one pair satisfying all of these conditions: (4, 13)
