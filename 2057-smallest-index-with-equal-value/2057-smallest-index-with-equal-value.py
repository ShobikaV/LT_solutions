class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        a=''
        for i in range(len(nums)):
            if i%10==nums[i]:
                a=i 
                break
        if a=='':
            return -1
        else:
            return a
            