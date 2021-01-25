//
//  Binary Search.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/22.
// 재귀함수 앞에 return자를 써야하는지 몰랐음
//
/*
#include <bits/stdc++.h>

using namespace std;

int binarySearch(int target, vector<int> arr, int start,int end){
    if(start>end) return -1;
    int mid=(start+end)/2;
    
    if(target<arr[mid]){
        return binarySearch(target,arr,start,mid-1);
    }
    else if(target>arr[mid]){
        return binarySearch(target,arr,mid+1,end);
    }
    else{
        return mid;
    }
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
    
    int result=binarySearch(target, arr, 0 , n-1);
    if(result==-1){
        cout<<"원소가 존재하지 않습니다."<<"\n";
    }else{
        cout<<result+1<<"\n";
    }
    return 0;
}
 */
