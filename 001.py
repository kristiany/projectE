below = 1000
print(
    #  [3, 6, 9 ... n]
    sum(range(3, below, 3)) +
    #  [5, 10, 15 ... n]
    sum(range(5, below, 5)) -
    #  Subtract the common divisors that are calculated twice
    #  [15, 30, 45 ... n]
    sum(range(15, below, 15)))
