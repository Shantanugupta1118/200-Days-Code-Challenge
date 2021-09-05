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
#define ll long long int 

/*---Main Driver---*/
int main() {
    int test_case; cin>>test_case;
    while(test_case--) {
        // write code here
        ll a,b,c;
        cin>>a>>b>>c;
        ll e=0, f=0;
        while(c>1) {
            if(a%c==0) {
                e++;
                a--;
            } 
            else if(b%c==0) {
                f++;
                b--;
            }
            else {
                c--;
            }
        }
        cout<<e<<" "<<f<<endl;
    }
    return 0;
}

