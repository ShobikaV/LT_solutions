class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        a=prod([nums[j],nums[j-1]])
        b=prod([nums[i],nums[i+1]])
        return abs(b-a)