from math import factorial
import time

digits = [factorial(i) for i in range(10)]
seen = {}

def digit_fact(n):
  global seen
  if n in seen:
    return seen[n]
  r_ret = 0
  rem = n
  while n > 0:
    r_ret += digits[n%10]
    n //= 10
  seen[rem] = r_ret
  return r_ret

def get_chain_len(n):
  r_set = set()
  r_set.add(n)
  while True:
    n = digit_fact(n)
    if n in r_set:
      return len(r_set)
    r_set.add(n)
  return len(r_set)

def sol1(lim):
  ans = 0
  for i in range(69, lim):
    tmp = get_chain_len(i)
    if tmp == 60:
      ans += 1
  print('number of chains below {} that contian 60 reapeted elms is {}'.format(lim, ans))

def main():
  lim = 1000000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))


main()
