str = str()

def popstring():  # populate string
    f = open("p008/unparsednumber.txt", "r")

    lines = f.readlines()
    for line in lines:
        global str
        line = line.replace("\n", "")
        str += line
    return str


popstring()

intlist = list(map(int, str))

greatest = 0

for x in range(0, len(intlist) - 13):  # -13 to pad end of list
    sum = intlist[x]
    for i in range(x, x + 12):  # start at x, +12 till the end
        sum *= intlist[i]

    if greatest < sum:
        greatest = sum
print(greatest)
