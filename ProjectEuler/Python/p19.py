#author agis daniels
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000



def main():
	amtsuns = 0
	mon_no_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
	mon_leap    = [31,29,31,30,31,30,31,31,30,31,30,31]
	day=1
	count=0
	for year in range(1901,2001):
		if year%4!=0:
			for a in mon_no_leap:
				day+=a
				if day%7==6:
					count+=1
		else:
			for a in mon_leap:
				day+=a
				if day%7==6:
					count+=1
	print(count)

if __name__=='__main__':
	main()
