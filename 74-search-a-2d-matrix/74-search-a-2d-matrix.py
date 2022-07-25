class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag=0
        for i in matrix:
            if target in i:
                flag=1
            else:
                flag=0
            if flag:
                ans=True
                break
            else:
                ans=False
        return(ans)