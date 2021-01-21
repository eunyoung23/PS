//
//  Implementation01.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/18.
//
//고민한 부분: 정사각형에서 벗어나는 공간에 들어가면 어떻게 처리할지 / 배열을 이용할지 스택을 이용할지/ 문자열을 입력받으면 어떻게 처리할지
//string 문자열은 문자열[i]형태 사용가능함(배열 돌릴 수 있음), size()도 사용 가능함

/*
#include <bits/stdc++.h>

using namespace std;

int n;
int x,y=1;
string plans;

int dx[4]={-1,1,0,0};
int dy[4]={0,0,1,-1};
char moveTypes[4]={'L','R','U','D'};

int main(){
    cin>>n;
    cin.ignore();    //정수를 받은 뒤에 문자열을 받으면 버퍼를 지워줘야 함.
    getline(cin,plans);
   
    for(int i=0; i<plans.size(); i++){
        char plan=plans[i];
        if(plan==moveTypes[i]){
            int nx=x+dx[i];
            int ny=y+dy[i];
        }
        if(nx<1 || nx>n ||ny<1 || ny>n) continue;

    }
    
    cout<<nx<<" "<<ny<<endl;
    
    return 0;
}
 */
 
