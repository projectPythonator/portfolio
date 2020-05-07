/*
kattis hissingmicrophone problem
Author: Agis Daniels
Solve given a line of input check if ss in in that string 
NOTE  
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
    string s;
    cin>>s;
    if(s.find("ss")!=string::npos){
        cout<<"hiss"<<endl;
    }else{
        cout<<"no hiss"<<endl;
    }
    return 0;
}
