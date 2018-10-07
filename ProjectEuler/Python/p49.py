from math import sqrt
import time

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

def sol1(lim):
  tmp_set = set([1487, 4817, 8147])
  sieve = [i for i in gen_sieve(lim) if len(str(i)) == 4 and i not in tmp_set]
  set_sieve = set(sieve)
  for prime in sieve:
    tmp1 = prime + 3330
    if tmp1 in set_sieve and ''.join(sorted(str(prime))) == ''.join(sorted(str(tmp1))):
      tmp2 = tmp1 + 3330
      if tmp2 in set_sieve and ''.join(sorted(str(tmp2))) == ''.join(sorted(str(tmp1))):
        print('the 12 digit number is {}'.format(str(prime)+str(tmp1)+str(tmp2)))
        break



def main():
  a = time.clock()
  lim = 10000
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
  
