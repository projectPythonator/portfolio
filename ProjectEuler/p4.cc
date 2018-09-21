//author agis daniels
//goal is Find the largest palindrome made from the product of two 3-digit numbers..
#include <iostream> // cin cout 

using namespace std;

int reverse(int r_num){
    int reversed=0;
    for (; 0<r_num; r_num/=10){
        reversed=10*reversed+(r_num%10);
    }
    return reversed;
}

bool is_palindrome (int n){
    return (n==reverse(n));
}

int main(){
    int largest = 0;
    for(int a=999; 100<=a; --a){    
        for(int b=999; b>=a; --b){
            int ab=a*b;
            if(largest>(ab)){
                break;
            }
            if(is_palindrome(ab)){
                largest=ab;
            }
        }
    }
    cout << "largest palindrone of three digit multile below 1000 is " << largest << '.' <<  endl;
    return 0;
}
