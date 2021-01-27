//
//  Shortest Path02.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/27.
//
//시작노드는 제외해야 하므로 count값에다가 -1을 해야함
/*
#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

int n,m,start;
int d[30001];
vector<pair<int,int>>graph[30001];

void dijkstra(int start){
    priority_queue<pair<int,int>> pq;
    pq.push({0,start});
    d[start]=0;
    while(!pq.empty()){
        int dist=-pq.top().first;
        int now=pq.top().second;
        pq.pop();
        if(d[now]<dist)continue;
        for(int i=0; i<graph[now].size(); i++){
            int cost=dist+graph[now][i].second;
            if(cost<d[graph[now][i].first]){
                d[graph[now][i].first]=cost;
                pq.push(make_pair(-cost,graph[now][i].first));
            }
        }
    }
}

int main(){
    cin>>n>>m>>start;
    int count=0;
    
    for(int i=0; i<m; i++){
        int a,b,c;
        cin>>a>>b>>c;
        graph[a].push_back({b,c});
    }
    
    fill(d,d+30001,INF);
    
    dijkstra(start);

    int max_distance=0;
    for(int i=1; i<=n; i++){
        if(d[i]!=INF){
            count++;
            max_distance=max(max_distance,d[i]);
        }
    }
        
    cout<<count-1<<" "<<max_distance<<"\n";
    
    return 0;

}
*/
