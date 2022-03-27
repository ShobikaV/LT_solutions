class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        flag=0
        arr.sort()
        d=arr[1]-arr[0]
        if len(arr)<=2:
            return True
        else:
            for i in range(2,len(arr)):
                if arr[i]-arr[i-1]==d:
                    flag=1
                else:
                    flag=0
                    break
        if flag:
            return True
        return False
                