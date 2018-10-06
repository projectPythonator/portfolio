from math import sqrt
from math import log10
import time

prime_set = set()
def gen_bit_sieve(lim):
  lim2 = lim // 2
  r = int(sqrt(lim)-1)//2
  bit_sieve = [False]*lim2
  bit_sieve[0] = True
  for i in range(1, r+1):
    if not bit_sieve[i]:
      for j in range(i*(i+1)+i*(i+1), lim2, 2*i+1):
        bit_sieve[j] = True
  return bit_sieve

def gen_sieve(lim):
  bit_sieve = gen_bit_sieve(lim)
  sieve = [2] + [i+i+1 for i in range((lim//2)-1) if not bit_sieve[i]]
  return sieve


def check(a):
  dig = len(str(a))
  num1 = a
  num2 = a
  for i in range(1, dig):
    num1 //= 10
    num2 = a%(10**(dig-i))
    if num1 not in prime_set or num2 not in prime_set:
      return False
  return True
    


def sol1(lim):
  ans = 0
  global prime_set

  sieve =  gen_sieve(lim)
  prime_set = set(sieve)
  ind = 4
  counts = 0
  while counts < 12 and ind < len(sieve):
    if check(sieve[ind]):
      print(sieve[ind])
      ans += sieve[ind]
      counts += 1
    ind += 1
  print('{} is {}, {}'.format(lim, ans, counts))


def main():
  a = time.clock()
  lim = 1000000
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
