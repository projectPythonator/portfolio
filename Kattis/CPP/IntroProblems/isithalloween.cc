/*
kattis isithalloween problem
Author: Agis Daniels
Solve simply check if its halloween or xmax
NOTE 
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
    string mon;
    int day;
    cin>>mon>>day;
    if(mon=="OCT" && day==31 || mon=="DEC" && day==25){
        cout<<"yup"<<endl;
    }else{
        cout<<"nope"<<endl;
    }
    return 0;
}
