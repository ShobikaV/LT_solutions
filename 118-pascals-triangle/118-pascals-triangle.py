class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix=[]
        if numRows<3:
            for i in range(numRows):
                matrix.append([1]*(i+1))
        else:
            prev_row=[1,1]
            matrix.append([1])
            matrix.append(prev_row)
            for i in range(2,numRows):
                row=[0]*(i+1)
                for j in range(i+1):
                    if j==0 or j==i:
                        row[j]=1
                    else:
                        row[j]=prev_row[j-1]+prev_row[j]
                prev_row=row
                matrix.append(row)
        return(matrix)