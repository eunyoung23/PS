//
//  DFS,BFS02.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/19.
//
/*
#include <bits/stdc++.h>

using namespace std;

int n,m;
int graph[200][200];

bool bfs(int x,int y){
    if(x<=-1 || x>=n || y<=-1 || y>=n){
        return false;
    }
    if(graph[x][y]==1){
        bfs(x-1,y);
        bfs(x+1,y);
        bfs(x,y+1);
        bfs(x,y-1);
    }
}

int main(){
    cin>>n>>m;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%1d",&graph[i][j]);
        }
    }
    
    
    return 0;
}
*/
