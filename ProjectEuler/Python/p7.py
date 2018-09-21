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
  nth = 4
  ans = 0
  i   = 11
  while nth <= lim-1:
    if is_prime(i):
      nth += 1
    i += 2
  ans = i - 2
  print('the {}th prime is {}.'.format(lim, ans))


def main():
  limit = 10001
  sol1(10001)
main()
