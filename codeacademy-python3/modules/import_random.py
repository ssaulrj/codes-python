<#Let’s take randomness to a whole new level by picking a random number from a list of randomly generated numbers between 1 and 100.
# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]
print(random_list)

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)
