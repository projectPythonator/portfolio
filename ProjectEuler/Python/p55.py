
import time

def is_pal(a):
  return (a == a[::-1])

def check(a):
  for i in range(50):
    a += int(str(a)[::-1])
    if is_pal(str(a)):
      return False
  return True

def sol1(lim):
  ans = 0
  for i in range(10, lim):
    if check(i):
      ans += 1
  print('number of lynch numbers below {} is {}'.format(lim, ans))

def main():
  lim = 10000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
