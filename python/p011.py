td_array = []  # 2d array
adj_numbers = 4


def popstring():  # populate string
    f = open("p11/numbergrid.txt", "r")

    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        line = line.split(" ")
        line = list(map(int, line))
        td_array.append(line)


popstring()

greatestprod = 0

# + 1 to some these because of uninclusive ranges

# fully inclusive x range for down searches
for y in range(len(td_array) - adj_numbers + 1):  # y is size of column - how many your searching for (indices max)
    for x in range(len(td_array[y])):  # x will be the size of the row
        product = 1
        for n in range(adj_numbers):
            product *= td_array[x][y + n]

        if greatestprod < product:
            greatestprod = product

# fully inclusive y range for right searches
for y in range(len(td_array)):  # y is size of column - how many your searching for (indices max)
    for x in range(len(td_array[y]) - adj_numbers + 1):  # x will be the size of the row
        product = 1
        for n in range(adj_numbers):
            product *= td_array[x + n][y]

        if greatestprod < product:
            greatestprod = product

# restricted x and y for diagonally down and right searches
for y in range(len(td_array) - adj_numbers + 1):  # y is size of column - how many your searching for (indices max)
    for x in range(len(td_array[y]) - adj_numbers + 1):  # x will be the size of the row
        product = 1
        for n in range(adj_numbers):
            product *= td_array[x + n][y + n]

        if greatestprod < product:
            greatestprod = product

# restricted x and y for reverse diagonal up right
for y in range(adj_numbers - 1, len(td_array)):  # y is size of column - how many your searching for (indices max)
    for x in range(adj_numbers - 1, len(td_array[y]) - adj_numbers + 1):  # x will be the size of the row
        product = 1
        for n in range(adj_numbers):
            product *= td_array[x + n][y - n]
            print(x + n, y - n)

        if greatestprod < product:
            greatestprod = product

print(greatestprod)
