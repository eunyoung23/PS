//
//  Sorting03.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/21.
//
//vector에 넣은 원소를 어떻게 꺼내는지 고민함 --> a[i]로
//A의 원소가 B의 원소보다 크거나 같을 떄, 반복문을 탈출하는 것도 고민해야 함
/*
#include <bits/stdc++.h>

using namespace std;

int N,K;
vector<int>a,b;

bool compare(int a,int b){
    return a>b;
}

int main(){
    cin>>N>>K;
    
    for(int i=0; i<N; i++){
        int x;
        cin>>x;
        a.push_back(x);
    }
    
    for(int i=0; i<N; i++){
        int y;
        cin>>y;
        b.push_back(y);
    }
    
    sort(a.begin(),a.end());
    sort(b.begin(),b.end(),compare);
    
    for(int i=0; i<K; i++){
        if(a[i]<b[i])swap(b[i],a[i]);
        else break;
    }
    
    int sum=0;
    for(int i=0; i<N; i++){
        sum+=a[i];
    }
    cout<<sum<<" ";
    
    return 0;
}
 */

