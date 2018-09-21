


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
 

def main():
    sol2(1000)


main()
