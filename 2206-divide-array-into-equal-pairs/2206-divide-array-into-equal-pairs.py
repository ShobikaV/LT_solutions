class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a=set(nums)
        for i in a:
            if nums.count(i)%2==0:
                flag=0
            else:
                flag=1
                break
        if flag:
            return False
        else:
            return True