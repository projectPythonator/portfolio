/*
kattis tarifa problem
Author: Agis Daniels
Solve a scan as input comes in to get data build up
NOTE 
*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    //declare variables
    int x=0, n=0, ans=0, pi=0;
    
    //read in inputs and solve 
    cin>>x>>n;
    while(n--){
        cin>>pi;
        ans=ans-pi+x;
    }
    
    //print answer
    cout<<ans+x<<endl;
    return 0;
}
