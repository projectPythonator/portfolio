//author agis daniels
//goal is By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#include <stdio.h> // cin cout 


//int get_fib_sum_rec(int end_goal,int cur, int last){
//  to run throgh the fib sequence up to endgoal 
//  and sum up the even terms
//  params::
//      end_goal :: the size of the sequence we will use
//      cur :: the cur fib num
//      last :: the last fib num
//  return the sum of the even fib numbers
long get_fib_sum_rec(long end_goal, long cur, long last){
	if(cur >= end_goal){
		return 0;
	}
	else{
		if(cur%2 == 0){
			return cur+get_fib_sum_rec(end_goal, cur+last, cur);
		}else{
			return get_fib_sum_rec(end_goal, cur+last, cur);
		}
	}
}


//int get_fib_sum_iter(int end_goal){
//  to run throgh the fib sequence up to endgoal 
//  and sum up the even terms
//  params::
//      end_goal :: the size of the sequence we will use
//  return the sum of the even fib numbers
void get_fib_sum_iter(long end_goal){
	//setting the varriables up to start the fib seq
	long fib1 = 0, sum_fib = 0;
	for(long fib2 = 1; fib2<end_goal; ){
		int tmp = fib1;
		fib1    = fib2;
		fib2   += tmp ;
		if(fib2%2==0){
			sum_fib+=fib2;
        	}
	}
	printf("The sum of the even fib numbers is %lld\n", sum_fib);
}

long get_fib_sum_iter_faster(int end_goal){
	long fib3 = 2;
	long fib6 = 0;
	long result = 2;
	long summed = 0;
 
	while (result < end_goal) {
    		summed += result;
    		result = 4*fib3 + fib6;
    		fib6 = fib3;
    		fib3 = result;
	}
	printf("The sum of the even fib numbers is %lld\n", result);
}


int main(){
	long up_lim = 4000000;
	get_fib_sum_iter        (up_lim);
	get_fib_sum_iter_faster (up_lim);
	printf("The sum of the even fib numbers is %lld\n", get_fib_sum_rec(up_lim, 1, 0));
	return 0;
}
