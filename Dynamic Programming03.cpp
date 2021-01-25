//
//  Dynamic Programming03.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/23.
//
/*
#include <bits/stdc++.h>

using namespace std;

int d[1001];
int n;

int main(){
    cin>>n;
    
    d[1]=1;
    d[2]=3;
    for(int i=3; i<=n; i++){
        d[n]=(d[n-2]*2+d[n-1])%796796;
    }
    
    cout<<d[n]<<" ";

    return 0;
}
 */
