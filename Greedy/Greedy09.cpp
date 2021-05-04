//
//  Greedy09.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/02/01.
//
/*
#include <iostream>
#include<vector>

using namespace std;


int n;  //공의 개수
int m;  //공의 최대 무게
int arr[11];  //1부터 10까지의 무게를 담아야 하므로 11로 바꾸어야 함

int main(){
    int count=0; //개수 세기
    cin>>n>>m;
    
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        arr[i]=x;
    }
    
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            if(arr[i]!=arr[j])
                count+=1;
        }
    }
    
    cout<<count<<"\n";
    
    return 0;
}
*/
/*
int n,m;
int arr[11];

int main(void){
    cin>>n>>m;
    
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        arr[x]+=1;
    }
    
    int result=0;
    
    for(int i=1; i<=m; i++){
        n-=arr[i];
        result+=arr[i]*n;
    }
    
    cout<<result<<"\n";
}
*/
