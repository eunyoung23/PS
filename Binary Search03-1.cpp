//
//  Binary Search03.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/22.
//
//타겟이 되는 배열은 정렬할 필요가 없음
/*
#include <bits/stdc++.h>

using namespace std;

int binarySearch(int target,vector<int>arr,int start,int end){
    while(start<=end){
        int mid=(start+end)/2;
        if(target<arr[mid])
            end=mid-1;
        else if(target>arr[mid])
            start=mid+1;
        else
            return mid;
    }
    return -1;
}

int n,m;
vector<int> arr,targets;

int main(){
    cin>>n;
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        arr.push_back(x);
    }
    sort(arr.begin(),arr.end());
    
    cin>>m;
    for(int i=0; i<m; i++){
        int target;
        cin>>target;
        targets.push_back(target);
    }
    
    for(int i=0; i<m; i++){
        int result=binarySearch(targets[i],arr,0,n-1);
    
        if(result==-1){
            cout<<"no"<<endl;
        }else{
            cout<<"yes"<<endl;
        }
    }
    
    return 0;
}
 */
