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

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int idx = low-1;
    itr(low, high, 1) {
        if(arr[i]<pivot) {
            idx++;
            swap(arr[idx], arr[i]);
        }
    }
    swap(arr[idx+1], arr[high]);
    return idx+1;
}
void quicksort(int arr[], int low, int high) {
    if(low<high) {
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi-1);
        quicksort(arr, pi+1, high);
    }
}




int main() {
    #ifndef ONLINE_JUDGE
        freopen("E:/CodeWork/testcase/input.txt", "r", stdin);
        freopen("E:/CodeWork/testcase/output.txt", "w", stdout);
    #endif 
    int test_case; cin>>test_case;
    while(test_case--) {
        int n, k; cin>>n>>k;
        int arr[n], min[k];
        itr(0, n, 1) {
            cin>>arr[i];
        }
        quicksort(arr, 0, n-1);
        itr(0, n, 1) cout<<arr[i]<<" ";
        cout<<"\n"<<arr[k-1]<<endl;
    }
}

