//
//  Implementation06.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/02/20.
//
//숫자인지 문자인지 어떻게 구분하는지 모름--isaplha라는 함수를 사용함
//알파벳 순서를 내림차순으로 어떻게 배치할지 --(알파벳을 아스키 코드로 인식하나??)
//c++ 문자열과 문자부분 다시 공부하기
//문자열을 받아서 어떻게 문자 한개 한개로 인식할지

#include <iostream>
#include <vector>
using namespace std;

string str;
int sum=0;
vector<char> result;

int main(){
    cin>>str;

    for(int i=0; i<str.size(); i++){
        if(isalpha(str[i])){
            result.push_back(str[i]);
        }
        else{
            sum+=str[i]-'0';
        }
    }
    
    sort(result.begin(),result.end());
    
    for(int i=0; i<result.size(); i++){
        cout<<result[i];
    }
    
    if(sum!=0){
        cout<<sum<<" ";
    }
    
    return 0;
}
