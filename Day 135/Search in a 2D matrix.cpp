#include<bits/stdc++.h>

using namespace std;

bool findInMat(int x, vector<vector<int>> &arr) {
	for(int i=0; i<arr.size(); i++) {
		for(int j = 0; j<arr.size(); j++) {
			if(x == arr[i][j]) {
				return true;
			}
		}
	}
	return false;
}


int main() {
//	Test Case 1
	int x=4, n=2, m=2;
	vector<vector<int>> arr
	{
		{2,4},{8,12}
	};
	cout<<findInMat(x, arr)<<endl;
	
//	Test Case 2
	x=7, n=3, m=4;
	vector<vector<int>> arr1{
		{1,2,4,5},{8,12,14,16}, {23, 25, 26, 29}
	};
	cout<<findInMat(x, arr1)<<endl;
	return 0;
}


//2
//4 2 2
//2 4
//8 12
//7 3 4
//1 2 4 5
//8 12 14 16
//23 25 26 29