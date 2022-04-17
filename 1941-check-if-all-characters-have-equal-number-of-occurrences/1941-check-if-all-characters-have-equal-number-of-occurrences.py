class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        flag=0
        for i in s:
            d[i]=s.count(i)
        a=min(d.values())
        for i in d:
            if d[i]==a:
                flag=1
            else:
                flag=0
                break
        if flag:
            return True
        else:
            return False