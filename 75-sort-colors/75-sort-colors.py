class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans=[]
        zeros=nums.count(0)
        ones=nums.count(1)
        twos=nums.count(2)
        for i in range(zeros):
            nums[i]=0
        for i in range(zeros,zeros+ones):
            nums[i]=1
        for i in range(zeros+ones,zeros+ones+twos):
            nums[i]=2
        return nums