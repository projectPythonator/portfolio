

def get_fib_sum_rec(end_goal, cur, last):
    if cur >= end_goal:
        return 0
    else:
        if cur%2 == 0:
            return cur + get_fib_sum_rec(end_goal, cur + last, cur)
        else:
            return get_fib_sum_rec(end_goal, cur + last, cur)


def get_fib_sum_iter(end_goal):
    fib1 = sum_fib = 0
    fib2 = 1
    while fib2 < end_goal:
        tmp  = fib1
        fib1 = fib2
        fib2 += tmp
        if fib2%2 == 0:
            sum_fib += fib2
    print('the sum of he even fib numbers up to {} is {}'.format(end_goal, sum_fib))

def get_fib_sum_iter_faster(end_goal):
    ''' interesting only go over the even numbers solution i found '''
    fib3 = 2
    fib6 = 0
    result = 2
    summed = 0
    while result < end_goal:
        summed += result
        result = 4 * fib3 + fib6
        fib6 = fib3
        fib3 = result
    print('the sum of he even fib numbers up to {} is {}'.format(end_goal, summed))


def main():
    up_lim = 4000000
    get_fib_sum_iter        (up_lim)
    get_fib_sum_iter_faster (up_lim)
    print('the sum of he even fib numbers up to {} is {}'.format(up_lim, get_fib_sum_rec(up_lim, 1, 0)))

main()
