
from math import sqrt
from math import log

def sol1(limit):
    sq_sum = sum((i**2 for i in range(1, limit+1)))
    sum_sq = sum((i for i in range(1, limit+1)))**2
    print('The Difference between the first hundred squres of natural numbers is {}'.format(sum_sq - sq_sum))

def sq_sum_eq(limit):
    return (limit * (limit + 1)) // 2

def sums_sq_eq(limit):
    return ((limit + limit + 1) * (limit + 1) * limit) // 6

def sol2(limit):
    sums = sq_sum_eq(limit)
    sum_sq = sums_sq_eq(limit)
    print('The Difference between the first hundred squres of natural numbers is {}'.format(sums ** 2 - sum_sq))

def main():
    limit = 100
    sol1(limit)
    sol2(limit)


main()
