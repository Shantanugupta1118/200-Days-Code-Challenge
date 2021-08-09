//# Github: Shantanugupta1118
//# DAY 70 of DAY 100
//Codechef Division2 - 01


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


/*---Main Driver---*/
int main() {
    #ifndef ONLINE_JUDGE
        freopen("E:/CodeWork/testcase/input.txt", "r", stdin);
        freopen("E:/CodeWork/testcase/output.txt", "w", stdout);
    #endif 
    int test_case; cin>>test_case;
    while(test_case--) {
        int a1, a2, a3, b1, b2, b3;
        cin>>a1>>a2>>a3>>b1>>b2>>b3;
        if((a1+a2+a3)>(b1+b2+b3)) {
            print(1);
        }
        else {
            print(2);
        }
    }
    return 0;
}

