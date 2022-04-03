class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        i=0
        while i<len(nums):
            count=0
            for j in nums:
                if j<nums[i]:
                    count+=1
            l.append(count)
            i+=1
        return l