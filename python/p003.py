cap = 600851475143
primes = []

for y in range(2, cap + 1):  # construct check, only needs primes
    print(y)
    if all(y % n != 0 for n in primes):
        primes.append(y)

print(primes[len(primes-1)])
