//
//  DFS,BFS 01.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/19.
//
//N*M 행렬 입력받는 방법을 고민함, 아예 코딩 방법을 방향을 못 잡음
/*
#include <bits/stdc++.h>

using namespace std;

int n,m;
int graph[1000][1000];

using namespace std;

bool dfs(int x,int y){
   
    if(x<=-1||x>=n||y<=-1||y>=m){
        return false;
    }
    if(graph[x][y]==0){
        graph[x][y]=1;
        dfs(x,y-1);
        dfs(x,y+1);
        dfs(x-1,y);
        dfs(x+1,y);
        return true;
    }
    return false;
}

int main(){
    cin>>n>>m;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%1d", &graph[i][j]);
        }
    }
    
    int result=0;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(dfs(i,j)) result+=1;
        }
    }
    
    cout<<result<<"\n";
    return 0;
}
 */
