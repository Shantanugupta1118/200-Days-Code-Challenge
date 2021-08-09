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


/*---Main Driver---*/
int main() {
    #ifndef ONLINE_JUDGE
        freopen("E:/CodeWork/testcase/input.txt", "r", stdin);
        freopen("E:/CodeWork/testcase/output.txt", "w", stdout);
    #endif 
    int test_case; cin>>test_case;
    while(test_case--) {
        int arr[] = {0,2,1,1,0,0,2,0,1,0,1,2,1,2,1,2,2,2,1,1,1,0,0,0,0,0,2,1,1,0,1,0,2,0,2,1};
        int n = sizeof(arr)/sizeof(arr[0]);
        int low, high, med;
        low = 0, high = n-1, med = 0;
        cout<<"Before Sort: ";
        itr(0, n, 1) {
            cout<<arr[i]<<" ";
        }
        
        while(high>=med) {
            switch (arr[med]) {
            case 0:
                swap(arr[low++], arr[med++]);
                break;
            case 1:
                med++;
                break;

            case 2:
                swap(arr[med], arr[high--]);            
            }
        }
        cout<<endl<<"After Sort: ";
        itr(0, n, 1) {
            cout<<arr[i]<<" ";
        }
    }
}

