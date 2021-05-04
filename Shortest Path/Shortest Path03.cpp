//
//  ShortestPath03.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/02/25.
// 몇 개가 왜 다르게 출력되는 지 모르겠음
//
#include <iostream>
#define INF 1e9

using namespace std;

int n,m;
int graph[101][101];

int main(){
    cin>>n;
    cin>>m;
    
    for(int i=0; i<101; i++){
        fill(graph[i],graph[i]+101,INF);
    }
    
    
    for(int a=1; a<=n; a++){
        for(int b=1; b<=n; b++){
            if(a==b){
                graph[a][b]=0;
            }
        }
    }
    
    // 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for (int i = 0; i < m; i++) {
        // A에서 B로 가는 비용은 C라고 설정
        int a, b, c;
        cin >> a >> b >> c;
        // 가장 짧은 간선 정보만 저장
        if (c < graph[a][b]) graph[a][b] = c;
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
                cout<<0<<" ";
            }
            else{
                cout<<graph[a][b]<<" ";
            }
        }
        cout<<"\n";
    }
    
    return 0;
}
