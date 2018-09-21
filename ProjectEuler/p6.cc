//author agis daniels
//goal is Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#include <iostream> // cin cout 

using namespace std;

int get_sums(int limit){
	return (limit*(limit+1))/2;
}

int get_sums_sq(int limit){
	return ((limit+limit+1)*(limit+1)*limit)/6;
}

int main(){
    int limit=0;
    cout << "Enter the limit." << endl;
    cin >> limit;
    int sum   =get_sums   (limit);
    int sum_sq=get_sums_sq(limit);
    cout << "The Difference between the first hundred squres of natural numbers is " << sum * sum - sum_sq << '.' <<  endl;
    return 0;
}
