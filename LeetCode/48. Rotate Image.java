#case1
class Solution {
    public void rotate(int[][] matrix) {
        int n=matrix.length;
        for(int i=0; i<n/2; i++){ //i=0,1
            for(int j=i; j<n-i-1; j++){ //j=0,1 
                int t=matrix[i][j];
                
                matrix[i][j]=matrix[n-j-1][i];
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n-i-1]=t;
            }
        }
    }
}

#case2
class Solution {
    public void rotate(int[][] matrix) {
        int n=matrix.length;
        
        //reverse up and down
        for(int i=0; i<n/2; i++){
            for(int j=0; j<n; j++){
                int temp=matrix[i][j];
                matrix[i][j]=matrix[n-1-i][j];
                matrix[n-i-1][j]=temp;
            }
        }
        
        //reverse diagonally
        for(int i=0; i<n; i++){
            for(int j=i; j<n; j++){
                int temp=matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=temp;
            }
        }
        
    }
}
