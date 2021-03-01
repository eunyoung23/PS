//
//  Binary Search03-2.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/22.
//
//cnt에서 0으로 초기화하는 것을 어떻게 할지 고민함.
/*
#include <bits/stdc++.h>

using namespace std;

int n,m;
vector<int> targets;
int arr[1000001];

int main(){
    cin>>n;
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        arr[x]=1;
    }
    
    cin>>m;
    for(int i=0; i<m; i++){
        int target;
        cin>>target;
        targets.push_back(target);
    }
    
    for(int i=0; i<m; i++){
        if(arr[targets[i]]==1){
            cout<<"yes"<<endl;
        }
        else{
            cout<<"no"<<endl;
        }
    }
    return 0;
}
*/
