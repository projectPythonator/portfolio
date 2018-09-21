//author agis daniels
//how many different ways can you sum up coins to 2 pounds
#include <iostream>//for cout cin

using namespace std;

const int coins[8]={1,2,5,10,20,50,100,200};

int memo[200][8];

int way[201];


//void fill_memo
//function for filling the memo array
void fill_memo(){
	for(int a=0; a<200; ++a){
		for(int b=0; b<8; ++b){
			memo[a][b]=0;
		}
	}
}

//void fill_way
//function for filling the way array
void fill_way(){
	for(int a=0; a<201; ++a){
		way[a]=1;
	}
}

//int ways(int targ, const int avc)
//		recursivly sums the problem
//	param targ our targeted amount
//	param avc our lvl in the problem
//	return results
int ways(int targ, const int avc){
	if(avc<=1){
		return 1;
	}
	int res=0;
	while(targ>=0){
		res+=ways(targ, avc-1);
		targ-=coins[avc-1];
	}
	return res;
}

//memo_ways(int targ, const int avc)
//		here we use d and c
//	param targ : used for targeted amount
//	param avc used for our current level
//	return result
int memo_ways(int targ, const int avc){
	if(avc<=1){
		return 1;
	}
	int t=targ;
	if(memo[t][avc-1]>0){
		return memo[t][avc-1];
	}
	int res=0;
	while(targ>=0){
		res+=memo_ways(targ, avc-1);
		targ-=coins[avc-1];
	}
	memo[t][avc-1]=res;
	return res;
}

//basic
//		helper most simple
//	return our answer
int basic(){
	int amount=200;
	return ways(amount, 8);
}

//basic
//		helper using our memo version
//	return our answer
int memo_ver(){
	int amount=200;
	fill_memo();
	return memo_ways(amount, 8);
}

//basic
//		retrun the amount using a combintoral method
//	return our answer
int best_ver(){
	int amount=200;
	fill_way();
	for(int i=1; i<8; ++i){
		const int c=coins[i];
		for(int j=c; j<=amount; ++j){
			way[j]+=way[j-c];
		}
	}
	return way[amount];
}

int main(){
	int ans1=basic();
	cout<<"The ways to sum up the coin from doing basic method "<<ans1<<endl;
	int ans2=memo_ver();
	cout<<"The ways to sum up the coin from doing memo method  "<<ans2<<endl;
	int ans3=best_ver();
	cout<<"The ways to sum up the coin from doing memo method  "<<ans3<<endl;
    return 0;
}

