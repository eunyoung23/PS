//마지막의 cost값을 어떻게 뺐는지 생각해보기
#include <iostream>
#include <vector>

using namespace std;

int n,m;
int result=0;
int parent[100001];
int last;
vector<pair<int,pair<int,int>>> edges;

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
        int a,b,c;
        cin>>a>>b>>c;
        edges.push_back({c,{a,b}});
    }
    
    sort(edges.begin(),edges.end());
    
    for(int i=0; i<edges.size(); i++){
        int cost=edges[i].first;
        int a=edges[i].second.first;
        int b=edges[i].second.second;
        if(findParent(a)!=findParent(b)){
            unionParent(a,b);
            result+=cost;
            last=cost;
        }
    }
    
    cout<<result-last<<"\n";
    
    return 0;
}
 
