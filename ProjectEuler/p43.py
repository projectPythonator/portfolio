import time
from itertools import permutations as perm

test_primes = [2, 3, 5, 7, 11, 13, 17]




def sol1():
  nums = [''.join(i) for i in perm('0123456789', 10) if i[0] != '0']
  ans = 0
  for num in nums:
    t_nums = [int(num[i:i+3]) for i in range(1, 8)]
    works = True
    for i in range(7):
      if t_nums[i]%test_primes[i] != 0:
        works = False
        break
    if works:
      ans += int(num)
  print('the file of words contians {} amount of tri nums'.format(ans))
  


def main():
  a = time.clock()
  sol1()
  b = time.clock()
  print('time taken is {:f}'.format(b-a))

main()
