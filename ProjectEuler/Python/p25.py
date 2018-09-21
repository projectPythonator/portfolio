#author agis daniels
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from math import log10

#fib function to run though and find the value
def Fib(n):
    n-=1
    a, b=1, 1
    x=2
    while log10(a)<n:
        a, b=a+b, a
        x+=1
    return x;

def main():
    ans=Fib(1000)
    print(ans)

if __name__=='__main__':
    main()
