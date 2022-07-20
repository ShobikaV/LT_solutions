class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>1:
                flag=1
                break
            else:
                flag=0
        if flag:
            return True
        else:
            return False