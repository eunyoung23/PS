#case1
class Solution:
    def rotate(self, matrix: List[List[int]]):
        n=len(matrix)
        for i in range(0,n//2):
            for j in range(i,n-1-i):
                t=matrix[i][j]
                
                matrix[i][j]=matrix[n-j-1][i]
                matrix[n-j-1][i]=matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1]=matrix[j][n-i-1]
                matrix[j][n-i-1]=t

                
#case2
class Solution:
    def rotate(self, matrix: List[List[int]]):
        n=len(matrix)
        for i in range(0,n//2):
            for j in range(n):
                tmp=matrix[i][j]
                matrix[i][j]=matrix[n-i-1][j]
                matrix[n-i-1][j]=tmp
                
                
        for i in range(0,n):
            for j in range(i,n):
                tmp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=tmp
                
#case3
class Solution:
    def rotate(self, matrix: List[List[int]]):
        n=len(matrix)
        for i in range(0,n//2):
            for j in range(n):
                matrix[i][j],matrix[n-i-1][j]=matrix[n-i-1][j],matrix[i][j]
                  
        for i in range(0,n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
