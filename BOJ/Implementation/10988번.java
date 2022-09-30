/*
자바에서 문자열 거꾸로 정렬하는 방법 익히기
 */
package Baekjoon;

import java.util.Scanner;

public class baekjoon_10988 {
    public static void main(String[] args) {
        /*
        Scanner in=new Scanner(System.in);

        String word=in.next();

        StringBuffer sb=new StringBuffer(word);
        String reverse=sb.reverse().toString();

        if(word.equals(reverse)){
            System.out.println(1);
        }else{
            System.out.println(0);
        }*/
        Scanner in=new Scanner(System.in);
        String word=in.next();

        String example="";
        for(int index=word.length()-1; index>=0; index--){
            example+=word.charAt(index);
        }

        if(word.equals(example)){
            System.out.println(1);
        }else{
            System.out.println(0);
        }

    }
}
