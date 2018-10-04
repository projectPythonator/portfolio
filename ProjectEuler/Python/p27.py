#study up a bit further for better answer
from math import sqrt

prime_set  = set()
prime_list = []

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

def is_prime(n):
  return (n in prime_set)

def count_quad_primes(a, b):
  n = 0
  while is_prime(n*n+n*a+b):
    n += 1
  return n
 
def sol1(lim):
  global prime_set, prime_list
  prime_list = gen_sieve(lim)
  prime_set  = set(prime_list)
  greatest = 0
  prod = 0
  blim = 168
  abeg = -999
  alim = 1000
  for b in range(blim):
    bVal = prime_list[b]
    for a in range(abeg, alim):
      counter = count_quad_primes(a, bVal)
      if greatest < counter:
        greatest = counter
        prod = a*bVal
  print('the product of a and b is {}'.format(prod))

def main():
  lim = 13100
  sol1(lim)
main()
