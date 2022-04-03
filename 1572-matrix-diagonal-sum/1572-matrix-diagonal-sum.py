class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        total=0
        for i in range(n):
            total+=(mat[i][i]+mat[i][n-i-1])
        if n%2!=0:
            total=total-mat[n//2][n//2]
        return(total)