//author agis daniels
//What is the sum of the digits of the number 2^1000?
#include <iostream> //for cout
#include <vector>   //for vector

using namespace std;

int main(){
	const int n=1000;
	int S=0;
	vector<int> vec;
	vec.push_back(1);
	for(int i=1; i<=n; ++i){
		const int size1=vec.size();
		for(int j=0; j<size1; ++j){
			vec[j]+=vec[j];
		}
		for(int j=0; j<size1-1; ++j){
			vec[j+1]+=vec[j]/10;
			vec[j]=vec[j]%10;
		}
		int sTemp=vec.size();
		while(vec[sTemp-1]>=10){
			vec.push_back(vec[sTemp-1]/10);
			vec[sTemp-1]=vec[sTemp-1]%10;
			sTemp=vec.size();
		}
	}
	const int size2=vec.size();
	for(int i=0; i<size2; ++i){
		S+=vec[i];
	}
	cout<<"the sum of 2^1000 is = "<<S<<endl;
}
