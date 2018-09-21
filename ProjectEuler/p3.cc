//author agis daniels
//goal is What is the largest prime factor of the number 600851475143 ?
#include <iostream> // cin cout 
#include <math.h> // sqrt 

using namespace std;

//long primefact(long in_num){
//  to run throgh the fib sequence up to endgoal 
//  and sum up the even terms
//  params::
//     	in_num the number we will do prime factorizaton on
//  return the sum of the even fib numbers
long primefact(long in_num){
	long last_factor;
	if(0==(in_num%2)){
		last_factor=2;
		in_num/=2;
		for(; 0==(in_num%2); in_num/=2){}
	}else{
		last_factor=1;
	}
	long max_factor=sqrt(in_num);
	for(long factor=3; (1<in_num)&&(factor<=max_factor); factor+=2){
		if(0==(in_num%factor)){
			in_num/=factor;
			last_factor=factor;
			for(; 0==(in_num%factor); in_num/=factor){}
			max_factor=sqrt(in_num);
		}
	}
	if (1==in_num){
		return last_factor;
	}else{
		return in_num;
	}
}

int main(){
	long num_to_fact=0, lrg_fact=0;
	cout << "Enter the number to factorize." << endl;
	cin >> num_to_fact;
	lrg_fact=primefact(num_to_fact);
	cout << "largest prime factor of " << num_to_fact  << " is " << lrg_fact << '.' <<  endl;
	return 0;
}
