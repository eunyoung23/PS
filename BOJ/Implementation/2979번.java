package Baekjoon;

import java.util.Scanner;

public class baekjoon_2979 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int A=in.nextInt();
        int B=in.nextInt();
        int C=in.nextInt();
        int result=0;

        int[] arr=new int[100];

        for(int i=0; i<3; i++){
            int start=in.nextInt();
            int end=in.nextInt();
            for(int j=start; j<end; j++){
                arr[j]+=1;
            }
        }

        for(int index=0; index<100; index++){
            if(arr[index]==3){
                result+=C*3;
            }else if(arr[index]==2){
                result+=B*2;
            }else if(arr[index]==1){
                result+=A;
            }
        }

        System.out.println(result);
    }
}
