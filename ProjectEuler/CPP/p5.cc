//author agis daniels
//goal is What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#include <iostream> // cin cout 
#include <math.h> // sqrt 
#include <vector> // vector

using namespace std;

//long get_number ()
//gets the number that is div by all ints 1-20
//  params ::
//     none
//  return the smallest n div by one to 20 
long get_number (){
    long pri[8] = {2,3,5,7,11,13,17,19};
    long k      = 20     ;
    long n      = 1      ;
    bool check  = true   ;
    long limit  = sqrt(k);
    vector<long> a       ;
    for(int i=1; pri[i-1]<=k; ++i){
        a.push_back(1);
        if(check){
            if(pri[i-1]<=limit){
                a[i-1]=floor(log(k)/log(pri[i-1]));
            }else{
                check=false;
            }
        }
        n*=pow(pri[i-1],a[i-1]);
    }
    return n;
}

int main(){
    long smallest_num=get_number();
    cout << "smallest number div by number 1-20 is " << smallest_num << '.' <<  endl;
    return 0;
}

