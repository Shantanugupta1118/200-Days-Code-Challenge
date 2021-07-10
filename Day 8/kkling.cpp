// GitHub ID: @Shantanugupta1118
// Day 8 of 100
// King Killing   -  codechef/MAY21


#include<bits/stdc++.h>

using namespace std;
#define ll long long
#define MOD 1000000007
int gcd(int a, int b) {
	if(b==0)
		return a;
	return gcd(b, a%b);
}

int32_t main() {
	ofstream fout;
	string line;
	fout.open("sample.txt");

	int sum = 0;
	for(int k=1; k<=1000; k++) {
		for(int i=1; i<=2*k; i++) {
			sum += gcd(k+i*i, k+(i+1)*(i+1));
		}
		sum = sum%MOD;
		cout<<sum<<" ";
	}
	cout<<endl;
	return 0;
}