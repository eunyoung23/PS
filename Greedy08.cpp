//
//  Greedy08.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/31.
//조합을 어떻게 표현할지 고민함
//
/*
#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> a;

int main(){
    cin>>N;
    
    for(int i=0; i<N; i++){
        int x;
        cin>>x;
        a.push_back(x);
    }
    
    sort(a.begin(),a.end());
    
    int max=0;
    for(int i=0; i<N; i++){
        max+=a[i];
    }
    
    bool visited[max];
    int sum=0;
    
    fill_n(visited,max,false);
    int j=0;
    
    for(int i=0; i<N; i++){
        while(j<N-i){
            sum+=a[i+1];
            visited[sum]=true;
            j++;
        }
    
    }
    
    for(int i=1; i<max; i++){
        if(!visited[i]){
            cout<<i<<" ";
            break;
        }
    }
    return 0;
}
 */

