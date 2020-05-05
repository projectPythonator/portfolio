/*
kattis qaly problem
Author: Agis Daniels
Solve summation of quality[i]*years[i]
NOTES
*/
#include <bits/stdc++.h>

using namespace std;

int main (){
    int n=0;
    double q,y,ans=0;
    cin>>n;
    while(n--){
        cin>>q>>y;
        ans+=q*y;
    }   
    cout<<fixed;
    cout<<setprecision(3);
    cout<<ans<<endl;
    return 0;
}
