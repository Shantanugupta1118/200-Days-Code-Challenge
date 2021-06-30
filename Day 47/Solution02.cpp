#include<bits/stdc++.h>
#includes<iostream>

using namespace std;

#define ll long long int

vector<int> xx[1001];
vector<pair<ll,vector<ll>>> px;
void dfs(ll st,ll e,ll vis[],vector<ll> rs,ll w);


int main()	{
    ll n,m,t,c,u,v;
    cin>>n>>m>>t>>c;
    while(m--)	{
        cin>>u>>v;
        xx[u].push_back(v);
        xx[v].push_back(u);
    }
    vector<ll> rs;
    ll w = c;
    ll vis[n+1] = {0};
    dfs(1,n,vis,rs,w);
    sort(px.begin(),px.end());
    vector<ll> first_arr[n+1];
    for(int i=0;i<px.size();i++){
        ll nes = px[i].second.size();
        for(auto u : px[i].second){
            first_arr[u].push_back(nes);
        }
    }
    ll second_arr[n+1] = {0};
    second_arr[1] = 1;
    second_arr[n] = 1;
    for(int i=2;i<=n-1;i++)	{
        if(first_arr[i].size() > 0)	{
            ll tm = first_arr[i][0];
            ll up = upper_bound(first_arr[i].begin(),first_arr[i].end(),tm) - first_arr[i].begin();
            second_arr[i] = up;
        }
    }
    for(int i=1;i<=n;i++)
    cout<<second_arr[i]<<" ";
    return 0;
}


void dfs(ll st,ll e,ll vis[],vector<ll> rs,ll w)	{
   rs.push_back(st);
   if(st == e)	{
       px.push_back({w*(rs.size()-1),rs});
       return;
   }
   for(auto u : xx[st])	{	
       if(vis[u] == 0)	{
          vis[st] = 1;
          dfs(u,e,vis,rs,w);
          vis[st] = 0;
       }
   }
}
