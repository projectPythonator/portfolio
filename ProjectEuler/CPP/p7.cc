//author agis daniels
//goal is What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#include <iostream> // cin cout 
#include <math.h> // sqrt 

using namespace std;

// this is an optimizied trival prime test method
bool is_prime(int n){
    if (n==1)      return false;
    else if(n<4)   return true;
    else if(n%2==0)return false;
    else if(n<9)   return true;
    else if(n%3==0)return false;
    else{
        int lim=sqrt(n);
        for(int i=5; i<=lim; i+=6){
            if(((n%i)==0) || ((n%(i+2))==0)){
                return false;
            }
        }
        return true;
    }
}

int main(){
    int nthprime=1;
    int answer  =0;
    int i;
    for( i=3; nthprime<=10000; i+=2){
        if(is_prime(i)){
            nthprime++;
        }
    }
    answer = i-2;
    cout << "the 10001th prime is " << answer << '.' <<  endl;
    return 0;
}
