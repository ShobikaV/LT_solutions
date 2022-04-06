class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]&1:
                nums[j],nums[i]=nums[i],nums[j]
                j-=1
            else:
                i+=1
        return(nums)