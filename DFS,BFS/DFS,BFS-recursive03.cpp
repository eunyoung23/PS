//
//  DFS,BFS-recursive03.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/19.
//
/*
#include <bits/stdc++.h>

using namespace std;

int recursive_function1(int i){
    int result=1;
    for(int j=1; j<=i; j++){
        result*=j;
    }
    return result;
}

int recursive_function2(int i){
    
    if(i<=1) return 1;
    return i*recursive_function2(i-1);
}

int main(){
    cout<<"반복적으로 구현: "<<recursive_function1(5)<<" ";
    cout<<"재귀적으로 구현: "<<recursive_function2(5)<<" ";
    
    return 0;
}
*/
