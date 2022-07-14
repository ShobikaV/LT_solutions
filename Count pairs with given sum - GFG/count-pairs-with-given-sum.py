#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        d={}
        count=0
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range(n):
            if k-arr[i] in d:
                count+=d[k-arr[i]]
            if k-arr[i]==arr[i]:
                count-=1
        return count//2
            
                
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends