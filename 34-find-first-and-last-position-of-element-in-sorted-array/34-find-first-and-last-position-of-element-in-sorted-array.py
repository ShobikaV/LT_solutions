class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        if target not in nums:
            return [-1,-1]
        else:
            c=nums.count(target)
            i=nums.index(target)
            l.append(i)
            l.append(i+(c-1))
        return l