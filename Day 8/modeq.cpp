// GitHub ID: @Shantanugupta1118
// Day 8 of 100
// Modular Equation   -  codechef/MAY21



#include<iostream>
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main() {
	ll t;
	cin>>t;
	while(t--)	{
		long long N,M,count=0;
		cin>>N>>M;
		vector<long long> mod(N+1,1);
		for(ll a=2;a<=N;a++)		{
			ll x=M%a;
			count+=mod[x];
			for(long long b=x;b<=N;b+=a)			{
				mod[b]++;
			}
		}
		cout<<count<<endl;
	}
	return 0;
}