class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=[]
        if n%2==0:
            for i in range(1,(n//2)+1):
                l.append(i)
                l.append(-(i))
        else:
            for i in range(1,(n//2)+1):
                l.append(i)
                l.append(-i)
        if len(l)!=n:
            l.append(0)
        return l