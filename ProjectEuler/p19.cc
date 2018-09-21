//author agis daniels
//How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000
#include <iostream> //for cout

using namespace std;

const int mon_no_leap[12]={31,28,31,30,31,30,31,31,30,31,30,31};
const int mon_leap   [12]={31,29,31,30,31,30,31,31,30,31,30,31};


int main(){
	int day=1, count=0;
	for(int year=1901; year<2001; ++year){
		if(year%4!=0){
			for(int month=0; month<12; ++month){
				day+=mon_no_leap[month];
				if(day%7==6){
					++count;
				}
			}
		}else{
			for(int month=0; month<12; ++month){
				day+=mon_leap[month];
				if(day%7==6){
					++count;
				}
			}
		}
	}
	cout<<"this is the amount of sundays that start of month "<<count<<endl;
	return 0;
}
