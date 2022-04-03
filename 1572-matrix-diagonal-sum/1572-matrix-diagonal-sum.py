class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        total=0
        if n%2!=0:
            for i in range(n):
                total+=(mat[i][i]+mat[i][n-i-1])
            total=total-mat[n//2][n//2]
        else:
            for i in range(n):
                total+=mat[i][i]+mat[i][n-i-1]
        return(total)