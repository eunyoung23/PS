//
//  Dynamic Programming05.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/02/11.
//
//3개의 수를 max할때는 어떻게 하는지
//arr[20][20]사용하는 방법
//어떻게 케이스를 다 출력할지

#include <iostream>

using namespace std;

int t,a,b;
int arr[20][20];
int dp[20][20];

int main(){
    cin>>t;
    
    for(int z=0; z<t; z++){
        cin>>a>>b;
        for(int i=0; i<a; i++){
            for(int j=0; j<b; j++){
                cin>>arr[i][j];
            }
        }

    for(int i=0; i<a; i++){
        for(int j=0; j<b; j++){
            dp[i][j]=arr[i][j];
        }
    }
    
    for(int j=1; j<b; j++){
        for(int i=0; i<a; i++){
            int leftUp,left,leftDown;
            if(i==0) {
                leftDown=dp[i+1][j-1];
                leftUp=0;
            }if(i==a-1){
                leftDown=0;
                leftUp=dp[i-1][j-1];
            }else{
                leftDown=dp[i+1][j-1];
                leftUp=dp[i-1][j-1];
            }
            left=dp[i][j-1];
            dp[i][j]=dp[i][j]+max(max(left,leftUp),leftDown);
        }
    }
    int result=0;

    for(int i=0; i<a; i++){
        result=max(result,dp[i][b-1]);
    }
    cout<<result<<"\n";
    
    }
    return 0;
}

/*  원래는 이렇게 해서 최댓값 구할려고 했음
for(int j=0; j<a; j++){
    max=arr[j][0];
    for(int z=0; z<b; z++){
        if(max<arr[j][z]){
            max=arr[j][z];
        }
    }
}
*/
