class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1'''
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        nums[:len(l)]=l
        return len(l)