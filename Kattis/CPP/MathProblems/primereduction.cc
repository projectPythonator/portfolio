/*
kattis primereduction problem
Author: Agis Daniels
Solve the problem asks to factor then sum up the factors
    do this till x is prime 
NOTE can optimize even faster with the following

OPTIMIZE method 1 (code snippit faster than scanf and printf exists in this repo)
faster input scanf or a fast int method in this repo same with printing
(only use on kattis or readup yourself as it can be unsafe for industry)
PROS faster input read 
CONS less readable sometimes

OPTIMIZE method 2 (code snippit miller rabin exists in this repo)
use faster prime checker like miller rabin deterministic for larger n 
plus a bitset for small primes
PROS faster prime check
CONS complements code and increases space requirements

OPTIMIZE method 3
store previous numbers so you dont need to refactorize
PROS dont need to redo reduce and add for the same number twice
CONS does cost extra space to store previous numbers the reduce add solved

OPTIMIZE 4 ((code snippit seive exists in this repo))
precompute primes up to sqrt of the max n
PROS dont need to pass over redundent non-prime numbers
CONS need to hardcode a prime array into the file or need to use a seive to 
generate them at runtime, either way takes more space during runtime
*/

#include <bits/stdc++.h>

using namespace std;

bool isPrime(int n){
    if(n<2) return false;
    if(n<4) return true;
    if((n&1)==0 || n%3==0) return false;
    for(int i=5; i*i<=n; i+=6){
        if(n%i==0 || n%(i+2)==0) return false;
    }
    return true;
}

int reduce_add(int n){
    int rVal=0, p=2;
    while(p*p<=n){
        if(n%p==0){
            int amt=0;
            while(n%p==0){
                amt++;
                n/=p;
            }
            rVal+=(p*amt);
        }
        p++;
    }
    if(n>1) rVal+=n;
    return rVal;
}

int main(){
    int x=0;
    cin>>x;
    while(x!=4){
        int ans=0;
        while(true){
            ans++;
            if(isPrime(x)){
                cout<<x<<' '<<ans<<endl;   
                break;
            }
            x=reduce_add(x);
        }
        cin>>x;
    }
    return 0;
}
