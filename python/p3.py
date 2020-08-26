primes = [2]
prime = True
number = 600851475143

if number % 2 != 0:  # function makes it even so we can keep is as a int
    number += 1
    number /= 2  # we know anything past half of it doesn't matter

for i in range(3, int(number), 2):  # increment by 2 to make it 2x faster
    for j in range(len(primes)):
        if i % primes[j] == 0:
            prime = False

    if prime:
        print(i)
        primes.append(i)
    prime = True
