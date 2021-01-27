//
//  Shortest Path01.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/27.
//
/*
#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

int n,m;
int p,q;
int graph[101][101];

int main(){
    cin>>n>>m;
    
    for(int i=0; i<501; i++){
        fill(graph[i],graph[i]+101,INF);
    }
    
    for(int a=1; a<=n; a++){
        for(int b=1; b<=n; b++){
            if(a==b) graph[a][b]=0;
        }
    }
    
    for(int i=0; i<m; i++){
        int x,y;
        cin>>x>>y;
        graph[x][y]=1;
        graph[y][x]=1;
    }
    
    for(int k=1; k<=n; k++){
        for(int a=1; a<=n; a++){
            for(int b=1; b<=n; b++){
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b]);
            }
        }
    }
    
    cin>>p>>q;
    
    if(graph[p][q]==INF){
        cout<<-1<<" ";
    }else{
        cout<<graph[1][q]+graph[q][p]<<" ";
    }
    
    return 0;
}
*/
