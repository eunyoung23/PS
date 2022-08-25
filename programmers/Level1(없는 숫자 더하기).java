import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        for(int num=1; num<10; num++){
            boolean isInclude=contains(numbers,num);
            if(!isInclude){
                answer+=num;
            }
        }
        
        return answer;
    }
    
    public boolean contains(final int[] arr,final int key){
        return Arrays.stream(arr).anyMatch(i->i==key);
    }
}
