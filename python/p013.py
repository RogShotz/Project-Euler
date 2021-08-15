digits = 10  # how many first digits to display


def popnumarr():  # populate number array
    f = open("p013/unparsednumber.txt", "r")

    lines = f.readlines()
    numarr = []
    for line in lines:
        line = line.replace("\n", "")
        numarr.append(line)

    return numarr


sum = 0
for x in popnumarr():  # add the numbers
    sum += int(x)

print("Sum: ", sum)

# not needed but makes for no counting
alldigit = list(str(sum))
tendigit = ""
for x in range(digits):
    tendigit += alldigit[x]

print(f"First {digits} digits: {int(tendigit)}")
