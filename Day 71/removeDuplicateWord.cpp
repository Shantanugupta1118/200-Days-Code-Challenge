//# Github: Shantanugupta1118
//# DAY 71 of DAY 100
// Remove Duplicate Words - Daffodil:: Unthinkable Solutions Hiring
// HackerEarth - 10 Aug 2021



/*
    Handling Cases (String might be case sensetive)
    using Hashmap approach to find the duplicate and remove it
*/


/*--- Header Files---*/
#include<iostream>
#include<bits/stdc++.h>
#include<cmath>
#include<string>
#include<cstdio>

using namespace std;

/*---Defines ---*/
#define itr(s,e,t) for(int i=s; i<e; i=i+t)
#define itr1(s,e,t) for(int i=s; i<=e; i=i+t)
#define rev_itr(s,e,t) for(int i=e; i>s; i=i-t)


void removeDuplicateWord(string str)    {
    for(int i=1; i<str.length(); i++) {
        str[i] = tolower(str[i]);
    }
    istringstream ss(str);
    unordered_set<string> hashmap_str;
    // transform(ss.begin(),ss.end(), ss.begin(), ::tolower);

    do {
        string word;
        ss >> word;
        while (hashmap_str.find(word) == hashmap_str.end()) {
            cout << word << " ";
            hashmap_str.insert(word);
        }
    } while (ss);
    cout<<endl;
}


/*---Main Driver---*/
int main() {
    #ifndef ONLINE_JUDGE
        freopen("E:/CodeWork/testcase/input.txt", "r", stdin);
        freopen("E:/CodeWork/testcase/output.txt", "w", stdout);
    #endif 
    int test_case; cin>>test_case;
    while(test_case>0) {
        string s;
        // scanf("%[^\n]s", s);
        getline(cin, s);
        removeDuplicateWord(s);
        test_case--;
    }
    return 0;
}

