import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answerList = new ArrayList<Integer>();
        
        for(int i=0; i<arr.length; i++){
            if (answerList.size()==0 || answerList.get(answerList.size()-1)!=arr[i]){
                answerList.add(arr[i]);
            }
        }

        return answerList.stream().mapToInt(i->i).toArray();
    }
}
