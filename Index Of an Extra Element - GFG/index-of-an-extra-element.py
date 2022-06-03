class Solution:
    def findExtra(self,a,b,n):
        i,j=0,0
        b.append(0)
        while(i<=n):
            if(a[i]!=b[j]):
                return a.index(a[i])
            i+=1
            j+=1
        

#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends