#author agis daniels
#What is the sum of the digits of the number 2^1000?

def main():
	x=2**1000
	print("the sum of digits of 2^1000 is below in three diff ways")
	print(sum([int(i) for i in str(x)]))
	print(sum(map(int, str(x))))
	print(sum(map(int, [x for x in str(x)])))

if __name__=='__main__':
	main()
