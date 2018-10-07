import time

def check_num(n):
  base = sorted(str(n))
  for i in range(2, 7):
    if base != sorted(str(n*i)):
      return False
  return True

def sol1(lim):
  for i in range(10, lim):
    if check_num(i):
      print(i)
      return

def main():
  lim = 1000000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
  
