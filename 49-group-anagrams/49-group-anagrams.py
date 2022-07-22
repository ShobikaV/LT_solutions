class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        d={}
        for i in strs:
            l="".join(sorted(i))
            if l not in d:
                d[l]=[]
            d[l].append(i)
        for j in d:
            ans.append(d[j])
        return ans  