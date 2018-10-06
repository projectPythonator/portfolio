
import time
from itertools import permutations as perm

g_lim = 5000
pent_nums = [(3*i*i-i)//2 for i in range(g_lim)]
pent_nums_set = set(pent_nums)

def sol1():
  D = 1000000000000
  for i in range(1, g_lim):
    ii = pent_nums[i]
    for j in range(i+1, g_lim):
      if (ii+pent_nums[j]) in pent_nums_set and pent_nums[j]-ii in pent_nums_set:
        if pent_nums[j]-ii<D:
          D = pent_nums[j]-ii
          print(i,j,ii,pent_nums[j])
  print('ans to p 43 is {}'.format(D))
  


def main():
  a = time.clock()
  sol1()
  b = time.clock()
  print('time taken is {:f}'.format(b-a))

main()
