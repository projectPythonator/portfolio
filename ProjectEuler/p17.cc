//author agis daniels
//If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#include <iostream> // for cout

using namespace std;

//globals for the word lengths
const int ones    [10] = {0,3,3,5,4,4,3,5,5,4};
const int teens   [10] = {3,6,6,8,8,7,7,9,8,8};
const int tens    [10] = {0,3,6,6,5,5,5,7,6,6};
const int hundreds[10] = {0,10,10,12,11,11,10,12,12,11};

//letter_sum(x):
//this function calcs the length of a number in the word form
//param x is the number
//return the len
int letter_sum(const int x){
    int lvl1=x/10;
    if(0==lvl1){
        return ones[x];
    }else if(0==(x/100)){
        if(1==lvl1){
            return teens[x%10];
        }else{
            return tens[lvl1]+ones[x%10];
        }
    }else{
        if(0==(x%100)){
            return hundreds[x/100];
        }else if(1==((x%100)/10)){
            return hundreds[x/100]+3+teens[x%10];
        }else{
            return hundreds[x/100]+3+tens[((x%100)/10)]+ones[x%10];
        }
     }
 }
 
int main(){
    int lettersum=11;
    for(int i=1; i<1000; ++i){
        lettersum+=letter_sum(i);
    }
    cout<<"the sum of all the letters of the words of numbers below 1000 is"<<endl;
    cout<<lettersum<<endl;
    return 0;
}
