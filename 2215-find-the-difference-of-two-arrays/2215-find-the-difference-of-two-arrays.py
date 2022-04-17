class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a1=[]
        a2=[]
        ans=[]
        for i in set(nums1):
            if i not in nums2:
                a1.append(i)
        ans.append(a1)
        for i in set(nums2):
            if i not in nums1:
                a2.append(i)
        ans.append(a2)
        return ans
                