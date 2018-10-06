import time
from itertools import permutations as perm


def sol1(lim):
  pent_nums_set = set([(3*i*i-i)//2 for i in range(lim)])
  hexa_nums_set = set([2*n*n-n for n in range(lim)])
  for i in range(286, lim):
    tri = (i*i+i)//2
    if tri in pent_nums_set and tri in hexa_nums_set:
      print('next tri pent hex num is {}'.format(tri))
      break


def main():
  a = time.clock()
  sol1(100000)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))

main()
