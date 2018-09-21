//author agis daniels
//goal is What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#include <iostream> // cin cout 
#include <math.h> // sqrt 

using namespace std;

long gcd(long a, long b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main(){
    long s = 1000;
    long s2 = s/2;
    long mlim = ceil(sqrt(s2))-1;
    for(long m=2; m<=mlim; ++m){
        if(0==(s2%m)){
            long sm=s2/m;
            for(; 0==(sm%2); sm/=2){}
            long k;
            if(1==(m%2)){
                k=m+2;
            }else{
                k=m+1;
            }
            while((k<m+m)&&(k<=sm)){
                if(0==(sm%k)&&(1==gcd(k, m))){
                    long d = s2/(k*m);
                    long n = k-m;
                    long a = d*(m*m-n*n);
                    long b = d*m*n+d*m*n;
                    long c = d*(m*m+n*n);
                    cout << a*c*b <<endl;
                    cout << (a+c+b==s) <<endl;
                    cout << s <<endl;
                    cout << a <<endl;
                    cout << b <<endl;
                    cout << c <<endl;
                }
                 k+=2;
            }
        }
    }
    return 0;
}
