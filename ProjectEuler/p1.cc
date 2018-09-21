//author agis daniels
//goal is Find the sum of all the multiples of 3 or 5 below 1000.
#include <stdio.h> 

void sol1(int up_lim){
	int tot_sum = 0;
	for(int i = 0; i < up_lim; ++i){
		if( (i%3 == 0) || (i%5 == 0) ){
			tot_sum+=i;
		}
	}
	printf("The sum of numbers below %d is %d.\n", up_lim, tot_sum); 
}

int sol2Helper(int n, int up_lim){
	return 	n*((up_lim-1)/n)*(((up_lim-1)/n)+1)/2;
}

void sol2(int up_lim){
	int threes, fives, fiffteens;
	threes    = sol2Helper(3, up_lim);
	fives     = sol2Helper(5, up_lim);
	fiffteens = sol2Helper(15, up_lim);
	printf("The sum of numbers below %d is %d.\n", up_lim, threes + fives - fiffteens); 
}

int main(){
	int up_lim = 1000;
	sol1(up_lim);
	sol2(up_lim);
	return 0;
}
