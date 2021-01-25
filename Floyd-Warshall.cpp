//
//  Floyd-Warshall.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/25.
//
//점화식에 따라 프로이드 워셜 알고리즘 짜는 법 고민함

#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

int n,m;
int graph[501][501];

int main(){
    cin>>n>>m;
    
    for(int i=0; i<501; i++){
        fill(graph[i],graph[i]+501,INF);
    }
    
    for(int a=1; a<=n; a++){
        for(int b=1; b<=n; b++){
            if(a==b) graph[a][b]=0;
        }
    }
    
    for(int i=0; i<m; i++){
        int x,y,z;
        cin>>x>>y>>z;
        graph[x][y]=z;
    }
    
    for(int k=1; k<=n; k++){
        for(int a=1; a<=n; a++){
            for(int b=1; b<=n; b++){
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b]);
            }
        }
    }
    
    for(int a=1; a<=n; a++){
        for(int b=1; b<=n; b++){
            if(graph[a][b]==INF){
                cout<<"INFINTY"<<" ";
            }
            else{
                cout<<graph[a][b]<<" ";
            }
        }
        cout<<"\n";
    }
    return 0;
}
