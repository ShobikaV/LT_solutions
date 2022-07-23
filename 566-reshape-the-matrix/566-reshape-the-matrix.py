class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        row,count=[],0
        ans=[]
        if m*n!=r*c:
            return mat
        else:
            for i in mat:
                for j in i:
                    count+=1
                    row.append(j)
                    if count==c:
                        ans.append(row)
                        row=[]
                        count=0
        return ans