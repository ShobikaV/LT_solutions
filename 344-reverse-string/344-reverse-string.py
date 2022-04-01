class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse()
        '''i,j=0,len(s)-1
        while i<=j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1'''
        n=len(s)
        for i in range(n//2):
            s[i],s[n-i-1]=s[n-i-1],s[i]
        