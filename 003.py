import itertools
import operator
import functools

nr = 600851475143
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''for p in primes:
    nr /= p
    print(nr)'''

#print(list(itertools.combinations(primes, 4)))
for i in range(2, len(primes)):
    for combo in itertools.combinations(primes, i):
        if functools.reduce(operator.mul, combo) == nr:
            print(combo)
            break

# https://www.smartickmethod.com/blog/math/operations-and-algebraic-thinking/divisibility/prime-numbers-sieve-eratosthenes/