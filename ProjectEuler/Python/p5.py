
from math import sqrt
from math import log

def sol2():
    pri = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    k = 20
    n = 1
    check = True
    limit = int(sqrt(k))
    a = []
    i = 1
    while pri[i-1] <= k:
        a.append(1)
        if check:
            if pri[i-1] <= limit:
                a[i-1] = int(log(k)/log(pri[i-1]))
            else:
                check = False
        n *= pri[i-1] ** a[i-1]
        i += 1
    print('smallest number div by number 1-20 is {}.'.format(n))

def main():
    sol2()


main()
