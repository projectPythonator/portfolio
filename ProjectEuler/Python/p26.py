#author agis daniels
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from decimal import *
	
def var_one():
    getcontext().prec=2100
    x=[str(Decimal(1)/Decimal(i)) for i in range(1,1001)]
    y=[len(x[i]) for i in range(1000)]
    best=0
    bestnum=0
    for i in range(len(x)):
        if(y[i]>20):
            same=True
            mid=100
            while same:
                if(x[i][100:100+mid]==x[i][100+mid:100+mid+mid]):
                    same=False
                else:
                    mid+=1
            if(mid>best):
                best=mid
                bestnum=i
    print(bestnum+1)

def main():
    var_one()

if __name__=='__main__':
    main()
