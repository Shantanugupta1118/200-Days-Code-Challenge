// # Github: Shantanugupta1118
// # DAY 66 of DAY 100

/*--- Header Files---*/
#include<iostream>
#include<bits/stdc++.h>
#include<cmath>
#include<string>

using namespace std;

/*--- Defines ---*/
#define itr(s,e,t) for(int i=s; i<e; i=i+t)
#define itr1(s,e,t) for(int i=s; i<=e; i=i+t)
#define rev_itr(s,e,t) for(int i=e; i>s; i=i-t)

/*
//  Time Complexity - O(n^2) for all BEST, AVG, WORST
void bubble_sort(int arr[], int n) {
    for(int i=0; i<n-1; ++i) {
        for(int j=0; j<n-i-1; ++j) {
            if(arr[j]>arr[j+1]) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}
*/

/*----- Optimizing Best Case-------*/
// Time Complexity - O(n) for Best; O(n^2) - Worst/Avg
void bubble_sort(int arr[], int n) {
    int pass, swapped=1;
    for(pass = n-1; pass>=0 && swapped; pass--) {
        swapped = 0;
        for(int i=0; i<= pass-1; i++) {
            if(arr[i] > arr[i+1]) {
                swap(arr[i], arr[i+1]);
                swapped = 1;
            }
        }
    }
}



// Main Driver
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
        bubble_sort(arr, n);
        itr(0, n, 1) {
            cout<<arr[i]<<" ";
        }
    }
}

