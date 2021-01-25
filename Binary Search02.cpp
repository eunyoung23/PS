//
//  Binary Search02.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/22.
//
//벡터 arr을 넘길 때 별도로 값을 copy하지 않고 이미 존재하는 변수의 reference값을 넘김
 //만약 &를 빼면 기존의 값을 넘기기 위해서 값을 copy하므로 시간 복잡도가 O(N)이 걸림
/*
#include <bits/stdc++.h>

using namespace std;

int binarySearch(int target,vector<int>& arr,int start,int end){
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

int n,target;
vector<int> arr;

int main(){
    cin>>n>>target;
    
    for(int i=0; i<n; i++){
        int data;
        cin>>data;
        arr.push_back(data);
    }
    
    int result=binarySearch(target,arr,0,n-1);
    
    if(result==-1){
        cout<<"원소가 존재하지 않습니다"<<"\n";
    }else{
        cout<<result+1<<"원소가 존재합니다"<<"\n";
    }
    
    return 0;
}
*/
