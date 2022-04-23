class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        d={}
        j=0
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]>=j:
                    j=d[s[i]]+1
            ans=max(ans,i-j+1)
            d[s[i]]=i
        return ans