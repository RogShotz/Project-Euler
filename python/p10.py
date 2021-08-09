import math

cap = 2000000
primes = []
nottofindprimes = []  # not used for finding primes because at mid point

for y in range(2, int(math.ceil(cap / 2))):  # find primes up to midpoint
    if all(y % n != 0 for n in primes):
        primes.append(y)

    if y % 100000 == 0:
        print(y)

for y in range(int(math.ceil(cap / 2)), cap):  # past midpoint, no primes matter for finding new primes
    if all(y % n != 0 for n in primes):
        nottofindprimes.append(y)

    if y % 100000 == 0:
        print(y)

sum = 0
for a in primes:
    sum += a

for a in nottofindprimes:  # add the primes not used for finding primes
    sum += a

print(sum)
