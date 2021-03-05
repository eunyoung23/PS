//
//  Implementation03.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/01/18.
//
//a1을 좌표로 어떻게 처리할지/ 체스판에서 벗어날떄 어떻게 할지 고민함
//char형을 int형을 변환하는 방법 - 아스키코드를 이용함.
//27행에서 발생한 문제 복습하기

/*
#include <bits/stdc++.h>

using namespace std;

int dx[]={2,2,-2,-2,1,1,-1,-1};
int dy[]={-1,1,-1,1,-2,2,-2,2};
string inputData;

int main(){
    cin >> inputData;
    int row = inputData[1] - '0';
    int column = inputData[0] - 'a' + 1;
    int count=0;
    
    for(int i=0; i<8; i++){
        int nextRow=row+dx[i];   //row+=data[i]; 했을때 왜 답이 잘못 나오는지
        int nextColumn=column+dy[i];
        if(nextRow>=1 && nextRow<=8 && nextColumn>=1 && nextColumn<=8){
            count +=1 ;
        }
    }
    
    cout<<count<<" ";
    
    return 0;
}
 */

