import time
from math import sqrt

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

prime_list = []
prime_set = set()

def factor_primes(n):
  r_set = []
  last_fact = 0
  for prime in prime_list:
    if prime*prime > n or 1 >= n:
      break
    if 0 == n%prime:
      n //= prime
      last_fact = prime
      tmp = prime
      while 0 == n%prime:
        n //= prime
        tmp *= prime
      r_set.append(tmp)
  if 1 == n:
    if r_set[-1]%last_fact == 0:
      r_set[-1] *= last_fact
    else:
      r_set.append(last_fact)
  else:
    if r_set[-1]%n == 0:
      r_set[-1] *= n
    else:
      r_set.append(n)
  return r_set

def sol1(lim):
  global prime_list, prime_set
  prime_list = gen_sieve(lim)
  prime_set = set(prime_list)
  i = 647
  while True:
    tmp1 = [j for j in range(i, i+4) if j in prime_set]
    if len(tmp1) == 0:
      set1 = factor_primes(i)
      if len(set1) == 4:
        set2 = factor_primes(i+1)
        if len(set2) == 4:
          set3 = factor_primes(i+2)
          if len(set3) == 4:
            set4 = factor_primes(i+3)
            if len(set4) == 4:              
              tmp = set(set1+set2+set3+set4)
              if len(tmp) == 16:
                print('first four consecutive integers to have four distinct prime factors each is {}'.format(i))
                break
            else:
              i=i+4
          else:
            i=i+3
        else:
          i=i+2
      else:
        i+=1
    else:
      i= tmp1[-1]+1

def main():
  a = time.clock()
  sol1(1000000)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))

main()
