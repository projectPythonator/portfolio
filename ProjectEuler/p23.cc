//author agis daniels
//Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#include <algorithm> //binary search
#include <iostream> //cout
#include <math.h>   //sqrt
#include <vector>   //vector

using namespace std;

//sum_div_three(int in)
//using prime factorization we can improve yet again
//param in is the number to find the divs sum of
//return the sum of the divs
int sum_div_three(int in){
	int sum=1;
	if(0==(in%2)){
		int j=4;
		in/=2;
		while(0==(in%2)){
			j<<=1;
			in>>=1;
		}
		sum*=(j-1);
	}
	for(int op=3; op*op<=in && 1<in; op+=2){
		if(0==(in%op)){
			int j=op*op;
			in/=op;
			while(0==(in%op)){
				j*=op;
				in/=op;
			}
			sum*=(j-1);
			sum/=(op-1);
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

//get_list()
//    this is to get the list of abundant numbers
//  param none
//  return vector of the list
vector<int> get_list(){
	vector<int> listAbunds(6965,0);
	int ind=0;
	for(int i=12; i<28124; ++i){
		const int tmp=helper_three(i);
		if(tmp>i){
			listAbunds[ind]=i;
			++ind;
		}
	}
	return listAbunds;
}

//get_sum(vector in)
//    this is to get us the sum using the n(nlogn) method with binary search
//  param in a vector full of abundant nymbers
//  return sum as our answer
int get_sum(const vector<int> &in){
	int sum=0;
	const int vSize=in.size();
	for(int i=1; i<28123; ++i){
		bool worked=true;
		for(int x=0; x<vSize; ++x){
			const int tmp=i-in[x];
			if(binary_search(in.begin(), in.end(), tmp)){
				worked=false;
				break;
			}if(tmp<12){
				break;
			}
		}
		if(worked){
			sum+=i;
		}
	}
	return sum;
}

//get_sum2(vector in)
//    this is a different version for testing faster
//  param in a vector full of abundant nymbers
//  return sum as our answer
int get_sum2(const vector<int> &in){
	int sum=0;
	const int vSize=in.size();
	vector<bool> opposite(28123,1);
	for(int a=0; (in[a]+in[a])<28123; ++a){
		const int aVal=in[a];
		int tmp=aVal+aVal;
		for(int b=a+1; tmp<28123; ++b){
			opposite[tmp]=0;
			tmp=aVal+in[b];
		}
	}
	for(int i=0; i<28123; ++i){
		if(opposite[i]){
			sum+=i;
		}
	}
	return sum;
}

int main(){
	vector<int> listAbunds=get_list();
	int answer=get_sum2(listAbunds);
	cout<<"The sum of all the numbers that cant be writen as the sum of two abundant using method of bool vec numbers is: "<<answer<<endl;
	int answer2=get_sum(listAbunds);
	cout<<"The sum of all the numbers that cant be writen as the sum of two abundant using binary scearch numbers is:     "<<answer2<<endl;
    return 0;
}
