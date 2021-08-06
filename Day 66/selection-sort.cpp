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
#define jitr(s,e,t) for(int j=s; j<e; j=j+t)
#define itr1(s,e,t) for(int i=s; i<=e; i=i+t)
#define rev_itr(s,e,t) for(int i=e; i>s; i=i-t)


void swapp(int *a,int *b) {
    int c;
    c = *a;
    *a = *b;
    *b = c;
}

void selection_sort(int arr[], int n) {
    int min, i, j;
    itr(0, n-1, 1) {
        min = i;
        jitr(i+1, n, 1) {
            if(arr[j] < arr[min]) 
                min = j;
        }
        swapp(&arr[min], &arr[i]);
    }
}


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
        selection_sort(arr, n);
        itr(0, n, 1) {
            cout<<arr[i]<<" ";
        }
    }
}

