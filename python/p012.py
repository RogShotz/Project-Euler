import math

divisorcap = 500
currdiv = 0  # current amount of divisors

topdiv = 0
x = 0
step = 1
while currdiv < divisorcap:
    x += step
    step += 1
    currdiv = 0
    for y in range(1, round(math.sqrt(x))):  # go until the square root of the number
        if x % y == 0:
            currdiv += 1

    currdiv *= 2  # multiply by two since it was broke early for efficiency
    if x % math.sqrt(x) == 0:  # add +1 if its a square root
        currdiv += 1
    if currdiv > topdiv:
        topdiv = currdiv
        print(
            f'Current Highest divisor: {currdiv:4d}; Number: {x}')  # marks position, useful for longer computations, indicates progress
