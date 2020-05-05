""" 
kattis primereduction problem
Author: Agis Daniels
Solve the problem asks to factor then sum up the factors
    do this till x is prime 
NOTE can optimize even faster with the following

OPTIMIZE method 1 (code snippit miller rabin exists in this repo)
use faster prime checker like miller rabin deterministic for larger n 
plus a bitset for small primes
PROS faster prime check
CONS complements code and increases space requirements

OPTIMIZE method 2
store previous numbers so you dont need to refactorize
PROS dont need to redo reduce and add for the same number twice
CONS does cost extra space to store previous numbers the reduce add solved

OPTIMIZE 3 (currently exists in this code as genSeive)
precompute primes up to sqrt of the max n
PROS dont need to pass over redundent non-prime numbers
CONS need to hardcode a prime array into the file or need to use a seive to 
generate them at runtime, either way takes more space during runtime
"""
from sys import stdin as rf

primes=[]
ps=set()
def genSeive(n):
    global primes, ps
    pb=[True]*n
    for i in range(4, n, 2):
        pb[i]=False
    for i in range(3, n, 2):
        if pb[i]:
            for j in range(i*i, n, 2*i):
                pb[j]=False
    primes=[2]
    for i in range(3,n,2):
        if pb[i]:
            primes.append(i)
    ps=set(primes)
    
def isPrime(n):
    if n<40000:
        return (n in ps)
    for p in primes:
        if p*p>n:
            return True
        if n%p==0:
            return False
    return True

def reduce_add(n):
    rVal=0
    for p in primes:
        if p*p>n:
            break
        if n%p==0:
            amt=0
            while n%p==0:
                amt+=1
                n//=p
            rVal+=(p*amt)
    if n>1:
        rVal+=n
    return rVal

def main():
    genSeive(40000)
    for line in rf:
        x=int(line)
        if x==4:
            break
        ans=0
        while True:
            ans+=1
            if isPrime(x):
                print("{} {}".format(x, ans))
                break
            x=reduce_add(x)
if __name__=='__main__':
    main()
