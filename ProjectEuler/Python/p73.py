from math import gcd
import time

def right_most_bin(d, t):
  l = 0
  r = d
  while l < r:
    m = int((l+r)/2)
    if (m / d) < t:
      l = m + 1
    else:
      r = m 
  return l


def left_most_bin(d, t):
  l = 0
  r = d
  while l < r:
    m = int((l+r)/2)
    if (m / d) > t:
      r = m
    else:
      l = m + 1 
  return l - 1

def sol1(lim):
  aa = 1/3
  bb = 1/2
  ans = -2
  for d in range(1, lim+1):
    a = left_most_bin(d, bb)
    b = right_most_bin(d, aa)
    for n in range(b, a+1):
      if gcd(n, d) == 1:
        ans += 1
  print('number of francs between {} and {} under set {} is {}'.format(aa, bb, lim, ans))



def main():
  lim = 12000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
