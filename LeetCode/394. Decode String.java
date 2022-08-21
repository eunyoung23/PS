/**
디코드 스트링문제가 재귀 문자라고 할 수 있음.
괄호가 어쩌고 저쩌고는 대부분 스택 문제이기는 함.
**/

class Solution {
    
    int idx=0;
    
    public String decodeString(String s) {
        return decodeString(s.toCharArray());
    }
    
    public String decodeString(char[] arr){
        StringBuilder sb=new StringBuilder();
        int count=0;
        while(idx<arr.length){
            char c=arr[idx];
            idx++;
            
            if(Character.isDigit(c)){
                count=count*10+Character.getNumericValue(c);
                
            }else if(c=='['){
                String inner=decodeString(arr);
                
                for(int i=0; i<count; i++){
                    sb.append(inner);
                }
                
                count=0;

            }else if(c==']'){
                break;
            }else{
                sb.append(c);
            }
            
        }
        return sb.toString();

    }
    
}
