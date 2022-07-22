class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans=[]
        n=len(matrix)
        for i in range(n):
            a=[]
            for j in range(n-1,-1,-1):
                a.append(matrix[j][i])
            ans.append(a)
        matrix[:]=ans
        return matrix
    
