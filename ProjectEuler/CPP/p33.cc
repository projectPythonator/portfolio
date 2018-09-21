//author agis daniels
//If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
#include <iostream>

using namespace std;

int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
}

//works
//		checks to see if set is none trival
//	a :: first number
//	b :: second number
//	return true is they arent trival false otherwise
bool works(const int a, const int b){
	int top1, top2, bot1, bot2;
	top1=a/10;
	top2=b/10;
	bot1=a%10;
	bot2=b%10
	if(top1==bot2 && top2==bot1){
		return false;
    }else{
        if(top1==bot2){
            int one=gcd(a, b), two=gcd(top2, bot1);
            if(((a/one)==(top2/two)) && ((b/one)==(bot1/two))){
                return true;
            }else{
                return false;
            }
        }else if(top2==bot1){
            int one=gcd(a, b), two=gcd(top1, bot2);
            if(((a/one)==(top1/two)) && ((b/one)==(bot2/two))){
                return true;
            }
            return false;
        }else{
            return false;
        }      
    }
}



int main(){
    int answers[8]={0,0,0,0,0,0,0,0};
    int pos = 0;
    for(int nu = 11; nu<100; ++nu){
        for(int de=11; de<100; ++de){
            if( nu%10 != 0 && de%10 != 0 && de != nu){
                if(is_cancel(nu, de)){
                    answers[pos]  =nu;
                    answers[pos+1]=de;
                    pos+=2;
                }
            }
        }
    }
    int numer = answers[0]*answers[2]*answers[4]*answers[6];
    int demer = answers[1]*answers[3]*answers[5]*answers[7];
    int div = gcd(numer,demer);
    return 0;

}
