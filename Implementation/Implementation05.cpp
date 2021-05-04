//
//  Implementation05.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/02/20.
//
//왜 long으로 변수 선언을 해야 하는지
//해설 정답으로 다시 한번 생각해보기

/*
#include <iostream>

using namespace std;

string str;
int sum1,sum2;

int main(){
    cin>>str;
    
    long n=str.size()/2;
    for(int i=0; i<n; i++){
        sum1+=int(str[i]);
    }
    
    for(int i=0; i<n; i++){
        sum2+=int(str[i+n]);
    }
    
    if(sum1==sum2){
        cout<<"LUCKY"<<endl;
    }else{
        cout<<"READY"<<endl;
    }
    
    return 0;
}
*/


/*
#include <iostream>

using namespace std;

string str;
int summary=0;

int main(){
    cin>>str;
    
    for(int i=0; i<str.size()/2; i++){
        summary+=str[i]-'0';
    }
    
    for(int i=str.size()/2; i<str.size(); i++){
        summary-=str[i]-'0';
    }


    if(summary==0){
        cout<<"LUCKY";
    }else{
        cout<<"READY";
    }
    return 0;
}
*/
