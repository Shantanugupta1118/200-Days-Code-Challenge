// # Github: Shantanugupta1118
// # DAY 65 of DAY 100

#include<iostream>
#include<bits/stdc++.h>

using namespace std;

#define itr(s, e, t) for(int i=s; i<e; i=i+t)


class Solution {
    public:
    std::vector<int> sortArr(vector<int>arr, int n) {
        void quicksort(vector<int>arr, int low, int high) {
            if(low<high) {
                int pi = partition(arr, low, high);
                quicksort(arr, low, pi-1);
                quicksort(arr, pi+1, high);
            }
        }
        int partition(vector<int>arr, int low, int high) {
            int piv = arr[high];
            int idx = low-1;
            itr(low, high) {
                if(arr[i] < piv) {
                    idx++;
                    swap(arr[idx], arr[i]);
                }
            }
            swap(arr[idx+1], arr[high]);
            return (i+1)
        }
        quicksort(arr, 0, n-1);
        return arr;
    }
};

int main() {

    int tc; cin>>tc;
    while(tc--) {
        int n;
        vector<int>s(n);
        for(int i=0; i<n; i++) {
            cin>>s[i];
        } 
        Solution sol;
        vector<int>v = sol.sortArr(s, n);
        for(auto i:v) {
            cout<<i<<' ';
        }
        cout<<endl;
    }
}

