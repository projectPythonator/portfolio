from math import sqrt
import time

p_set = set()
p_list = []

def is_prime(n):
  if n in p_set:
    return True
  for i in p_list:
    if i*i > n:
      return True
    if n%i == 0:
      return False

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
  global p_set, p_list
  bit_sieve = gen_bit_sieve(lim)
  p_list =  [i+i+1 for i in range((lim//2)-1) if not bit_sieve[i]]
  p_set = set(p_list)

def sol1(lim):
  tot = 1
  primes = 0
  i = 1
  step = 2
  end = False
  while not end:
    for j in range(4):
      tot += 1
      i += step
      if is_prime(i):
        primes += 1
      if (primes/tot) < .10:
        end = True
        break
    step += 2
  print(primes, tot, i)
  print('len of side that falls below {} % is {}'.format(10, sqrt(i)))

def main():
  lim = 10000000
  a = time.clock()
  gen_sieve(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))



main()
