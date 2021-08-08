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


class Solution {
    public:
    void pattern(int arr[], int n) {
        int i, space=0;
        int minimum_range = MIN(arr, n);
        if(minimum_range<0) {
            space = minimum_range;
        }
        for(int i=0; i<n; i++) {
            if(arr[i]<0) {
                std::string spacing = (space-abs(arr[i]))*" ";
                cout<<spacing<<(abs(arr[i])+1)*"*";
            }
            else {
                std::string spacing = space*" ";
                cout<<spacing<<(abs(arr[i])+1)*"*";
            }
            cout<<endl;
        }
    }
    public:
    int MIN(int arr[], int n) {
        int mn=INT_MAX;
        itr(0, n, 1) {
            if(mn>arr[i]) {
                mn = arr[i];
            }
        }
        return mn;
    }
};


/*---Main Driver---*/
int main() {
    #ifndef ONLINE_JUDGE
        freopen("E:/CodeWork/testcase/input.txt", "r", stdin);
        freopen("E:/CodeWork/testcase/output.txt", "w", stdout);
    #endif 
    int test_case; cin>>test_case;
    while(test_case--) {
        int n; cin>>n;
        int arr[n];
        itr(0, n, 1) {
            cin>>arr[i];
        }
        Solution ob;
        ob.pattern(arr, n);
    }
}

