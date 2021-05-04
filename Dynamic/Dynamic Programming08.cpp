#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> arr;

int main(){
    cin>>n;
    
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        arr.push_back(x);
    }
    
    reverse(arr.begin(), arr.end());
    
    int dp[2000];
    for(int i=0; i<n; i++){
        dp[i]=1;
    }
    
    //가장 긴 증가하는 부분 수열(LTS) 알고리즘
    for(int i=1; i<n; i++){
        for(int j=0; j<i; j++){
            if(arr[j]<arr[i]){
                dp[i]=max(dp[i],dp[j]+1);
            }
        }
    }
    
    int maxValue=0;
    for(int i=0; i<n; i++){
        maxValue=max(maxValue,dp[i]);
    }
    
    cout<<maxValue<<"\n";
    
    return 0;
}

