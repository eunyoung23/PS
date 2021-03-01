//
//  Dynamic Programming01.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/23.
//

#include <bits/stdc++.h>

using namespace std;
/*
int fib(int x){
    if(x==1 || x==2){
        return 1;
    }
    else{
        return fib(x-1)+fib(x-2);
    }
}

int main(){
    cout<<fib(4)<<" ";
    
    return 0;
}
*/
/*
long long d[100];

long long fibo(int x){
    if(x==1 || x==2){
        return 1;
    }
    if(d[x]!=0){
        return d[x];
    }
    d[x]=fibo(x-1)+fibo(x-2);
    return d[x];
}

int main(){
    cout<<fibo(50)<<"\n";
}
 */
/*
long long d[100];

int main(){
    d[1]=1;
    d[2]=1;
    int n=50;
    
    for(int i=3; i<=n; i++){
        d[i]=d[i-1]+d[i-2];
    }
    
    cout<<d[n]<<" ";
    
    return 0;
}
 */
