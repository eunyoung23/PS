#include <iostream>
#include <vector>

using namespace std;

int binarySearch(vector<int>& arr,int start,int end){
    int mid=(start+end)/2;
    
    while(start<=end){
        if(arr[mid]==mid)
            return mid;
        else if(mid<arr[mid])
            end=mid-1;
        else
            start=mid+1;
    }
    return -1;
}

int n;
vector<int> arr;

int main(){
    cin>>n;
    
    for(int i=0; i<n; i++){
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }
    
    int index=binarySearch(arr,0,n-1);
    
    cout<<index<<"\n";
    
    return 0;
}
