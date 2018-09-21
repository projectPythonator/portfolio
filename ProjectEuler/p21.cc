//author agis daniels
//Evaluate the sum of all the amicable numbers under 10000.
#include <iostream> // cout
#include <math.h>   // sqrt

using namespace std;

//sum_div_one(const int in)
//very basic find sum of divs very slow
//param in is the number to find the divs sum of
//return the sum of the divs
int sum_div_one(const int in){
	int sum=1;
	for(int i=2; i<in-1; ++i){
		if(0==(in%i)){
			sum+=i;
		}
	}
	return sum;
}

//sum_div_two(const int in)
//a improved version of the basic version going only up to the sqrt
//param in is the number to find the divs sum of
//return the sum of the divs
int sum_div_two(const int in){
	if(0==in){
		return 0;
	}
	int sum=1, f=2, step=1;
	int lim=sqrt(in);
	if(lim*lim==in){
		sum+=lim;
		--lim;
	}
	if(0!=(in%2)){
		f=3;
		step=2;
	}
	for(; f<=lim; f+=step){
		if(0==(in%f)){
			sum+=f+(in/f);
		}
	}
	return sum;
}

//sum_div_three(int in)
//using prime factorization we can improve yet again
//param in is the number to find the divs sum of
//return the sum of the divs
int sum_div_three(int in){
	int sum=1, p=2;
	while(p*p<=in && 1<in){
		if(0==(in%p)){
			int j=p*p;
			in/=p;
			while(0==(in%p)){
				j*=p;
				in/=p;
			}
			sum*=(j-1);
			sum/=(p-1);
		}
		if(2==p){
			p=3;
		}else{
			p+=2;
		}
	}
	if(1<in){
		sum*=(in+1);
	}
	return sum;
}

//helper(int in)
//a helper function for the prime fact function above
int helper_three(const int in){
	return sum_div_three(in)-in;
}

//solution_one()
//    a basic solution for the problem
//  param none
//  return answer to our problem
int solution_one(){
	int total=0;
	for(int a=1; a<9999; ++a){
		for(int b=a+1; b<9999; ++b){
		    if(helper_three(b)==a && helper_three(a)==b){
				total+=a+b;
			}
		}
	}
	return total;
}

//solution_two()
//    an imporved version for finding the answer
//  param none
//  return answer to our problem
int solution_two(){
	int total=0;
	for(int a=2; a<9999; ++a){
		const int b=helper_three(a);
	    if(b>a){
		    if(helper_three(b)==a){
				total+=a+b;
			}
		}
	}
	return total;
}


int main(){
	cout<<"the answer from sol one is "<<solution_one()<<endl;
	cout<<"the answer from sol two is "<<solution_two()<<endl;
    return 0;
}
