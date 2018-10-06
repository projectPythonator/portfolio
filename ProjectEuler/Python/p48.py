import time
from math import sqrt

def helper(lim):
  return str(sum([i**i for i in range(1, lim+1)]))[-10:]

def sol1(lim):
  print('lsat 10 digits of sum of i^i up to {} is {}'.format(lim, helper(lim)))

def main():
  a = time.clock()
  sol1(1000)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))

main()
