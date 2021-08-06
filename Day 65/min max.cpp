// # Github: Shantanugupta1118
// # DAY 65 of DAY 100



#include<iostream>
#include<bits/stdc++.h>
#include<cmath>
#include<string>

using namespace std;

#define itr(s,e,t) for(int i=s; i<e; i=i+t)
#define itr1(s,e,t) for(int i=s; i<=e; i=i+t)
#define rev_itr(s,e,t) for(int i=e; i>s; i=i-t)

int main() {
    #ifndef ONLINE_JUDGE
        freopen("E:/CodeWork/testcase/input.txt", "r", stdin);
        freopen("E:/CodeWork/testcase/output.txt", "w", stdout);
    #endif 
    int test_case; cin>>test_case;
    while(test_case--) {
        int max = INT_MIN, min = INT_MAX;
        int n; cin>>n;
        int arr[n];
        itr(0, n, 1) {
            cin>>arr[i];
        }
        itr(0, n, 1) {
            if(arr[i]>max) {
                max = arr[i];
            }
            else if(arr[i]<min) {
                min = arr[i];
            }
        }
        cout<<"MAX: "<<max<<" "<<"MIN: "<<min<<endl;
    }
    return 0;
}

