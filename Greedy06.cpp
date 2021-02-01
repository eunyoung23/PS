//
//  Greedy06.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/31.
//
//문자열 처리를 어떻게 할지 고민함
//문자를 숫자로 변경해햐 한다는 것을 모름
//0인 경우만 고려했는데 1인 경우도 고려해야함
/*
#include <iostream>

using namespace std;

string s;

int main(){
    cin>>s;
    int sum=s[0]-'0';
    
    for(int i=1; i<s.size(); i++){
        if(s[i]<=1 || sum<=1)
            sum+=s[i]-'0';
        else
            sum*=s[i]-'0';
    }
    cout<<sum<<" ";
    
    return 0;
}
*/
