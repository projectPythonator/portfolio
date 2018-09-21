def sol1(up_lim):
    '''loop solution'''
    tot_sum = 0
    generator = (i for i in range(up_lim) if i%3 == 0 or i%5 == 0)
    answer = sum(generator)
    print("The sum of numbers below {} is {}.".format(up_lim, answer))

def sol_2_helper(n, up_lim):
    return n * ((up_lim - 1) // n) * (((up_lim - 1) // n) + 1) // 2

def sol2(up_lim):
    '''algebra solution'''
    threes    = sol_2_helper(3, up_lim)
    fives     = sol_2_helper(5, up_lim)
    fiffteens = sol_2_helper(15, up_lim)
    print("The sum of numbers below {} is {}.".format(up_lim, threes + fives - fiffteens))
    
def main():
    up_lim = 1000
    sol1(up_lim)
    sol2(up_lim)

main()
