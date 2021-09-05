//# Github: Shantanugupta1118
//# DAY 76 of DAY 100


/*--- Header Files---*/
#include<iostream>
#include<bits/stdc++.h>
#include<cmath>
#include<string>

using namespace std;

/*
int maxCuttedSegments(int b[],int n)    {
    int a[n+1][3];
    memset(a,0,sizeof(a));
    int x,y;
    for(int i=1;i<=n;i++)    {
        if(i<b[0])                       
        continue;
        for(int j=0;j<3;j++)  {
            x=0;
            if(i-b[j]>=0)  {
                if(i-b[j]==0)  {
                    x = 1;
                }
                else if(a[i-b[j]][j])   {
                    x = 1 + a[i-b[j]][j];
                }
            }
            y = j>=1 ? a[i][j-1] : 0;
            a[i][j] = max(x,y);
        }
    }
    return a[n][2];
}

// Driver Code 
int main() {
	int t;	cin>>t;
	while(t--)	{
	    int n; cin>>n;
	    int b[3];
	    cin>>b[0]>>b[1]>>b[2];
	    sort(b,b+3);
	    cout<<maxCuttedSegments(b,n)<<endl;
	}
	return 0;
}
*/


int findMaximum(int l, int p, int q, int r) {
	int dp[l + 1];
	memset(dp, -1, sizeof(dp));
	dp[0] = 0;
	for (int i = 0; i <= l; i++) {

		if (dp[i] == -1)
			continue;
		
        if (i + p <= l)
			dp[i + p] = max(dp[i + p], dp[i] + 1);
		
        if (i + q <= l)
			dp[i + q] = max(dp[i + q], dp[i] + 1);
		
        if (i + r <= l)
			dp[i + r] = max(dp[i + r], dp[i] + 1);
	}
	if (dp[l] == -1) {
		dp[l] = 0;
	}
	return dp[l];
}

// Driver Code
int main()  {
	int tc; cin>>tc;
	while(tc--) {
	long long int l, p, q, r;
	cin>>l>>p>>q>>r;
	cout << findMaximum(l, p, q, r);
	return 0;
	}
}
