#author aghis daniels
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#digits(x)
#a compact but slower version of summing the powers of fifths
#x is the number we will break up and sum
#return the sum
def digits(x):
	return sum([int(i)**5 for i in str(x)])

#digits2(x)
#a traditional number spliting functions powers of 5ths
#x is the number we will break up and sum
#return the sum
def digits2(x):
	rsum=0
	while 1<x:
		tmp=x%10
		x//=10
		rsum+=tmp*tmp*tmp*tmp*tmp
	rsum+=x*x*x*x*x
	return rsum

#is_num(x)
#helper for comparing x and sum of fifths
#x is the number we will break up and sum
#return true if x = sum of fifths
def is_num(x):
	return(x==digits2(x))

#solve()
#this will run throuigh all the possible solutions
#param none
#return answers 	
def solve():
	return sum([i for i in range(2,200000)if is_num(i)])
	
def main():
	print(solve())

if __name__=='__main__':
    main()
