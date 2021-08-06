toppali = 0


def pali(x, y): # making sure its a palindrome
    pro = x * y
    pros = list(map(int, str(pro)))
    if len(pros) % 2 == 0:  # make sure it can be a pali
        mid = int(len(pros) / 2)  # biases to the left
        valid = 0
        for j in range(mid):
            if pros[j] == pros[(len(pros) - 1) - j]:
                valid += 1
            else:
                break;  # saves resources
        if valid == mid:
            return True
        else:
            return False


for x in range(100, 999, 1):
    for y in range(100, 999, 1):
        if pali(x, y):
            pro = x * y  # product
            if toppali < pro:
                toppali = pro
                print(toppali)
