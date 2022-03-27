class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=[]
        ans=[]
        l=s.split()
        for i in range(k):
            ans.append(l[i])
        return (" ".join(ans))