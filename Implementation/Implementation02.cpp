//
//  Implementation02.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/18.
//
//시간 문자열을 어떻게 처리할 것인지 고민함.
//for문을 3번 돌리고 개수 세기 위해서 count변수를 사용한다는 것까지 생각함(3을 만나면 count변수 올라감)

/*
#include <bits/stdc++.h>

using namespace std;

int n;
int cnt=0;

bool check(int h,int m,int s){
    if(h/10==3 || h%10 ==3 || m/10==3 || m%10==3 || s/10==3 || s%10==3)
        return true;
    else
        return false;
}

int main(){
    cin>>n;
    
    for(int i=0; i<=n; i++){
        for(int j=0; j<60; j++){
            for(int z=0; z<60; z++){
               if(check(i,j,z)) cnt++;
            }
        }
    }
    
    cout<<cnt<<endl;
    
    return 0;
}
 */
