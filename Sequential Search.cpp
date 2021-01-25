//
//  Sequential Search.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/22.
//
// vector안에 자료형이 string도 가능함
//vector도 vector변수명[i]가 가능함
/*
#include <bits/stdc++.h>

using namespace std;

int sequentialSearch(int n,string target,vector<string> v){
    
    for(int i=0; i<n; i++){
        if(target==v[i]){
            return i+1;
        }
    }
    return -1;
}

int n;
string target;
vector<string> v;

int main(){
    cout<<"생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요"<<"\n";
    cin>>n>>target;
    
    cout<<"앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다."<<"\n";
    for(int i=0; i<n; i++){
        string s;
        cin>>s;
        v.push_back(s);
    }
    
    cout<<sequentialSearch(n, target, v)<<"\n";

    return 0;
}
 */
