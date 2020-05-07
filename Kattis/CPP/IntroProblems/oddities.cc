/*
kattis oddities problem
Author: Agis Daniels
Solve read in n lines and test if each is odd or even
NOTE 
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
    int n,x;
    cin>>n;
    while(n--){
        cin>>x;
        string ans=(x&1)? "odd": "even";
        cout<<x<<" is "<<ans<<endl;
    }
    return 0;
}
