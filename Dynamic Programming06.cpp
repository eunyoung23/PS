//
//  Dynamic Programming06.cpp
//  CodingTest_w
//
//  Created by 이은영 on 2021/02/14.
//
//정수 사각형 입력을 어떻게 받을지

#include <iostream>

using namespace std;

int n;
int arr[500][500];

int main(){
    cin>>n;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            cin>>arr[i][j];
        }
    }

    
    for(int i=1; i<n; i++){
        for(int j=0; j<=i; j++){
            int upleft,up;
            if(j==0)upleft=0;
            else upleft=arr[i-1][j-1];
            if(i==j)up=0;
            else up=arr[i-1][j];
            arr[i][j]=arr[i][j]+max(upleft,up);
        }
    }

    int result=0;
    for(int j=0; j<n; j++){
        result=max(result,arr[n-1][j]);
    }
    cout<<result<<"\n";
    
    return 0;
}

/*   최댓값을 이런식으로 구하려고 했움
for(int i=0; i<n; i++){
    for(int j=0; j<=i; j++){
        result=arr[i][j];
        if(arr[i+1][j]>arr[i+1][j+1]) {
            result=arr[i+1][j];
        }
        else {
            result=arr[i+1][j+1];
        }
    }
}
*/
