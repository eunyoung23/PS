//
//  Dynamic Programming04.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/24.
//
#include <iostream>
#include <vector>

using namespace std;

int n,m;
vector<int> arr;

int main(){
    cin>>n>>m;
    
    int d[m];
    d[0]=0;
    for(int i=1; i<=m; i++){
        d[i]=10001;
    }
    
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        arr.push_back(x);
    }
    
    for(int i=0; i<n; i++){
        int cnt=arr[i];
        for(int j=cnt; j<=m; j++){
            if(d[j-cnt]!=10001)
            d[j]=min(d[j],d[j-cnt]+1);
        }
    }
    
    
    if(d[m]==10001){
        cout<<-1<<"\n";
    }else{
        cout<<d[m]<<"\n";
    }
    
    return 0;
}
 
