import time

t0 = time.time()
divcap = 20  # how many can it evenly divide up to
# 12, 15 is redundant because higher multiple
check = [11, 13, 14, 16, 17, 18, 19,
         20]  # compile here instead of using range which recompiles to check for array every time
found = False
x = 0

# TODO: implement automatic check populator with math reasoning for similar product multiples
# for x in range(11, divcap):  # 1-10 is redundant
# check.append(x)

while not found:
    x += divcap  # step by divcap because it can't be anything less than that

    if all(x % n == 0 for n in check):  # some pog shit, fors can go after to elaborate on a value
        found = True

t1 = time.time()
totaltime = t1 - t0
print("time: ", totaltime, "solution: ", x)
