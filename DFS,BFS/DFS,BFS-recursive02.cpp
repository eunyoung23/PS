//
//  DFS,BFS-recursive02.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/19.
//
//return 대신에 break를 사용할 수는 없음 - 반복문이 아니므로.
//왜 i를 전역변수로 선언하면 안되는지.
//함수의 반환값이 void이므로 return 0;을 하면 안됨.
/*
#include <bits/stdc++.h>

using namespace std;

void recursive_function(int i){
    if(i==10) return;
    cout<<i<<"번째 재귀 함수에서"<<i+1<<"번째 재귀함수를 호출합니다"<<"\n";
    recursive_function(i+1);
    cout<<i<<"번째 재귀 함수를 종료합니다"<<"\n";
}

int main(){
    recursive_function(1);
    
    return 0;
}
 */
