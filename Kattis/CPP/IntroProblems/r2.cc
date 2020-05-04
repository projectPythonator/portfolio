/*
kattis R2 problem
Author: Agis Daniels
Solves for r2 in mean calc (r1+r2)/2 == s
NOTES
*/
#include <bits/stdc++.h>

using namespace std;

int main (){
    int r=0,s=0;
    cin>>r>>s;
    cout<<((r>s)? s-(r-s): s+(s-r))<<endl;
    return 0;
}
