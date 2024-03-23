import random as rdm
import math as mat

# Number of balls balls that drop inside
c = 0

# Total number of balls dropped
n = 1000

# Iteration variable
i = 0

# Iterate for the number of balls dropped
for i in range(0, n):
    # Generate random number x,y in[0,1]
    x = rdm.random()
    y = rdm.random()

    # If inside circle there should be an increment
    if mat.sqrt(x ** 2 + y ** 2) <= 1:
        c = c + 1

# inside / total = pi / 4
pi = (4 * c) / n

print('The value of pi at n=1000 is', pi)