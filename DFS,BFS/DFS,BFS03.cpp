//
//  DFS,BFS03.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/02/02.
//
//각 노드별로 최단거리를 구하는 방법을 고민함
//탐색하는 알고리즘을 어떻게 최단거리를 구할지
//알맞은 노드 번호가 없을 때는 -1을 어떻게 출력할지

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n,m,k,x;
vector<int> graph[300001];
vector<int> d(300001, -1);

int main(){
    cin>>n>>m>>k>>x;
    
    for(int i=0; i<m; i++){
        int a,b;
        cin>>a>>b;
        graph[a].push_back(b);
    }
    
    d[x]=0;
    
    queue<int> q;
    q.push(x);
    while(!q.empty()){
        int node=q.front();
        q.pop();
        for(int i=0; i<graph[node].size(); i++){
            int nextnode=graph[node][i];
            if(d[nextnode]==-1){
                d[nextnode]=1+d[node];
            }else{
                if(d[nextnode]>d[node])   //값은 그대로 이므로 이거는 코드 작성 안해도 됨
                    d[node]=d[node];
            }
            q.push(nextnode);
        }
    }
    
  
    bool check=true;
    for(int i=1; i<=n; i++){
        if(d[i]==k){
            cout<<i<<"\n";
            check=true;
            }
        }
 
    if(!check)           //이 방법 생소했으므로 잘 기억하기
        cout<<-1<<"\n";
    
    return 0;
}

