/*
kattis transitwoes problem
Author: Agis Daniels
Solve to check if our route allows us to arrive on time
NOTE 
*/

#include <bits/stdc++.h>

using namespace std;

#define LOC_MAX_N 20

int main()
{
    //declare variables
    int s=0,t=0,n=0;
    int coms[LOC_MAX_N], tims[LOC_MAX_N], arvs[LOC_MAX_N];
    
    //init arrays 
    memset(coms, 0, sizeof coms);
    memset(tims, 0, sizeof tims);
    memset(arvs, 0, sizeof arvs);
    
    //read in inputs 
    cin>>s>>t>>n;
    for(int i=0; i<=n; ++i) cin>>coms[i];
    for(int i=0; i<n; ++i) cin>>tims[i];
    for(int i=0; i<n; ++i) cin>>arvs[i];
    
    //solve
    for(int i=0; i<n; ++i){
        int tmp=arvs[i];
        s+=coms[i];
        s+=(((tmp-(s%tmp))%tmp)+(tims[i]));
    }
    
    //print answer
    string ans=(s+coms[n-1]<=t)? "yes": "no";
    cout<<ans<<endl;
    return 0;
}
