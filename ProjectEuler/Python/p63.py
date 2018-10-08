import time
from math import log10

def count_passed(n):
  res = 0
  base = 2
  leno = int(log10(base**n))+1
  while leno <= n:
    if leno == n:
      res += 1
    base += 1
    leno = int(log10(base**n))+1
  return res

def sol1(lim):
  ans = 0
  for i in range(1, lim):
    ans += count_passed(i)
  print('number of nth digit and nth power numbers is {}'.format(ans))



def main():
  lim = 1000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
