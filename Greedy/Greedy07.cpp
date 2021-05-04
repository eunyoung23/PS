//
//  Greedy07.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/31.
//
//0애서 1로 바뀌거나 1에서 0으로 바뀌는 시점의 개수 세기 --이걸 고민을 많이 함
/*
#include <iostream>

using namespace std;

string s;
int cnt0;
int cnt1;

int main(){
    cin>>s;
    
    if(s[0]=='0'){
        cnt1+=1;
    }else{
        cnt0+=1;
    }
    
    for(int i=0; i<s.size()-1; i++){
        if(s[i]!=s[i+1]){
            if(s[i+1]=='0'){
                cnt1+=1;
            }else{
                cnt0+=1;
            }
        }
    }

    cout<<min(cnt1,cnt0)<<"\n";
    
    return 0;
}
*/

/*
0001100->1
00011->1
10011->1
110110->2
1101101->2
*/

