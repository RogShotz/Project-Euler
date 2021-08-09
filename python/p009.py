import math

pythagTripOf = 1000


def find_pythag_trip():
    for b in range(2, 999):
        for a in range(1, b):  # used to make sure it doesnt pass the range, since it has to be smaller
            c_squared = a ** 2 + b ** 2
            if math.sqrt(c_squared).is_integer():
                if a + b + math.sqrt(c_squared) == pythagTripOf:
                    c = int(math.sqrt(c_squared))
                    print("a value: ", a, "; b value: ", b, "; c value: ", c)
                    print("product = ", a * b * c)
                    return True  # ends once found


if not find_pythag_trip():  # prints if nothing was found
    print("No natural pythagorean triplets found")
