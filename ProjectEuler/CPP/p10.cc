//author agis daniels
//goal is Find the sum of all the primes below two million.?
#include <iostream> // cin cout
#include <math.h> // sqrt
#include <bitset> // for bit set
#include <vector> // for the vector

using namespace std;

//is_prime(int n)
//this is a function that can be used uses trivial division
//param n is the number to check
//return true if prime false otherwise
bool is_prime(int n){
    if(!(n%3)){
        return false;
    }
    int r = sqrt(n);
    for(int f = 5 ; f <= r;f+=6){
        if(n%f==0 || n%(f+2)==0){
            return false;
        }
    }
    return true;
}

//get_sieve of eratosthenes(const int size)
//sieve of eratosthenes the bool part of it
//param size is the size we would like to cover
//return the seive in a bit set
bitset<1000000> get_sieve_of_eratosthenes(const int size){
    bitset<1000000> seive;
    const int size2 = size/2;
    const int r     = (sqrt(size)-1)/2;
    seive.set(0);
    for(int i=1; i<=r; ++i){
        if(0==seive[i]){
            for(int j=i*(i+1)+i*(i+1); j<size2; j+=(2*i+1)){
                seive.set(j);
            }
        }
    }
    return seive;
}

//get_sieve(const int size)
//sieve of eratosthenes the vector part
//param size used for the size of the sieve
//return the seive in a vector
vector<int> get_seive(const int size){
    bitset<1000000> seive = get_sieve_of_eratosthenes(size);
    vector<int> rVec;
    rVec.push_back(2);
    for(int i=999999; i>0; --i){
        if(0==seive[i]){
            rVec.push_back(i+i+1);
        }
    }
    return rVec;
}

int main(){
    vector<int> vec_seive = get_seive(2000000);
    long sum_primes    = 0;
    int prime_set_size = vec_seive.size();
    for(int i = prime_set_size-1 ; i >= 0 ; --i){
        sum_primes += vec_seive[i];
    }
    cout << "sum of first 2000000 is " << sum_primes << '.' <<  endl;
    return 0;
}
