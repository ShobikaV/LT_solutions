#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
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

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends