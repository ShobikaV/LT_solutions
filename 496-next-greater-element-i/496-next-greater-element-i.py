class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        d={}
        for i in nums2:
            while len(stack) and stack[-1]<i:
                d[stack.pop()]=i
            stack.append(i)
        for ind in range(len(nums1)):
            nums1[ind]=d.get(nums1[ind],-1)
        return nums1