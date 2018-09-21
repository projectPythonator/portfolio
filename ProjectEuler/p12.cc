//author agis daniels
//What is the value of the first triangle number to have over five hundred divisors?
#include <iostream> // cin cout
#include <math.h>   // sqrt
#include <vector>   // for the vector

using namespace std;

typedef vector<int> PrimesSet;

typedef vector<bool> PrimesBool;

typedef const int cstInt;

//get_div(const int x)
//get the number of divisors 
//param x is the number i am finding the divisors for
//return the amount of divisors
int get_div(cstInt x){
    int count=0;
    cstInt lim = sqrt(x);
    for(int i =1; i < lim ;i++){
        if(x%i==0){
            count++;
        }
    }
    count+=count;
    return count+1;
}

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
            for(int j=i*(i+1)+i*(i+1); j<size2; j+=(2*i+1)){
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

//get_ans_1(PrimesSet primeSeive)
//sieve of eratosthenes the vector part
//param sPrimesSet primeSeive a seive of primes to use on this problem
//return the seive in a vector
int get_ans_1(){
    int t=1, a=1, cnt=0, tt, expo;
    PrimesSet primeSeive=get_seive(65500); // get our main prime seive
    cstInt seiveSize=primeSeive.size();
    for(; cnt<=500; ){
        cnt=1;
        ++a;
        t+=a;
        tt=t;
        for(int i=0; i<seiveSize; ++i){
            cstInt curPrime=primeSeive[i];
            if(curPrime*curPrime>tt){
                cnt+=cnt;
                break;
            }
            expo=1;
            while(0==(tt%curPrime)){
                ++expo;
                tt/=curPrime;
            }
            if(1<expo){
                cnt*=expo;
            }if(1==tt){
                break;
            }
        }
    }
    return t;
}

//get_tri_num(cstInt num)
//returns the nth triangle number
int get_tri_num(int num){
    return (num*num-num)/2;
}

//get_ans_2(
//more faster version
//none params
//return the ans
int get_ans_2(){
    int n  =3; //starting prime
    int Dn =2; //num div for each prime
    int cnt=0; //to insure loop is entered
    int n1, Dn1, expo;
    PrimesSet primeSeive=get_seive(1000);
    cstInt seiveSize=primeSeive.size();
    for(; cnt<=500; ){
        ++n;
        n1=n;
        if(0==(n1%2)){
            n1/=2;   
        }
        Dn1=1;
        for(int i=0; i<seiveSize; ++i){
            cstInt curPrime=primeSeive[i];
            if(curPrime*curPrime>n1){
                Dn1*=2;
                break;
            }
            expo=1;
            while(0==(n1%curPrime)){
                ++expo;
                n1/=curPrime;
            }
            if(1<expo){
                Dn1*=expo;
            }if(1==n1){
                break;
            }
        }
        cnt=Dn*Dn1;
        Dn=Dn1;
    }
    return get_tri_num(n);
}

int main(){
    cout<<"this is the first function that isnt as fast "<<get_ans_1()<<endl;
    cout<<"this is the second function that is faster "<<get_ans_2()<<endl;
    return 0;
}
