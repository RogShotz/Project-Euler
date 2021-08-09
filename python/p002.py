prev = 1
cur = 2
temp = 0
sum = 0

while cur < 4000000:
    if cur % 2 == 0:
        sum += cur
    temp = cur + prev
    prev = cur
    cur = temp

print(sum)