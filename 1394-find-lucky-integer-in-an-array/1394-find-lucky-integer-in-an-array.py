class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for i in sorted(set(arr),reverse=True):
            if i==arr.count(i):
                return i
        return -1
        