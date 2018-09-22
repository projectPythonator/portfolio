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

def sol1(lim):
  t = a = 1
  cnt = 0
  tt = 0
  expo = 0
  sieve = gen_sieve(65500)
  while cnt <= lim:
    cnt = 1
    a += 1
    t += a
    tt = t
    for cur_prime in sieve:
      if cur_prime*cur_prime > tt:
        cnt += cnt
        break
      expo = 1
      while 0 == tt%cur_prime:
        expo += 1
        tt //= cur_prime
      if 1 < expo:
        cnt *= expo
      if 1==tt:
        break
  print('the value of the first triangle number to have over {} is {}'.format(lim, t))

def get_tri_num(num):
  return (num*num-num)//2

def sol2(lim):
  '''a studied solution'''
  n = 3
  dn = 2
  cnt = 0
  n1 = dn1 = expo = 0
  sieve = gen_sieve(1000)
  while cnt <= lim:
    n += 1
    n1 = n
    if 0 == n1%2:
      n1//= 2
    dn1 = 1
    for cur_prime in sieve:
      if cur_prime*cur_prime > n1:
        dn1 *= 2
        break
      expo = 1
      while 0 == n1%cur_prime:
        expo += 1
        n1 //= cur_prime
      if 1 < expo:
        dn1 *= expo
      if 1==n1:
        break
    cnt = dn*dn1
    dn = dn1
  print('the value of the first triangle number to have over {} is {}'.format(lim, get_tri_num(n))) 


def main():
  sol1(500)
  sol2(500)
main()
