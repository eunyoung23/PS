//
//  Graph09.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/02/28.
//
//서로소 집합으로 구해야할지 신장트리로 구해야 할지 고민함.
//같은 집합에 있는지 어떻게 따질지 고민함
#include <iostream>
#include <vector>

using namespace std;

int n,m;
int graph[501][501];
int parent[501];
vector<int> plan;

int findParent(int x){
    if(x==parent[x]) return x;
    return parent[x]=findParent(parent[x]);
}

void unionParent(int a,int b){
    a=findParent(a);
    b=findParent(b);
    if(a<b) parent[b]=a;
    else parent[a]=b;
}

bool result=true;

int main(){
    cin>>n>>m;
    
    for(int i=1; i<=n; i++){
        parent[i]=i;
    }
    
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            cin>>graph[i][j];
            if(graph[i][j]==1){
                unionParent(i,j);
            }
        }
    }
    
    for(int i=1; i<=m; i++){
        int x;
        cin>>x;
        plan.push_back(x);
    }
    
    for(int i=0; i<m-1; i++){
        if(parent[plan[i]]!=parent[plan[i+1]]){
            result=false;
        }
    }
    
    if(result){
        cout<<"yes"<<endl;
    }else{
        cout<<"no"<<endl;
    }
    
    return 0;
}

