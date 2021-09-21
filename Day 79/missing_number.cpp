#include<bits/stdc++.h>
#include<iostream>

using namespace std;

class Solution {
	public: 
	int missing_array(int N, int arr[]) {
		int sum = N*(N+1)/2;
		
		for(int i=0; i<N-1; i++) {
			sum-=arr[i];
		}
		return sum;
	}
};


int main() {
	int tc; cin>>tc;
	while(tc--) {
		int N; cin>>N; 
		int arr[N];
		for(int i=0; i<N-1; i++) {
			cin>>arr[i];
		}
		cout<<Solution().missing_array(N, arr)<<endl;
	}
	return 0;
}
