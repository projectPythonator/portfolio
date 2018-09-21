//author agis daniels
//Find the maximum total from top to bottom of the triangle below:
#include <iostream>  // cout
#include <algorithm> // use for max

using namespace std;

//get_sum(int ind,int graph[136],int level)
//recursive solution
//params ind is the current index
//       graph is the graph we are traversing through
//       level is the level of the triangle
//return the greatest sum
int get_sum(int ind,const int graph[136],int level){
    if(graph[ind+level]==0){
        return graph[ind];
    }
    else{
        return graph[ind]+max(get_sum(ind+level,graph,level+1),get_sum(ind+level+1,graph,level+1));
    }
}

//for this function i will input a explination of what happened later
int my_original_way(const int graph[136]){
    //this problem calls me to use tmp arrays
    int setlower[15];
    int setupper[15];
    int settemp [15];
    for(int i=0; i<15; ++i){
        setlower[i]=0;
        setupper[i]=0;
        settemp [i]=0;
    }
    setlower[0]=graph[0]+graph[1];
    setlower[1]=graph[0]+graph[2];
    int z=0, indu=3, upperlvl=3;
    while(graph[indu]!=0){
        z=0;
        for(int i=0; i<upperlvl; ++i){
            setupper[i]=graph[indu+i];
        }
        settemp[0]=setupper[0]+setlower[z];
        for(int i=1; i<upperlvl-1; ++i){
            if(setlower[z]>=setlower[z+1]){
                settemp[i]=setupper[i]+setlower[z];
            }else{
                settemp[i]=setupper[i]+setlower[z+1];
            }
            ++z;
        }
        settemp[upperlvl-1]=setupper[upperlvl-1]+setlower[upperlvl-2];
        for(int i=0; i<upperlvl; ++i){
            setlower[i]=settemp[i];
        }
        indu+=upperlvl;
        ++upperlvl;
    }
    int max=0;
    for(int i=0; i<15; ++i){
        if(setlower[i]>max){
            max=setlower[i];
        }
    }
    return max;
}


int main(){
    const int graph[136] ={75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,19,1,23,75,3,34,88,2,77,73,7,63,67,99,65,4,28,6,16,70,92,41,41,26,56,83,40,80,70,33,41,48,72,33,47,32,37,16,94,29,53,71,44,65,25,43,91,52,97,51,14,70,11,33,28,77,73,17,78,39,68,17,57,91,71,52,38,17,14,91,43,58,50,27,29,48,63,66,4,68,89,53,67,30,73,16,69,87,40,31,4,62,98,27,23,9,70,98,73,93,38,53,60,4,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    int sum  = get_sum(0, graph, 1);
    int sum2 = my_original_way(graph);
    cout<<"this is the answer from the recursive sol "<<sum<<endl;
    cout<<"this is the answer from my own solution   "<<sum2<<endl;
    return 0;
}
