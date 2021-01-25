//
//  Dynamic Programming02.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/23.
//
//출력문에 d[n-1]이 둘어가야함
/*
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> v;
int d[100];

int main(){
    cin>>n;
    
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        v.push_back(x);
    }
    
    d[0]=v[0];
    d[1]=max(v[1],d[0]);
    
    for(int i=2; i<n; i++){
        d[i]=max(d[i-1],d[i-2]+v[i]);
    }
    
    cout<<d[n-1]<<" ";
    
    return 0;
}
 */
