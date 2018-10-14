from math import gcd
import time

def left_most_bin(d, n, t):
  l = 0
  r = n
  while l < r:
    m = int((l+r)/2)
    if (m / d) > t:
      r = m
    else:
      l = m + 1 
  return l - 1


def sol1(lim):
  targ = 3/7
  closest = 0
  ans= 0
  for d in range(1, lim):
    n = left_most_bin(d, d//2, targ)
    while gcd(n, d) != 1:
      n -= 1
    if closest < n/d < targ:
      closest = n/d
      ans = n
  print('proper fraction left of 3/7  is {}'.format(ans))


def main():
  lim = 1000000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
