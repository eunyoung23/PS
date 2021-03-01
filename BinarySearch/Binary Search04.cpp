//
//  Binary Search04.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/22.
//
//binarysearch를 꼭 함수로 따로 구현하지 않아도 됨
/*
#include <bits/stdc++.h>

using namespace std;

int n,m;
vector<int> arr;

int main(){
    cin>>n>>m;
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        arr.push_back(x);
    }
    
    int start=0;
    int end=arr[n-1];
    
    int result=0;
    while(start<=end){
        long long int total=0;
        int mid=(start+end)/2;
        for(int i=0; i<n; i++){
            total+=arr[i]-mid;
        }
        if(m>total){
            end=mid-1;
        }
        else{
            result=mid;
            start=mid+1;
        }
            
    }
    cout<<result<<"\n";
    
    return 0;
}
*/
