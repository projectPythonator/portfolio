//author agis daniels
//What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

#include <iostream> //cout

using namespace std;

//get_sum()
//simple simulation of going around in spiral for collecting the sum
int get_sum1(){
	int sum =0;
    int step=2;
    const int end=1001*1001;
    for(int i=1; i<end; step+=2){
        sum+=i; i+=step;
        sum+=i; i+=step;
        sum+=i; i+=step;
        sum+=i; i+=step;
    }
	return sum+end;
}

//get_sum2()
//use eqations
int get_sum2(){
	int sum=1; 
	for(int i=2, b=2, x=3; i<=501; ++i, b+=2) { 
		sum+=(x+x+x+x)+(b+b+b+b+b+b); 
		x+=(b+b+b+b)+2; 
	}
	return sum;
}

int main(){
    int ans1=get_sum1();
    cout<<"the sum of the diagonals is "<<ans1<<endl;
    int ans2=get_sum2();
    cout<<"the sum of the diagonals is "<<ans2<<endl;
    return 0;
}
