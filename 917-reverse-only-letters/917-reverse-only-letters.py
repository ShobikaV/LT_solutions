class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l=list(s)
        i,j=0,len(s)-1
        while i<j:
            if  not l[i].isalpha():
                i+=1
            elif  not l[j].isalpha():
                j-=1
            else:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
        return "".join(l)