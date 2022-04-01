class Solution:
    def sortSentence(self, s: str) -> str:
        l=[]
        d={}
        ans=[]
        l=s.split()
        for i in l:
            a=i[len(i)-1:]
            d[int(a)]=i[:-1]
        for i in range(1,len(d)+1):
            ans.insert(i,d[i])
        return " ".join(ans)