from math import sqrt
from math import gcd
import time

def sol1(lim):
  d = ''.join(list(map(str,range(1, lim+1))))
  prod = 1
  for i in range(7):
    prod *= int(d[10**i-1])
  print('answer is {}'.format(prod))


def main():
  lim = 1000000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))

main()
