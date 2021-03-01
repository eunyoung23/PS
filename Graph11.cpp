//
//  Graph11.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/03/01.
//
//절약할 수 있는 최대금액을 구해야하는 것을 알고 있어야 함.

#include <iostream>
#include <vector>

using namespace std;

int n,m;
int parent[200001];
vector<pair<int,pair<int,int>>> edges;
int result;

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

int main(){
    cin>>n>>m;
    
    for(int i=1; i<=n; i++){
        parent[i]=i;
    }
    
    for(int i=0; i<m; i++){
        int a,b,cost;
        cin>>a>>b>>cost;
        edges.push_back({cost,{a,b}});
    }
    
    sort(edges.begin(),edges.end());
    int total=0;
    
    for(int i=0; i<edges.size(); i++){
        int cost=edges[i].first;
        int a=edges[i].second.first;
        int b=edges[i].second.second;
        total+=cost;
        if(findParent(a)!=findParent(b)){
            unionParent(a,b);
            result+=cost;
        }
    }
    
    cout<<total- result<<"\n";
    
    return 0;
}

