from math import sqrt

def is_prime(n):
  if n == 1:   return False
  if n < 4:    return True
  if 0 == n%2: return False
  if n < 9:    return True
  if 0 == n%3: return False
  lim = int(sqrt(n)+2)
  for i in range(5, lim, 6):
    if 0 == n%i or 0 == n%(i+2):
      return False
  return True

def sol1(lim):
  ans = sum([i for i in range(3, lim, 2) if is_prime(i)])+2
  print('sum of all the primes below {} is {}'.format(lim, ans))

def gen_bit_sieve(lim):
  lim2 = lim // 2
  r = int(sqrt(lim)-1)//2
  bit_sieve = [False]*lim
  for i in range(1, r+1):
    if not bit_sieve[i]:
      for j in range(i*(i+1)+i*(i+1), lim2, 2*i+1):
        bit_sieve[j] = True
  return bit_sieve

def gen_sieve(lim):
  bit_sieve = gen_bit_sieve(lim)
  sieve = [2] + [i+i+1 for i in range((lim//2)-1, 0, -1) if not bit_sieve[i]]
  return sieve

def sol2(lim):
  ''' a refined solution for the trivial version '''
  print('sum of all the primes below {} is {}'.format(lim, sum(gen_sieve(lim))))

def main():
  sol2(2000000)
  sol1(2000000)

main()
 
