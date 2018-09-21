//author agis daniels
//What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

#include <algorithm> //next_perm
#include <stdio.h>  //printf
#include <string>    //string lib

using namespace std;

//get_answer(string in)
//    gets us the 1000000th perm of the string
//  param sting to operate on
//  return 1000000th perm
string get_answer(string in){
	for(int i=999999; i; --i){
		next_permutation(in.begin(), in.end());
	}
	return in;
}

int main(){
	string ans=get_answer("0123456789");
	printf("the 1000000th permutation of 0123456789 is %s\n",ans.c_str());
	return 0;
}
