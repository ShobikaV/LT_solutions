class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans=""
        for i in s:
            if s.count(i)==1:
                ans=s.index(i)
                break
        if ans!="":
            return ans
        else:
            return -1