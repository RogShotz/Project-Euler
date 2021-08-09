cap = 101
natsum = 0
squaresum = 0

for x in range(cap):
    natsum = natsum + x ** 2
    squaresum = squaresum + x

squaresum = squaresum ** 2

print(squaresum-natsum)