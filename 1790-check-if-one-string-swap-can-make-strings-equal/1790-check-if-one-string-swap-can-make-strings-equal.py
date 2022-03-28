class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        if s1==s2:
            return True
        l1=[];
        l2=[];
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
                l1.append(s1[i]);
                l2.append(s2[i]);
                if count>2:
                    return False
        if count==2:
            if(l1[0]==l2[1] and l2[0]==l1[1]):
                return True
        return False