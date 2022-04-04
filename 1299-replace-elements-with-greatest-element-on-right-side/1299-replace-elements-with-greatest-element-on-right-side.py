class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)):
            if len(arr[i+1:])!=0:
                ans.append(max(arr[i+1:]))
            else:
                ans.append(-1)
        return ans