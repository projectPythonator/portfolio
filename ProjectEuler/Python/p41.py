from math import sqrt
from math import log10
import time

prime_set = [set([str(i) for i in range(1, j+1)]) for j in range(9)]
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
  b = set(a)
  return (len(b.intersection(prime_set[len(b)])) == len(a) and '0' not in b)
    


def sol1(lim):
  s = gen_sieve(lim)
  sieve = list(map(str, s))[::-1]
  for i in sieve:
    if check(i):
      print('largest pan prime is {}'.format(i))
      break


def main():
  print(prime_set)
  a = time.clock()
  lim = 10000000
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
