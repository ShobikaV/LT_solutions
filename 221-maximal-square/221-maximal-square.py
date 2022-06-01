class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        t=[[int(matrix[i][j]) for j in range(n)]for i in range(m)]
        
        print(t)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if t[i][j]==1:
                    t[i][j]=min(t[i+1][j],t[i][j+1],t[i+1][j+1])+1
        ans=0
        for i in t:
            ans=max(ans,max(i))
        return ans**2