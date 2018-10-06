
import time

def is_pal(a):
  return (a == a[::-1])

def sol1(lim):
  ans = 0
  for i in range(1, lim, 2):
    if is_pal(str(i)) and is_pal("{0:b}".format(i)):
      ans += i
  print('the sum of base 10 and 2 palindrome numbers below {} is {}'.format(lim, ans))


def main():
  a = time.clock()
  lim = 1000000
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
