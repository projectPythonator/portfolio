

def is_palindrome(num):
    return (str(num) == str(num)[::-1])


def sol2(limit):
    largest = 0
    a = 999
    lim = 100
    while lim <= a:
        b = 999
        while a <= b:
            ab = a*b
            if ab < largest:
                break
            if is_palindrome(ab):
                largest = ab
            b -= 1
        a -= 1
    print('largest palindrone of three digit multile below {} is {}'.format(limit, largest))
 

def make_palin(fh):
    return int(str(fh) + str(fh)[::-1])

def sol3(limit):
    '''improved version studying from other solutions'''
    found = False
    first_half = 998
    palin = 0
    factors = [0]*2
    while not found:
        first_half -= 1
        palin = make_palin(first_half)
        i = 999
        while i > 99:
            if (palin // i) > 999 or i*i < palin:
                break
            if 0 == palin%i:
                found = True
                factors[0] = palin // i
                factors[1] = i
                break
            i -= 1
    print('largest palin drome of 3 digits is {}'.format(palin))

def main():
    sol3(1000)
    sol2(1000)


main()
