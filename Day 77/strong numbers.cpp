//# Github: Shantanugupta1118
//# DAY 65 of DAY 100


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

bool checkStrong(int n) {
    int x;
    for(x=2;; x++) {
        if(n%x==0) return false; 
        if(x>n) return true;
        n = n-(n/x);
    }
}


/*---Main Driver---*/
int main() { 
    int n; cin>>n;
    if(checkStrong(n)) {
        cout<<"Yes"<<endl;
    }
    else {
        cout<<"No"<<endl;
    }
}

