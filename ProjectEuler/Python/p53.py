import time

def binomialCoefficient(n, k):
    if(k > n - k): 
        k = n - k 
    res = 1
    for i in range(k): 
        res *= (n - i) 
        res //= (i + 1) 
    return res 

def sol1(lim):
  ans = 0
  for i in range(1, lim+1):
    for j in range(1, lim+1):
      if binomialCoefficient(i,j) > 1000000:
        ans+=1
  print(ans)

def main():
  lim = 100
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
  
