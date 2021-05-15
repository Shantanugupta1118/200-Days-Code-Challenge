#include<bits/stdc++.h>


using namespace std;

#define ll long long
#define itr(i, start, end) for(int i = start; i < end; i++)
#define MOD 1000000007
#define mk make_pair
#define uniq(v) (v).erase(unique(all(v)), (v).end())
#define ff first
#define ss second
#define rf(i, start, end) for(int i = start; i >= end; i--)
#define sc(a) scanf("%lld", &a)
#define psf push_front
#define ppf pop_front
#define ppb pop_back
#define pb push_back
#define pq priority_queue
#define all(s) s.begin(),s.end()
#define sp(a) setprecision(a)
#define rz resize
#define ld long double
#define inf (ll)1e18
#define ub upper_bound
#define lb lower_bound
#define bs binary_search
#define eb emplace_back
#define sz(a) (int)(a.size())

const double pi = acos(-1);

ll binpow(ll a, ll b, ll md) {ll res = 1;while(b!=0) {if(b&1)res *= a, res %=md;a *= a, a%=md; b>>=1;}return res%md;}

ll ans;
vector<vector<int>> v;
vector<ll> dp, tot;

void dfs(int curr, int p) {
	dp[curr]=1, tot[curr]=1;
	ll sum = 0, count = 0;
	itr(i, 0, sz(v[curr])) {
		ll node = v[curr][i];
		if(node != p) {
			dfs(node, curr);
			dp[curr] += ((2*dp[node])%MOD), dp[curr]%=MOD, count++, tot[curr]+=tot[node], tot[curr]%=MOD, tot[curr]+= dp[node], tot[curr]%=MOD;
			sum += dp[node];
		}
	}
	itr(i, 0, sz(v[curr])) {
		int node = v[curr][i];
		if(node != p) {
			tot[curr] += (dp[node]*((sum - dp[node] + MOD)%MOD))%MOD;
			tot[curr] %= MOD;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false), cin.tie(NULL);
	int tc;
	cin >> tc;
	itr(i, 1, tc+1) {
		ans = 0; 
		int n;
		cin >> n;
		v.rz(n+1), dp.rz(n+1), tot.rz(n+1);
		itr(i, 0, n-1) {
			int l, r;
			cin>>l>>r;
			v[l].pb(r), v[r].pb(l);
		}
		dfs(1, 1);
		ll ans = tot[1]%MOD;
		cout<<ans<<endl;
		dp.clear(), v.clear(), tot.clear(); 
	}
}