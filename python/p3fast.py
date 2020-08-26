num = 600851475143
newnum = num

counter = 2
while counter * counter <= newnum:
    if newnum % counter == 0:
        newnum = newnum / counter
        largestFact = counter
        print(counter)
    elif counter == 2:  # made for incrementing by two
        counter +=1
    else:
        counter += 2
if newnum > largestFact:
    print(newnum)