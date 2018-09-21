//author agis daniels
//How many such routes are there through a 20×20 grid?
#include <iostream>
#include <vector>
using namespace std;

//cache for ways2 function
long cache[20][20]={{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}};





//long count_ways(int m, int n)
//returns the count from a recursive version
//param m and n which equal to x and y
//return 1 if we hit an edge otherwise sum of both
long count_ways(int m, int n){
	if(n==0||m==0){
		return 1;
	}else{
		return count_ways(m-1, n)+count_ways(m, n-1);
	}
}

//long count_ways2(int m, int n)s
//returns the count from a recursive version by divide and conqur
//param m and n are used for the cache
//return 1 if we hit edge retrun catch pos if already known otherwise calc the spot
long count_ways2(int m, int n){
	if(n==0||m==0){
		return 1;
	}else if(cache[m][n]>0){
		return cache[m][n];
	}
	cache[m][n]=count_ways2(m, n-1)+count_ways2(m-1, n);
	return cache[m][n];
}

//long count_ways3(int m, int n)
//returns the count from a iterative version by divide and conqur
//param m and n are used for the grid cords
//return the answer after doing iteration
long count_ways3(int m, int n){
	//grid for ways3 function
	long grid[21][21]={{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}};
	for(int i=0; i<=m; ++i){
		grid[i][0]=1;
	}
	for(int j=0; j<=n; ++j){
		grid[0][j]=1;
	}
	for(int i=1; i<=m; ++i){
		for(int j=1; j<=n; ++j){
			grid[i][j]=grid[i-1][j]+grid[i][j-1];
		}
	}
	return grid[m][n];
}

//long Combinatorial_sol(int n)
//returns the count using Combinatorial
//param n is the size of the grid
//return the anser
long Combinatorial_sol(int n){
	long result=1;
	for(int i=1; i<=n; ++i){
		result=result*(n+i)/i;
	}
	return result;
}

int main(){
	long x=0, y=0;
	cout<<"please enter x then y."<<endl;
	cin>>x>>y;
	long recAns=count_ways2(x, y);
	cout<<"this is the answer from the recursive function     = "<<recAns<<endl;
	long iterAns=count_ways3(x, y);
	cout<<"this is the answer from the iterative function     = "<<iterAns<<endl;
	long combAns=Combinatorial_sol(x);
	cout<<"this is the answer from the Combinatorial function = "<<combAns<<endl;
	return 0;
}
