//author aghis daniels
//Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#include <iostream> //cout

using namespace std;

//int rec_sum(int n)
//recursive version of the function below
//x is the number we will break up and sum
//return the sum
int rec_sum(int n){
	if(1>=n){
		return n*n*n*n*n;
	}else{
		return (n%10)*(n%10)*(n%10)*(n%10)*(n%10)+rec_sum(n/10);
	}
}

//int sum_of_num(int n)
//a traditional number spliting functions powers of 5ths
//x is the number we will break up and sum
//return the sum
int sum_of_num(int n){
	int sum=0;
	while(1<n){
		const int tmp=n%10;
		n/=10;
		sum+=tmp*tmp*tmp*tmp*tmp;
	}
	sum+=n*n*n*n*n;
	return sum;
}

//bool is_num(const int in)
//a helper function
//x is the number we will break up and sum
//return true is in == sum of digit fifths
bool is_num(const int in){
	return (in==sum_of_num(in));
}

//int solve()
//solving the problem here
int solve(){
	int ans=0;
	for(int i=2; i<250000; ++i){
		if(is_num(i)){
			ans+=i;
		}
	}
	return ans;
}

int main(){
    int total=solve();
    cout<<"the sum of all numbers taht digits are sum of powers of 5 are "<<total<<endl;
    return 0;
}


