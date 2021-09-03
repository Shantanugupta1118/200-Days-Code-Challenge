//# Github: Shantanugupta1118
//# DAY 75 of DAY 100
// StairCase - Hackerrank

/*--- Header Files---*/
#include<iostream>
#include<bits/stdc++.h>
#include<cmath>
#include<string>

using namespace std;

/*---Defines ---*/
#define itr(s,e,t) for(int i=s; i<e; i=i+t)
#define itr1(s,e,t) for(int i=s; i<=e; i=i+t)
#define rev_itr(s,e,t) for(int i=e; i>s; i=i-t)


void staircase(int a) {
    int i, j, k, l;
    for(i=1;i<a+1;i++) {
        for(k=1;k<=a-i;k++)  {
            cout<<" ";  
        }
        for(l=i;l>0;l--)   {
            cout<<"#";
        }
        cout<<endl;
    }
}


int main() {
    int n; cin>>n;
    staircase(n);
    return 0;
}