from math import gcd

def sol1():
  de = 1
  no = 1
  for i in range(1, 10):
    for denom in range(1, i):
      for nomom in range(1, denom):
        if (nomom*10+i)*denom == nomom*(i*10+denom):
          de *= denom
          no *= nomom
  print('the answer to inccorect correct cancels is  {}'.format(de//gcd(no, de)))

def main():
  sol1()
main()
