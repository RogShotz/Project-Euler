primes = []
found = False
x = 2
primesplace = 10001  # which primes place you want to search for

while len(primes) < primesplace:
    if all(x % n != 0 for n in primes):
        print(x)  # remove if slow
        primes.append(x)
    x += 1

print(primes[len(primes) - 1])
