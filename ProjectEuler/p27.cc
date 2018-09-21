//autoher agis daniels
//Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0?
#include <algorithm>//binary search
#include <iostream> //cout
#include <math.h>   //sqrt
#include <vector>   //vector

using namespace std;

typedef vector<int> PrimesSet;

typedef vector<bool> PrimesBool;

typedef const int cstInt;

//get_sieve of eratosthenes(const int size)
//sieve of eratosthenes the bool part of it
//param size is the size we would like to cover
//return the seive in a bit set
PrimesBool get_sieve_of_eratosthenes(cstInt size, cstInt size2){
    cstInt r=(sqrt(size)-1)/2;
    PrimesBool seive(size2,0);
    seive[0]=1;
    for(int i=1; i<=r; ++i){
        if(0==seive[i]){
            for(int j=i*(i+1)+i*(i+1); j<size2; j+=(i+i+1)){
                seive[j]=1;
            }
        }
    }
    return seive;
}

//get_sieve(const int size)
//sieve of eratosthenes the vector part
//param size used for the size of the sieve
//return the seive in a vector
PrimesSet get_seive(cstInt size){
    cstInt size2=size/2; 
    PrimesBool seive=get_sieve_of_eratosthenes(size, size2);
    PrimesSet rVec;
    rVec.push_back(2);
    for(int i=0; i<size2; ++i){
        if(0==seive[i]){
            rVec.push_back(i+i+1);
        }
    }
    return rVec;
}

//is_prime(cstInt x, const vector<int> &seive)
//checks if x is prime
//x value to check for prime
//seive prime seive
//return false if x is even otherwise return if x is in seive
bool is_prime(cstInt x, const vector<int> &seive){
	if(x&1){
		return binary_search(seive.begin(), seive.end(), x);
	}
	return false;
}

//count_quad_primes(const vector<int> &seive, cstInt a, cstInt b)
//counts amount of primes generated from a and b
//a is aVal
//b is bval
//seive prime seive
//return amount of primes
int count_quad_primes(const vector<int> &seive, cstInt a, cstInt b){
	for(int n=0; ; ++n){
		if(!is_prime((n*n+n*a+b), seive)){
			return n;
		}
	}
}

//solve()
//solves the problem
//return answer
int solve(){
	PrimesSet seive=get_seive(13100);
	int greatest=0; 
    int product =0;
    for(int b=0; b<168; ++b){
		cstInt bVal=seive[b];
        for(int a=-999; a<1000; ++a){
            cstInt counter=count_quad_primes(seive, a, bVal);
			if(counter>greatest){
				greatest=counter;
				product =a*bVal;
			}
		}
    }
	return product;
}

int main(){
	int ans=solve();
	cout<<"the product of a and b is "<<ans<<endl;
    return 0;
}
