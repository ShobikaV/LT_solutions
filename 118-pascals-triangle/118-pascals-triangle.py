class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix=[]
        if numRows==1:
            matrix.append([1])
        else:
            matrix.append([1])
            prev_row=[]
            for i in range(1,numRows):
                row=[]
                for j in range(i+1):
                    if j==0 or j==i:
                        row.append(1)
                    else:
                        row.append(prev_row[j-1]+prev_row[j])
                prev_row=row
                matrix.append(row)
        return(matrix)
