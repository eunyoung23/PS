#include <iostream>

using namespace std;

int n,m;
int parent[100001];

int findParent(int x){
    if(x==parent[x]) return x;
    else return findParent(parent[x]);
}

void unionParent(int a,int b){
    a=findParent(a);
    b=findParent(b);
    if(a<b) parent[b]=a;
    else    parent[a]=b;
}

int main(){
    cin>>n>>m;
    
    for(int i=0; i<=n; i++){
        parent[i]=i;
    }
    
    
    for(int i=0; i<m; i++){
        int oper,b,c;
        cin>>oper>>b>>c;
        if(oper==0){
            unionParent(b, c);
        }if(oper==1){
            if(findParent(b)==findParent(c)){
                cout<<"yes"<<endl;
            }else{
                cout<<"no"<<endl;
            }
        }
    }

    
    return 0;
}

