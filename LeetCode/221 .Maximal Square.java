class Solution {
    public int maximalSquare(char[][] matrix) {
        int[][] m = new int[matrix.length][matrix[0].length];
        int max=0;
        
        for(int i=0; i<matrix.length; i++){
            for(int j=0; j<matrix[i].length; j++){
               if(matrix[i][j]=='1'){
                   int tmp=(i==0 || j==0)?0:Math.min(Math.min(m[i-1][j],m[i][j-1]),m[i-1][j-1]);
                   m[i][j]=1+tmp;
                   max=Math.max(max,m[i][j]);
               } 
            }
        }
        
        
        return max*max;
    }
}
