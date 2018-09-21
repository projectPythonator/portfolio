//author agis daniels
//Which starting number, under one million, produces the longest chain?
#include <stdio.h>//output functions
#include <time.h> //for recording the time

typedef unsigned int unInt;

//global
const int max_value = 1000000; //cache size
int count[1000000] = {0};  //cache

int next(int num);

//iter_process(unsigned int num)
//    this function takes care of number that wont be in our cache
//  param in is an unsigned int to modify
//  return the count that is above the max_value plus the count we have stored by 
//  the next
int iter_process(unInt in){
	int counter=0;
	for(; in>=max_value; in>>=1){
	    ++counter;
		if(in&1){ //if odd
			++counter;
			in+=in+in+1;
		}
	}
	return counter+next(in);
}

//int next(int num)
//    this function takes care of both if numbers are in cache or not recursively
//  param num is the current number that we are working with
//  return the count of the number above 1000000(max_value) or return the count
//  of cache number after updating it properly
int next(int num){
	if(num>=max_value){ //not in 'count' cache
		return iter_process(num);
	}
	if(0==count[num-1]){
		if(num&1){ //if odd
			count[num-1]=1+next(num+num+num+1);
		}else{  //even
			count[num-1]=1+next(num/2);
		}
	}
	return count[num-1];
}

//int cache_ver()
//    basically the main program part for the cache version
//  param none
//  return the answer to the question
int cache_ver(){
	int wanted_n, len, max_len=0;
	
	count[0] = 1; //cache for 1
	
	for(int i=1; i<=1000000; i+=2){
		len=next(i);
		if(len>max_len){
			max_len=len;
			wanted_n=i;
		}
	}
	return wanted_n;
}

//const int get_len(int in)
//    this function runs throgh the collatz seq to find its len
//  param in is the number to stat with
//  return the length of the sequence
const int get_len(int in){
    int counter=0;
    for(unInt x=in; x>1; x/=2, ++counter){
        if(x&1){
            x+=x+x+1;
            ++counter;
        }
    }
    return counter;
}

//int non_cache_ver()
//    basically the main program part for the non-cache version takes a bit longer
//    then with the cache
//  param none
//  return the answer to the question
int non_cache_ver(){
    int maxlen=0, maxnum=0;
    for(int col=1; col<=1000000; col+=2){
       const int len=get_len(col);
       if(len>maxlen){
            maxlen=len;
            maxnum=col;
       }
    }
	return maxnum;
}


int main(){
	clock_t begin=clock();
	printf("the answer using cache = %d\n", cache_ver());
	clock_t end=clock();
	double time_spent=(double)(end-begin)/CLOCKS_PER_SEC;
	printf("time_spent for cache = %f\n", time_spent);
	clock_t begin2=clock();
	printf("the answer for no cache = %d\n", non_cache_ver());
	clock_t end2=clock();
	double time_spent2=(double)(end2-begin2)/CLOCKS_PER_SEC;
	printf("time_spent for no cache = %f\n", time_spent2);
	return 0;
}
