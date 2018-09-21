
from math import sqrt

def largest_prime_factor(in_num):
    ''''''
    last_factor = 0
    if 0 == in_num%2:
        last_factor = 0
        in_num //= 2
        while 0 == in_num%2:
            in_num //= 2
    else:
        last_factor = 1
    max_factor = int(sqrt(in_num))
    factor = 3
    while 1 < in_num and factor <= max_factor:
        if 0 == in_num%factor:
            in_num //= factor
            last_factor = factor
            while 0 == in_num%factor:
                in_num //= factor
            max_factor = int(sqrt(in_num))
        factor += 2
    if 1 == in_num:
        return last_factor
    else:
        return in_num

def main():
    num_to_fact = 600851475143
    lrg_fact = largest_prime_factor(num_to_fact)
    print('largest prime factor of {} is {}.'.format(num_to_fact, lrg_fact))

main()
